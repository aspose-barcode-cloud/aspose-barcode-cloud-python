import argparse
import re

PROP_SETTER_DECORATOR_RE = re.compile(r"^\s+@(?P<prop_name>[^.]+)\.setter$")
DEPRECATED_RE = re.compile(r"^\s*DEPRECATED:\s+(?P<message>[^#]+)")
COMMENT_ENDED_RE = re.compile(r'^(?P<indent>\s*)"""$')


def main(input_file):
    filename = input_file.name
    content = [line.rstrip() for line in input_file.readlines()]
    input_file.close()

    with open(filename, "wt") as result:
        property_name = None
        deprecation_message = None

        for line in content:
            match_with_prop_name = PROP_SETTER_DECORATOR_RE.match(line)
            if match_with_prop_name:
                # comment section started
                property_name = match_with_prop_name.groupdict()["prop_name"]
                deprecation_message = None

            deprecated_match = DEPRECATED_RE.match(line)
            if property_name and deprecated_match:
                # deprecation message found
                deprecation_message = deprecated_match.groupdict()["message"].strip()

            match_with_indent = COMMENT_ENDED_RE.match(line)
            if match_with_indent:
                if deprecation_message:
                    # comment section ended
                    result.write(line + "\n")

                    indent = match_with_indent.groupdict()["indent"]
                    result.write(
                        f'{indent}warnings.warn(\n{indent}    "'
                        f"Property '{property_name}' is deprecated. {deprecation_message}"
                        f'",  # noqa: E501\n{indent}    category=DeprecationWarning,\n{indent})\n'
                    )
                    property_name = None
                    deprecation_message = None

                    continue

                property_name = None
                deprecation_message = None

            result.write(line + "\n")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=argparse.FileType("rt"))
    args = parser.parse_args()
    return vars(args)


if __name__ == "__main__":
    main(**parse_args())

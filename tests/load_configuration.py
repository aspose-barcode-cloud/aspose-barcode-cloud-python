from __future__ import absolute_import, division

import inspect
import json
import logging
import os
import six

from aspose_barcode_cloud import Configuration

logger = logging.getLogger(__name__)

DEFAULT_CONFIG_FILENAME = os.path.join(os.path.split(os.path.abspath(__file__))[0], "configuration.json")
DEFAULT_ENV_PREFIX = "TEST_CONFIGURATION"


def from_file(filename):
    """
    @rtype: Configuration
    """
    logger.debug("Loading test configuration from file '%s'..." % filename)
    with open(filename, "r") as json_file:
        js = json.load(json_file)

    return Configuration(**js)


def from_env(prefix):
    """
    @rtype: Configuration
    """
    logger.debug("Loading test configuration from env with prefix '%s'..." % prefix)
    constructor_param_names = (
        inspect.getargspec(Configuration.__init__) if six.PY2 else inspect.getfullargspec(Configuration.__init__)
    ).args[1:]
    kwargs = {}
    for name in constructor_param_names:
        env_name = "%s_%s" % (prefix, name.upper())
        value = os.environ.get(env_name)
        if value is not None:
            logger.warning("Set '%s' from environ to %s" % (env_name, name))
            kwargs[name] = value

    return Configuration(**kwargs)


TEST_CONFIGURATION = (
    from_file(DEFAULT_CONFIG_FILENAME) if os.path.isfile(DEFAULT_CONFIG_FILENAME) else from_env(DEFAULT_ENV_PREFIX)
)

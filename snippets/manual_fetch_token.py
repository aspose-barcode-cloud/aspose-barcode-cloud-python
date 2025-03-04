import requests


def main():
    client_id = "Client Id from https://dashboard.aspose.cloud/applications"
    client_secret = "Client Secret from https://dashboard.aspose.cloud/applications"

    base_url = "https://id.aspose.cloud/"
    endpoint = "connect/token"

    # Check the client_id is changed to not break github ci pipeline
    if client_id.startswith("Client Id"):
        print("client_id not configured. Skip this snippet test")
        return

    payload = {"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}

    response = requests.post(f"{base_url}{endpoint}", data=payload)
    response.raise_for_status()

    data = response.json()
    token = data["access_token"]
    print("Token recieved successfully")
    # Uncomment next line to view token
    # print(token)


if __name__ == "__main__":
    main()

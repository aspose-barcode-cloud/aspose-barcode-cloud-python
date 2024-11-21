import requests

def main():
    client_id = "<Your-Client-Id>"
    client_secret = "<Your-Client-Secret>"

    base_url = "https://id.aspose.cloud/"
    endpoint = "connect/token"

    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    try:
        response = requests.post(f"{base_url}{endpoint}", data=payload)
        response.raise_for_status() 
        
        data = response.json()
        print(data)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

if __name__ == "__main__":
    main()

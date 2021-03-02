import requests

def main():
    # response = requests.get("http://www.google.com")
    # print("Status Code: ",response.status_code)
    # print("Headers: ",response.headers)
    # print("Content-Type: ",response.headers['Content-Type'])
    # print("Html Content: ",response.text)

    payload = {"base": "USD", "symbols": "SEK"}
    resp = requests.get("https://api.exchangeratesapi.io/latest", params=payload)
    if resp.status_code != 200:
        print("Status Code: ",resp.status_code)
        raise Exception("There was an error")

    print("Content-Type: ",resp.headers['Content-Type'])
    
    data = resp.json()
    print("Json Data: ", data)

if __name__ == "__main__":
    main()
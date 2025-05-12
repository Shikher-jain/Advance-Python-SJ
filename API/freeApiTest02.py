import requests

def fetch_get_stock_freeapi():

    url = "https://api.freeapi.app/api/v1/public/stocks"
    response = requests.get(url)
    data = response.json()  
    print(data['success'])
    
    # print(response)
    # print(data)

    if data['success'] and "data" in data:

        user = data["data"]
        print(f"Name: { user['name']['title'] +" "+ user['name']['first'] +" "+ user['name']['last']}")
        print(f"User Name: {user['login']['username']}")
        print(f"Country: {user['location']['country']}")
        print(f"Phone: {user['phone']}")

    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        fetch_get_stock_freeapi()
        print("Stock data fetched successfully!")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to fetch user stock.")

if __name__ == "__main__":
    main()
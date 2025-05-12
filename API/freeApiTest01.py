import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    # print(response)
    data = response.json()  
    # print(data)
    print(data['success'])

    if data['success'] and "data" in data:

        user = data["data"]
        print(f"Name: { user['name']['title'] +" "+ user['name']['first'] +" "+ user['name']['last']}")
        print(f"User Name: {user['login']['username']}")
        print(f"Country: {user['location']['country']}")
        print(f"Phone: {user['phone']}")

    else:
        raise Exception("Failed to fetch user data")


fetch_random_user_freeapi()
                            
def main():
    try:
        fetch_random_user_freeapi()
        print("User data fetched successfully!")
    except Exception as e:
        print(f"Error: {e}")
        print("Failed to fetch user data.")

if __name__ == "__main__":
    main()

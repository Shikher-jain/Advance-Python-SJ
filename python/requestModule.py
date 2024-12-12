import requests
from bs4 import BeautifulSoup

url="https://www.google.com"
response=requests.get(url) 
# print(response.text)

soup = BeautifulSoup(response.text,'html.parser')
# print(soup.prettify())

for headings in soup.find_all("div"):
    print(headings.text)

# url="https://jsonplaceholder.typicode.com/posts"

# data={
#     "title":"request",
#     "userID":"12345" ,
#     "Body":"module"
# }
# headers={
#     "Content-type":"application/json;charset=UTF-8"
# }
# response=requests.post(url,headers=headers,json=data)
# print(response.text)


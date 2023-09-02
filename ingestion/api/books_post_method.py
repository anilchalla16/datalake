import requests as re
from requests.auth import HTTPBasicAuth
import json

with open(r"D:\datalake\ingestion\api\files\bearer_token.json","r") as file:
    token_read = json.load(file)
    token_read = token_read["accessToken"]
url = "https://simple-books-api.glitch.me/orders"

headers = {
    "Authorization"  :token_read,
    "Content-Type":"application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

json_data = {
  "bookId": 1,
  "customerName": "John"
}
post_response = re.post(url,headers=headers,json=json_data)
print(post_response.json())
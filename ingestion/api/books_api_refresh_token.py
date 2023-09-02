import requests as re
import json


with open(r"D:\datalake\ingestion\api\files\bearer_token.json","r") as file:
    data = json.load(file)
    data = data["accessToken"]
    print(data)


url = "https://simple-books-api.glitch.me/api-clients/"
headers = {
    "Authorization"  :data,
    "Content-Type":"application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
json_body = {
   "clientName": "Postman",
   "clientEmail": "challaanil16644@gmail.com"
}
post_response = re.post(url,headers=headers,json=json_body)
print(post_response.json())
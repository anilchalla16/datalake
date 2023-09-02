import requests as re
import json


url = "https://simple-books-api.glitch.me/api-clients/"
headers = {
    "Content-Type":"application/json",
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br"
}

json_body = {
   "clientName": "Postman",
   "clientEmail": "challaanil934666@gmail.com"
}

response  = re.post(url,headers=headers,json=json_body).json()
print(response)






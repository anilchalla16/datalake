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
   "clientEmail": "challaanil964@gmail.com"
}

response  = re.post(url,headers=headers,json=json_body)
if response.status_code == 201:  # Successful authentication
    print("Bearer token:", response)
    data = response.json()
    data = json.dumps(data, indent=4)
    with open(r"D:\datalake\ingestion\api\files\bearer_token.json","w") as token_gen:
        token_gen.writelines(data)
        print("Bear token generated successful")
else:
    print("Authentication failed with status code:", response.status_code)





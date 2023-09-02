import requests as re
import json

base_url = "https://simple-books-api.glitch.me"
get_uri = "books"
url = base_url + "/" + get_uri
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
response = re.get(url, headers=headers)
if response.status_code==200:
    output_json = response.json()
else:
    pass


data = json.dumps(output_json,indent=4)
with open(r"D:\datalake\ingestion\api\files\sample.json","w") as f:
  f.writelines(data)
print("file is loaded")



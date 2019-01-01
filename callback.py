import requests

url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
api_key = ""  # see the key on yandex
querystring = {"key": api_key,
               "text": "heir", "lang": "en-it", "format": "plain"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "be2664d9-36d3-41cf-b44b-4c83d865e887"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

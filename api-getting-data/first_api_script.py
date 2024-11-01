import requests

url = 'https://the-one-api.dev/v2/character'
response = requests.get(url)
print(response.status_code)


api_key = "..."
url = 'https://the-one-api.dev/v2/character'
authorization_headers = {
	'Authorization: Bearer ' + api_key
}

response = requests.get(url, headers=authorization_headers)
print(response.status_code)


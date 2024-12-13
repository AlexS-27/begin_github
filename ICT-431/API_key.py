import requests

url = "http://10.229.33.64/rest/V1/integration/admin/token"
data = {
    "username": "API",
    "password": "227227Ak!"
}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Jeton :", response.text)
else:
    print("Erreur :", response.status_code, response.text)


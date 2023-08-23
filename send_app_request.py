import requests

url = 'http://127.0.0.1:5000'
login = url + "/login"

payload = {
    'name': 'admin',
    'password': 'helloworld1234',
}

result = requests.post("http://127.0.0.1:5000/login", data=payload)
print(result.content)

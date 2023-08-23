import requests

url = 'http://127.0.0.1:5000'
login = url + "/login"

payload = {
    'username': 'donald',
    'email': 'donald@gmail.com',
    'password': 'helloworld1234',
}

s = requests.Session()

result = s.post(login, data={'name': 'donald', 'password': 'helloworld1234'})
print(result.status_code)
print(result.text)

result = s.get(url + "/user/3")
print(result.status_code)
print(result.text)

result = s.get(url + "/logout")
print(result.status_code)
print(result.text)

result = s.get(url + "/user/3")
print(result.status_code)
print(result.text)



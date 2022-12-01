import requests
from bs4 import BeautifulSoup

url = 'http://mathpong.web.ctfcup.ru'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
payload = {
    'auth': 'none',
    'desc': 'return api description',
    'params': 'none'
}

r = requests.get(url, headers=headers, data=payload)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)
# print(r)
url = 'http://mathpong.web.ctfcup.ru/api/signup'
payload = {
    "auth": "none",
    "desc": "signup method. needed to create your account. needed login and password",
    "params": "{'login': 'lil_bunny', 'password': 'test_'}"
}
r = requests.post(url, headers=headers, json=payload)
# print(r)
# print(BeautifulSoup(r.content, 'html.parser'))

url = 'http://mathpong.web.ctfcup.ru/api/signin'
payload = {
    "auth": "none",
    "desc": "signin method. needed to create your account. needed login and password. sets a cookie to work with api",
    "params": "{'login': 'lilbunny', 'password': 'test'}"
}
r = requests.post(url, headers=headers, json=payload)
print(r)
r2 = requests.post(url, headers=headers, json=payload)
print(r2.cookies['auth'])
print(BeautifulSoup(r.content, 'html.parser'))


cookies = {'auth': r2.cookies['auth']}



url = 'http://mathpong.web.ctfcup.ru/api/task'
payload = {
    "auth": "required",
    "desc": "return a task to mine coins",
    "params": "none"
}
r = requests.get(url, headers=headers, json=payload, cookies=cookies)

print(r)
print(BeautifulSoup(r.content, 'html.parser'))



url = 'http://mathpong.web.ctfcup.ru/api/user'
payload = {
    "auth": "required",
    "desc": "return a user info",
    "params": "none"
}
r = requests.get(url, headers=headers, json=payload,  cookies=cookies)
print(r)
print(BeautifulSoup(r.content, 'html.parser'))



url = 'http://mathpong.web.ctfcup.ru/api/shop'
payload = {
    "auth": "required",
    "desc": "return a price for a flag",
    "params": "none"
}
r = requests.get(url, headers=headers, json=payload, cookies=cookies)
print(r)
print(BeautifulSoup(r.content, 'html.parser'))


url = 'http://mathpong.web.ctfcup.ru/api/shop'
payload = {
    "auth": "required",
    "desc": "try to buy a flag",
    "params": "none"
}
r = requests.post(url, headers=headers, json=payload, cookies=cookies)
print(r)
print(BeautifulSoup(r.content, 'html.parser'))


url = 'http://mathpong.web.ctfcup.ru/api/shop'
payload = {
    "auth": "required",
    "desc": "try to buy a flag",
    "params": "none"
}
r = requests.post(url, headers=headers, json=payload, cookies=cookies)
print(r)
print(BeautifulSoup(r.content, 'html.parser'))



# "POST /api/shop":{"auth":"required","desc":"try to buy a flag","params":"none"}
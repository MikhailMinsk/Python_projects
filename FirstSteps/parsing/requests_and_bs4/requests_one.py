import requests

r = requests.get('https://api.github.com/events')
print(r.text)
# print(r.raw)
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

# passing arguments
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)

payload = {'key1': 'value1', 'key2[]': ['value2', 'value3']}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'user-agent': 'rtfm/0.0.1'}
r = requests.post("http://httpbin.org/post", data=payload, headers=headers)
print(r.text)


bad_r = requests.get('http://httpbin.org/status/404')
try:
    bad_r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print('ERROR: %s' % e)

requests.get('http://github.com', timeout=0.001)






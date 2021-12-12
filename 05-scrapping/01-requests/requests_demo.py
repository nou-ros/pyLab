import requests

'''
r = requests.get('https://xkcd.com/353/')
# components of the r
print(dir(r))
# description of the components
print(help(r))
# html
print(r.text)
# status_code
print(r.status_code)
# true for anyother than 400 
print(r.ok)
r.headers
print(r.headers)
'''
# download image
'''
img = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.png', 'wb') as f:
    f.write(img.content)
'''


# https://httpbin.org/ to check http methods 

'''
# GET
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
'''
'''
# POST
payload = {'username': 'dev', 'password': 'dev12'}
r = requests.post('https://httpbin.org/post', data=payload)
# print(r.json())
r_dict = r.json()
print(r_dict['form'])
'''
'''
# auth - with wrong password r will return 404
r  = requests.get('https://httpbin.org/basic-auth/nouros/testing', auth=('nouros', 'testing'))

# print(r.text)
print(r)
'''

# delay - if takes more than 3 seconds than this will time out. 
r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)
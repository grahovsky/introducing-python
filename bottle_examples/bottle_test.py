import requests

resp = requests.get('http://localhost:9999/echo/Max')
if resp.status_code == 200 and \
    resp.text == 'Say hello to my little friend: Max!':
    print('It worked! That almost never happens!')
else:
    print('Argh, go this:', resp.text)
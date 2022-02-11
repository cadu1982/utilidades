import requests
import http.client

request = requests.get('https://eost3x8tn4c57r.m.pipedream.net')
get = request.json()
print(get['about'])

post = requests.post('https://eost3x8tn4c57r.m.pipedream.net', data={'Carlos':'Diego'})

put = requests.put('https://eost3x8tn4c57r.m.pipedream.net', data={'Carlos':'Diego'})

delete = requests.delete('https://eost3x8tn4c57r.m.pipedream.net', data={'Carlos':'Diego'})

# conn = http.client.HTTPSConnection('eo9lc0xvxjwrps9.m.pipedream.net')
# conn.request("POST", "/", '{ "test": "event"}', {'Content-Type': 'application/json'})
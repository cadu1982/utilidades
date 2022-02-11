import requests

request = requests.get('https://api.chucknorris.io/jokes/random')

caminho = request.json()

print(caminho['icon_url'])


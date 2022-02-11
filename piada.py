import requests

request = requests.get('https://api.chucknorris.io/jokes/random')

piada = request.json()

print(piada['value'])
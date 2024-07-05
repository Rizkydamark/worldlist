import requests

api_key = 'b28eb97b-ff7f-4dcd-804e-c236d1cc79cc'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
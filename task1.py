import requests


payload = {
    'lang': 'ru',
    'M': '',
    'q': '',
    'n': '',
    'T': ''
}

cities = [
    'Лондон',
    'Шереметьево',
    'Череповец'
]

url_template = 'https://wttr.in/{}'

for city in cities:
    url = url_template.format(city)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)

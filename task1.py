import requests


url_template = 'https://wttr.in/{}?lang=ru&MqnT'

url_london = url_template.format('Лондон')
response_london = requests.get(url_london)
response_london.raise_for_status()

url2_sheremethvo = url_template.format('Шереметьево')
response_sheremethvo = requests.get(url2_sheremethvo)
response_sheremethvo.raise_for_status()

url_cherepovec = url_template.format('Череповец')
response_cherepovec = requests.get(url_cherepovec)
response_cherepovec.raise_for_status()

print(response_london.text)
print(response_sheremethvo.text)
print(response_cherepovec.text)
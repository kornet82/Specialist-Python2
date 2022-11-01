import requests
import json
from pprint import pprint

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
# Variant 1
data_dict1 = json.loads(response.text)
# Variant 2
data_dict2 = response.json()

pprint(data_dict1)
pprint(data_dict2)
print(data_dict1['Valute']['EUR']['Value'])
print(data_dict2['Valute']['USD']['Value'])



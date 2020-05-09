import requests, pprint

token= 'f1e8f0db52193aec776f3b4d6ac0a40d90f90577'
header = {'Authorization': f'Token {token}'}  # Без слова токен не работает
response = requests.get('http://127.0.0.1:8000/api/v0/exportcountries_api/', headers=header)
pprint.pprint(response.json())
import requests

domain='https://transparency.entsog.eu/api/v1/connectionpoints'
url=f'{domain}?limit=100'
result=requests.get(url).json()
pointType=set([i['pointType'] for i in result['connectionpoints']])
commercialType=set([i['commercialType'] for i in result['connectionpoints']])




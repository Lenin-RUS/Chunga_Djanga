import requests
import time


urls=('http://yandex.ru', 'http://rbc.ru', 'http://google.com')

def elps_time(url):
    return requests.get(url).elapsed

DB_NAME = 'mydb1'
result = requests.post('http://localhost:8086/query', {'q': f'CREATE DATABASE {DB_NAME}'}).json()
client = InfluxDBClient(database='mydb1')

def url_answer_time():
    json_data = []
    for i, url in enumerate(urls):
        zzz=elps_time(url)
        data = {
            'measurement': 'url_answer',
            'tags': {
                'url': url
            },
            'fields': {
                'value': str(zzz)
            }
        }

        json_data.append(data)

    print(json_data)
    return client.write_points(json_data)


if __name__ == '__main__':
    while True:
        url_answer_time()
        time.sleep(1)

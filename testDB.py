# Сохранение данных в influxdb с помощью influxdb
import time
from influxdb import InfluxDBClient
import psutil

client = InfluxDBClient(database='cpuusage')


def save_cpu_load():
    json_data = []
    for cpu, load in enumerate(psutil.cpu_percent(percpu=True)):
        data = {
            'measurement': 'percpu',
            'tags': {
                'cpu': f'cpu{cpu}',
                'server': 'localhost'
            },
            'fields': {
                'value': load
            }
        }
        json_data.append(data)

    print(json_data)
    return client.write_points(json_data)


if __name__ == '__main__':
    while True:
        save_cpu_load()
        time.sleep(1)
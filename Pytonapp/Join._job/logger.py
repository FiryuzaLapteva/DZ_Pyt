from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Pytonapp/Join._job/log.csv', 'a') as file:
        file.write('{}; temperature;{}\n'.format(time,data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Pytonapp/Join._job/log.csv', 'a') as file:
        file.write('{}; pressure;{}\n'.format(time,data))

def wine_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('Pytonapp/Join._job/log.csv', 'a') as file:
        file.write('{}; wine_speed;{}\n'.format(time,data))
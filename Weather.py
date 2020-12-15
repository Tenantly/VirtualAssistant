import requests
city = input('City?')
api_url = 'https://api.openweathermap.org/data/2.5/weather'

params = {
    'q': city,
    'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
    'units': 'metric',
    'lang': 'ru'
}

res = requests.get(api_url, params = params)
#print(res.status_code)
#print(res.headers['Content-Type'])
#print(res.json())
data = res.json()
template = 'Погода в городе {}: {}, температура {} градусов'
print(template.format (city, data['weather'][0]['description'], data['main']['temp']))
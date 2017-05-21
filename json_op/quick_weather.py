import json, requests, sys

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % location
res = requests.get(url)
res.raise_for_status()
weather_data = json.loads(res.text)
# 取出json串中的list对象列表
w = weather_data['list']

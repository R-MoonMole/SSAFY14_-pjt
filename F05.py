import requests
from collections import defaultdict
from datetime import datetime
import statistics

# 날씨 설명 교정 맵핑
description_mapping = {
    '온흐림': '흐림',
    '튼구름': '구름 조금',
    '가벼운 비': '약한 비',
    '맑음': '맑음',
    '흐림': '흐림',
    '구름 조금': '구름 조금',
    '약한 비': '약한 비',
    '비': '비',
    '천둥구름': '뇌우',
    '눈': '눈',
    '박무': '안개'
}

# 날씨 이모지 맵핑
weather_emoji = {
    '맑음': '☀️',
    '흐림': '☁️',
    '구름 조금': '🌤️',
    '약한 비': '🌦️',
    '비': '🌧️',
    '눈': '❄️',
    '뇌우': '⛈️',
    '안개': '🌫️'
}

def get_five_day_forecast(city_name, api_key):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'kr'
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f'API 요청 실패: {response.status_code}')
        return

    data = response.json()['list']

    daily_data = defaultdict(list)

    # 날짜별로 그룹핑
    for entry in data:
        dt_txt = entry['dt_txt']
        date = dt_txt.split(' ')[0]  # yyyy-mm-dd
        weather_desc = entry['weather'][0]['description']
        corrected_desc = description_mapping.get(weather_desc, weather_desc)
        emoji = weather_emoji.get(corrected_desc, '')

        daily_data[date].append({
            'temp': entry['main']['temp'],
            'feels_like': entry['main']['feels_like'],
            'temp_max': entry['main']['temp_max'],
            'temp_min': entry['main']['temp_min'],
            'weather': corrected_desc,
            'emoji': emoji
        })

    # 날짜별 평균값 계산 및 출력
    print(f'📍 {city_name} 지역의 5일간 날씨 예보:')
    print('-' * 40)

    today = datetime.today().date()

    for date_str, entries in daily_data.items():
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
        if date_obj < today:
            continue  # 과거 데이터 제외

        temps = [e['temp'] for e in entries]
        feels = [e['feels_like'] for e in entries]
        maxs = [e['temp_max'] for e in entries]
        mins = [e['temp_min'] for e in entries]
        weather = entries[0]['weather']
        emoji = entries[0]['emoji']

        print(f'📅 {date_str} {emoji} {weather}')
        print(f'   🌡️ 온도: {round(statistics.mean(temps), 1)}°C')
        print(f'   🧍 체감온도: {round(statistics.mean(feels), 1)}°C')
        print(f'   🔼 최고기온: {round(max(maxs), 1)}°C')
        print(f'   🔽 최저기온: {round(min(mins), 1)}°C')
        print('-' * 40)

# 예시 실행
api_key = '6cb951cf1d8c34ced7d86ba0c1519b81'  # <- 여기에 발급받은 OpenWeather API 키를 입력하세요
get_five_day_forecast('Seoul', api_key)
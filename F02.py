from pprint import pprint
import requests

# Openweather API 를 활용하여 특정 지역의 "현재 날씨"에 대한 정보를 출력하세요.
# 서울의 위도:37.56, 경도:126.97

# 날씨 데이터 변수에 할당
weather_data = {}
original_data = {}
def get_seoul_weather():
    global weather_data
    global original_data
    # OpenWeatherMap API 키
    API_key = 'e1f011915a9b1500a0292c1d8e310cfe'

    # 서울의 위도
    lat = 37.56
    # 서울의 경도
    lon = 126.97

    # API 요청 URL
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

    # API 요청 보내기
    weather_data = requests.get(url).json()

    # main 키와 weather 키의 값만 추출하여 새로운 딕셔너리 생성
    original_data = {'main': weather_data['main'], 'weather': weather_data['weather']}
    return original_data
    

pprint(get_seoul_weather())
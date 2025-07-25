from pprint import pprint
import requests

# Openweather API 를 활용하여 특정 지역의 "현재 날씨"에 대한 정보를 출력하세요.
# 서울의 위도:37.56, 경도:126.97

# 날씨 데이터 변수에 할당
weather_data = {}
dummy_data = {}
def get_seoul_weather():
    global weather_data
    global dummy_data
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
    # key 값만 리스트에 담기
    dummy_data = weather_data.keys()
    return dummy_data

print(get_seoul_weather())

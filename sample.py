from pprint import pprint
import requests

# Openweather API 를 활용하여 특정 지역의 "현재 날씨"에 대한 정보를 출력하세요.
# 서울의 위도:37.56, 경도:126.97


def get_seoul_weather():
    # OpenWeatherMap API 키
    API_key = 'e1f011915a9b1500a0292c1d8e310cfe'

    # 서울의 위도
    lat = 37.56
    # 서울의 경도
    lon = 126.97

    # API 요청 URL
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

    # API 요청 보내기
    response = requests.get(url).json()
    return response

# 날씨 데이터 변수에 할당
weather_data = get_seoul_weather()

# 날씨 데이터 key 값만 리스트에 담기
dummy_data = list(weather_data.keys())
print(dummy_data)

# main 키와 weather 키의 값만 추출하여 새로운 딕셔너리 생성
original_data = {'main': weather_data['main'], 'weather': weather_data['weather']}
pprint(original_data)

# key 값들을 모두 한글로 변환
translated_main_data = {'체감온도': original_data['main']['feels_like'],
                        'None' : original_data['main']['grnd_level'],
                        '습도' : original_data['main']['humidity'],
                        '기압' : original_data['main']['pressure'],
                        '해수면기압' : original_data['main']['sea_level'],
                        '온도' : original_data['main']['temp'],
                        '최고온도' : original_data['main']['temp_max'],
                        '최저온도' : original_data['main']['temp_min'],}

translated_weather_data = {'요약': original_data['weather'][0]['description'],
                           '아이콘' : original_data['weather'][0]['icon'],
                           '식별자' : original_data['weather'][0]['id'],
                            '핵심' : original_data['weather'][0]['main']}

translated_data = {'기본': translated_main_data, '날씨': translated_weather_data}

# 한글로 변환된 데이터에 섭씨 온도 데이터를 추가
translated_data['기본'].update({'온도(섭씨)': round(((translated_data['기본']['온도'] - 32) * 5 / 9), 2),
                                '체감온도(섭씨)': round(((translated_data['기본']['체감온도'] - 32) * 5 / 9), 2),
                                '최고온도(섭씨)': round(((translated_data['기본']['최고온도'] - 32) * 5 / 9), 2),
                                '최저온도(섭씨)': round(((translated_data['기본']['최저온도'] - 32) * 5 / 9), 2)})
pprint(translated_data)

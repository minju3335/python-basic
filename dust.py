import requests
from pprint import pprint # python 안에 존재, 예쁘게 보이게 함

URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2B58fRxySTvs0PfFQUY4WIxmfUdNzO2PRCGrFR%2BwurNXadOEb4nRyU4TfZFft%2FX7IOwZchblSbWUzs2S9mm1q2Q%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"

res = requests.get(URL)

# print(res) 
#파이썬 코드로 API 요청을 하는 것

data = res.json()
# pprint(data) #pprint 뎁스 구조를 바꿔준다

# pprint(data['response']['body'])
# pprint(data['response']['body']['items'])
#값이 대괄호로 나오는데 인덱스로 접근해야한다는 것
# pprint(data['response']['body']['items'][13])


#여기서 강남구를 찾고싶어, 원하는 거 뽑는 것
items = data['response']['body']['items']
for item in items:
    if item['stationName'] == '강남구':
        pprint(item['pm10Value'])
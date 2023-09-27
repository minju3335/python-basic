numbers = [1, 2, 3, 4, 5]


max_num = max(numbers)
print(max_num)


import random
random_number = random.randint(1, 100)
print(random_number)

#######

menus = ['김밥', '라면', '만두']
random_number = random.randint(0, 2)
print(menus[random_number])


menu = random.choice(menus)
print(menu)


######

numbers = range(1, 46) #range 범위는 이상, 미만
lucky_number = random.sample(numbers, 6)
print(sorted(lucky_number)) #sorted는 값을 정렬해서 출력해줌



####
URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'

# pip install requests 모듈
import requests

res = requests.get(URL)
data = res.json() #dictionary 구조


# print(res)
# print(res.text) #string이고 값
# print(res.json()) # dictionary 구조, 함수임

# print(data) #dictionary 구조


drwtNo1 = data['drwtNo1'] #drwNo는 URL에 있던 변수
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

# print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)

# print(data['drwNoDate'])

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

print(lucky_number)
print(lotto_number)

print(set(lucky_number) & set(lotto_number)) # set는 집합의 형태로 바꿔줌
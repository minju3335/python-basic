# 1. apple / Apple 대/소문자 주의
# 2. git add. / git add . 띄어쓰기 주의
# 3. message / massage 오타 주의

# 변수, variable
dust = 10 # 값을 대입, 할당하다. 할당한다는 의미의 =

# print(dust)
# 주석처리는 Ctrl + /

dust = '10' # 같은 변수에 할당하면 덮어씌운다
print(dust)


# 1. 숫자
dust = 10
# 2. 글자
dust = '5'
# 3. 참/거짓(boolean)
dust = True #or False  #True와 False의 첫문자는 대문자


# 리스트 : 여러 개의 데이터가 나열되어있는 형태
dust_list = [10, 20, 0, 50, 100]
print(dust_list[3])

# 딕셔너리 : 사전처럼 표현
# key : value 형태
dust_dict = {
    '서울': 100,
    '대전': 10,
    '부산': 50,  # 콜론 앞은 붙어쓰고 뒤에는 한칸 뛰어쓰기
}
print(dust_dict)
print(dust_dict['부산'])
# PEP8 python style guide 참고해서 쓰기


# 2. 조건
age = 10

if age > 20:
    print('성인입니다.')
elif age > 8:
    print('청소년입니다.')
else:
    print('어린이입니다.')



dust = 100 

# dust 150보다 크다면 => 매우나쁨
# 80~150 => 나쁨
# 30~79 => 보통
# 0~29 => 좋음
if dust > 150:
    print('매우나쁨')
elif 80 <= dust < 150:
    print('나쁨')
elif 30 <= dust < 79:
    print('보통')
else :
    print('좋음')



# 3. 반복
menus = ['짜장면', '김밥', '라면', '피자']

n = 0
while n < 4: #오른쪽 코드가 True면 밑에 코드를 실행
    print(menus[n])
    n = n + 1


for menu in menus
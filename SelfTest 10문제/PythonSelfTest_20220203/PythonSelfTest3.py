# 문제 3

'''
나이에 따라 지하철 교통요금 출력하는 프로그램을 작성하시오.
8세 미만의 어린이의 지하철 교통요금은 450원이다.
8세 이상 19세 이하의 청소년 지하철 교통요금은 720원이다.
20세 이상의 성인 지하철 교통요금은 1250원이다.
'''

age = int(input('나이를 입력하세요 : '))

if(age < 8):                  # 8세 미만 요금
    print("어린이 요금 450원")
elif 8<= age <=19:           # 8세 이상 19세 이하 요금
    print("청소년 요금 720원")
else:                        # 20세 이상 성인 요금
    print("성인 요금 1250원")  
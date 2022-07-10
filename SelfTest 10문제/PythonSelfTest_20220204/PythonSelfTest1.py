# 문제 1
'''
시험점수를 입력받아
90 ~ 100점은 A,
80 ~ 89점은 B,
70 ~ 79점은 C,
60 ~ 69점은 D,
나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''

number = int(input("시험점수를 입력해주세요 : "))

if(90 <= number <= 100):     # 90 ~ 100점은 A등급
    print('A')
elif(80 <= number <= 89):   # 80 ~ 89점은 B등급
    print('B')
elif(70 <= number <= 79):   # 70 ~ 79점은 C등급
    print('C')
elif(60 <= number <= 69):   # 60 ~ 69점은 D등급
    print('D')
else:            # 그 외 나머지 F등급
    print('F')
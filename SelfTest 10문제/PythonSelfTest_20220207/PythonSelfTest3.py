# 문제 3 
'''
사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
'''

num1 = int(input("첫번째 숫자 입력: "))
num2 = int(input("두번째 숫자 입력: "))
num3 = int(input("세번째 숫자 입력: "))

if(num1 >= num2 and num1 >= num3):    # num1 입력 숫자가 num2, num3보다 크면 num1 출력
    print(num1)
elif(num2 >= num1 and num2 >= num3): # num2 입력 숫자가 num1, num3보다 크면 num2 출력
    print(num2)
else:          # num3 입력 숫자가 num1, num2보다 크면 num3 출력
    print(num3)
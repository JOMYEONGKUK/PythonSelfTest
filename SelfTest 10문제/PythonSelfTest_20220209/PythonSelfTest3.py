# 문제 3
'''
사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
'''

# 첫번째, 두번째, 세번째 숫자 입력
num1 = int(input("첫번째 숫자를 입력해주세요: "))
num2 = int(input("두번째 숫자를 입력해주세요: "))
num3 = int(input("세번째 숫자를 입력해주세요: "))

if num1 >= num2 and num1 >= num3:  # 첫번째 숫자가 두번째 세번째 숫자보다 크거나 같으면 첫번째 숫자를 출력
    print(num1)
elif num2 >= num1 and num2 >= num3:  # # 두번째 숫자가 첫번째 세번째 숫자보다 크거나 같으면 두번째 숫자를 출력
    print(num2)
else:             # 그 외 값은 세번째 숫자를 출력
    print(num3)
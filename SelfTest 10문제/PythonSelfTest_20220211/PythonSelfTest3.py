# 문제 3
'''
숫자를 추측해서 맞추는 프로그램을 만드시오.
'''

import random

n = random.randint(1, 30)   # 1~30 사이에 있는 임의의 수를 뽑습니다.

while True:                # 영원히 반복합니다.
    x = input("맞혀보세요? ")
    g = int(x)              # 입력받은 값을 비교할 수 있도록 정수로 바꿉니다.
    if(g == n):            # 사용자가 추측한 값과 수가 같으면 정답
        print("정답")
        break             # 정답을 맞히면 브레이크로 반복문을 멈춤
    if(g < n):
        print("작습니다.")
    if(g > n):
        print("큽니다.")
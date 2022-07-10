# 문제 4
'''
# 10 ~ 99 까지 사이의 난수를 n개 생성하는 프로그램을 만드시오
단, 13 이 나오면 중단하시오.
'''

import random

# 난수의개수 입력
n = int(input("난수의 개수를 입력하세요: "))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end= ' ')
    if r == 13:   # 난수 출력 후 13이 나오면 프로그램 중단
        print("프로그램을 중단합니다.")
        break

# 난수 출력 후 13이 나오지 않으면 난수 생성 종료
else:
    print("난수 생성을 종료합니다.")
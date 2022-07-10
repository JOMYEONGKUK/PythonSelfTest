# 문제 3
'''
*개를 n개 출력하되 w개마다 줄바꿈을 하는 프로그램을 만드시오.
'''

print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요? "))
w = int(input("몇 개마다 줄바꿈할까요? "))

for i in range(n):     # n번 반복합니다.
    print('*', end='')
    if i % w == w - 1: # n번 판단
        print() # 줄바꿈
        
if n % w:      # 1번 판단
    print()    # 줄바꿈
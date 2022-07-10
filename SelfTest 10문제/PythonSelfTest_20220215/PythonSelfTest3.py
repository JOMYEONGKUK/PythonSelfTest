# 문제 3
'''
특정 문자를 줄바꿈 없이 연속으로 출력하는 프로그램을 만들어보시오.
'''

print("a와 b를 번갈아 출력합니다.")
x = int(input("몇개를 출력하겠습니까? ")) # 문자 입력

for i in range(x):
    if i % 2:    
        print('-', end='') # 홀수인 경우 -를 출력함
    else:
        print('+', end='') # 짝수인 경우 +를 출력함
        
print()
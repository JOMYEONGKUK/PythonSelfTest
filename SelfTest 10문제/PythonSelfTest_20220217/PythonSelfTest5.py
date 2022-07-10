# 문제 5
'''
이중 루프로 구구단 곱셉표를 출력하는 프로그램을 입력하시오.
'''

print('-' * 27)
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end = '')
    print() # 행 변경 
print('-' * 27)
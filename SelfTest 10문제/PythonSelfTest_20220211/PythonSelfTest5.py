# 문제 5
'''
1부터 n까지 곱을 구하는 함수를 만들어라.
'''

def factorial(n):
    fact = 1      # 곱을 구하기 위한
    for x in range(1, n+1): # range로 1부터 n까지 반복합니다.
        fact = fact * x     # 지금까지 계산된 값에 x를 곱해 fact에 다시 저장합니다.
    return fact            # 계산된 fact 값을 돌려줍니다.

print(factorial(5))
print(factorial(10))
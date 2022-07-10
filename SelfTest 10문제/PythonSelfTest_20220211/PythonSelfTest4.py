# 문제 4
'''
1부터 n까지의 합을 구하는 함수를 만들어라.
'''
def sum_func(n):
    s = 0            # 합을 구하기 위한 변수 s를 0으로 지정
    for x in range(1, n+1):  # range로 1부터 n까지 반복합니다.
        s = s+x            # s 값에 xx 를 더해서 s로 다시 저장합니다.
    return s              # 계산된 s 값을 결괏값으로 돌려줍니다.

print(sum_func(10))
print(sum_func(100))
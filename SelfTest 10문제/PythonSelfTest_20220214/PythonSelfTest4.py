# 문제 4
'''
최소값을 구하는 프로그램을 함수를 사용해서 만드시오.
'''

# 함수의 정의
def number_a(b):
    n = len(b)    # 입력 길이
    min_v = b[0]  # 리스트 중 첫번째 값을 최소값
    for i in range(1, n):  # 1부터 n까지 반복
        if b[i] < min_v:   # 이번 값이 현재까지 기억된 값보다 작으면
            min_v = b[i]   # 최소값을 변경
    return min_v

# 함수의 호출
v = [18, 92, 18, 33, 58, 7, 33, 42]
print(number_a(v))
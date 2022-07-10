# 문제 3
'''
입력으로 돌아오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.(단 입력으로
들어오는 수의 개수는 정해져 있지 않다.)
'''

# 함수의 정의
def arg(*args):
    result = 0
    for i in args:
        result = result + i
    return result/len(args)  # 호출한 숫자를 개수만큼 나눗셈 한 후 반환

# 함수의 호출
arg(1,2,3,4,5,6,7,8,9,10)
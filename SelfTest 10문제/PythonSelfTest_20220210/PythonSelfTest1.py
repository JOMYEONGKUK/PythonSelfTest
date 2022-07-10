# 문제 1
'''
두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation
함수를 작성하라.
'''

# 함수의 정의
def print_arithmetic_operation(a,b):
    print(a, '+', b, '=', a+b)  # 덧셈 값
    print(a, '-', b, '=', a+b)  # 뺄셈 값
    print(a, '*', b, '=', a+b)  # 곱셈 값
    print(a, '/', b, '=', a+b)  # 나눗셈 값
    
# 함수의 호출   
print_arithmetic_operation(3, 4)
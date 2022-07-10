# 문제 5
'''
1 ~ 100까지의 수 중에서 홀수와 홀수의 합을 실행 결과와 같이 출력하는
프로그램을 작성하시오.
'''

result = 0

# 반복문 정의
for i in range(1, 101):
    if i % 2 == 1:
        if i == 99:  # 99인 경우에는 '+' 부호 대신 '=' 출력함
            print(i, end=' = ')
        
        else:
            print(i, end=' + ')
        
        result += i
    
# 반복문 실행
print(result)
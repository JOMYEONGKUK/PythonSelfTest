# 문제 1
'''
8개의 정수가 있는 리스트에서 특정 정수의 위치를 전부 찾는 프로그램을 
함수를 사용해서 만드시오.
'''

# 함수의 정의
def number_list(a, x):
    n = len(a)  # 입력 크기와 길이 n
    result = []    # 새 리스틀 만들어 결과값을 저장함
    for i in range(0, n):   # 리스트 a의 모든 값을 차례로
        if x == a[i]:       # x 값과 비교하여
            result.append(i) # 같으면 위치 길이 번호를 결과에 추가함
            
    return result   # 결과 리스트를 반환해줌


v = [17, 92, 18, 33, 58, 7, 33, 42] # v 변수 리스트 정수 8개 값
print(number_list(v, 18)) # [2] 인덱싱 기준으로 2번
print(number_list(v, 33)) # [3,6] 33이 인덱싱 기준으로 리스트에 두번 나옴
print(number_list(v, 900)) # [] 900 이란 정수는 리스트에 없기 때문에 공백
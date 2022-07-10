# 문제 2
'''
학생 번호에 해당하는 학생 이름을 찾는 프로그램을 get_name 함수를 사용해서
만드시오.
'''

# 함수의 정의
def get_name(s_no, s_name, find_no):
    n = len(s_no)              # 입력 크기와 길이
    for i in range(0, n):
        if find_no == s_no[i]:  # 학생 번호가 찾는 학생 번호와 같으면
            return s_name[i]   # 해당하는 학생 이름을 결과로 반환함
        
    return "몰라요"    # 결과를 못찾았으면 몰라요 출력

sam_no = [39, 14, 67, 105]
sam_name = ["Justin", "John", "Mike", "Summer"]

# 함수 출력
print(get_name(sam_no, sam_name, 105))
print(get_name(sam_no, sam_name, 777))
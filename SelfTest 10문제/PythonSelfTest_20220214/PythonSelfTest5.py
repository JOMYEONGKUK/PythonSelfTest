# 문제 5
'''
사람이 총 n명일 때 두명을 뽑아 짝으로 만드는 프로그램을 만드시오.
'''

# 함수의 정의
def print_pro(a):
    n = len(a)           # 리스트의 자료 개수를 n에 저장
    for i in range(0, n - 1):     # 0부터 n-2까지 반복
        for j in range(i + 1, n):  #i + 1부터 n-1까지 반복
             print(a[i], "-", a[j])
                
name = ["Tom", "Jerry", "Mike"]
print_pro(name)
print()
name2 = ["Tom", "Jerry", "Mike", "John"]
print_pro(name2)
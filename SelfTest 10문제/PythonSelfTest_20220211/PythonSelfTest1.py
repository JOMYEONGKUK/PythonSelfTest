# 문제 1
'''
a와 b를 오름차순으로 정렬한 다음 해당 범위의 모든 정수를 더하는 프로그램입니다.
'''

print("a부터 b까지 정수의 합을 구합니다.")

print()

# a와 b 정수 입력
a = int(input("정수 a를 입력하세요: "))
b = int(input("정수 b를 입력하세요: "))

print()

if(a > b):
    a, b = b,a # a와 b를 오름차순으로 정렬
    
sum = 0
for i in range(a, b + 1):
    sum += i      # sum에 i를 더합니다.

# 출력합니다.
print("{}부터 {}까지의 정수의 합은 {}입니다.".format(a, b, sum))
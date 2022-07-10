# 문제 1
'''
주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민등록 번호를 입력
받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라.
지역코드 : 00 ~ 08 출생지 : 서울
지역코드 : 09 ~ 12 출생지 : 부산
'''

number = input("주민등록번호 입력: ") # 주민등록번호 입력
number2 = number.split("-")[1]  # 주민번호 앞자리와 뒷자리 사이를 split 함수로 공백을 기준으로 "-" 나눔
if 0 <= int(number2[1:3]) <= 8: # 숫자 0이 뒷자리 1번째 3번째보다 작거나 같고 뒷자리 1번째 3번째 숫자가 8보다 작거나 같으면 서울입니다. 출력
    print("서울입니다.")
else:   # 그 외 서울이 아닙니다. 출력
    print("서울이 아닙니다.")
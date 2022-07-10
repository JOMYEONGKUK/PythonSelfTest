# 문제 4
'''
휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를
입력 받고, 통신사를 출력하는 프로그램을 작성하라.
번호 통신사
011  SKT
016  KT
019  LGU
010  알수없음
'''
number1 = input("휴대폰번호 입력: ")
b = number1.split("-")[0]

if(b == "011"):
    print("SKT")
elif(b == "016"):
    print("KT")
elif(b == "019"):
    print("LGU")
else:
    print("알수없음")
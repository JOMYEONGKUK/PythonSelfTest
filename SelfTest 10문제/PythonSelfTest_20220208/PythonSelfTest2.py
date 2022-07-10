# 문제 2
'''
투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이
투자 경고 종목이라면 '투자 경고 종목입니다.'를 아니면"투자 경고 종목이 아닙니다
"를 출력하는 프로그램을 작성하라.

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
'''
# 투자 경고 종목명 입력
x = input("종목명: ")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG"]

# 종목값이 warn_investment_lis 안에 있으면 투자 경고 종목입니다. 출력
if x in warn_investment_list:
    print("투자 경고 종목입니다.")
# 종목값에 없는 종목이 나오면 투자 경고 종목이 아닙니다 출력
else:
    print("투자 경고 종목이 아닙니다.")
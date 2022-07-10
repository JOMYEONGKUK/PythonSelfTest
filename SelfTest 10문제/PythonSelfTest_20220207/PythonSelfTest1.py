# 문제 1
'''
사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
힌트-1 : islower() 함수는 문자의 소문자 여부를 판별합니다. 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다.
힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.
'''

Alphabet = input("문자를 입력해주세요: ")  # 알파벳 소문자 또는 대문자 입력


if(Alphabet.islower()):  # islower 함수로 모든 문자열이 소문자이면 참 소문자면 거짓
    print(Alphabet.upper())  # upper 소문자 입력시 대문자로 출력해줍니다.
else:
    print(Alphabet.lower())  # lower 대문자로 입력시 소문자로 출력해줍니다.
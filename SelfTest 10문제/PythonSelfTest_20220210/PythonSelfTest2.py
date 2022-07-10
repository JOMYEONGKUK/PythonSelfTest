# 문제 2
'''
매개변수로 문자열을 받고, 해당 문자열이 red면 apple을, yellow면 banana를,
green이면 melon을, 어떤 경우도 아닐 경우 I don't know를 리턴하는 함수를 정의하고,
사용하여 result변수에 결과를 할당하고 print해본다.
'''

# 함수의 정의
def color_a(color):
    if color == 'red':  # color가 red와 같으면
        return 'apple' # apple 반환
    elif color == 'yellow': # color가 yellow와 같으면
        return 'banana'    # banana 반환
    elif color == 'green':  #color가 green과 같으면
        return 'melon'      # melon 반환
    else:    # 그외 나머지 I don't know 출력
        return "I don't know"
    
# 함수의 호출
color_a('red')
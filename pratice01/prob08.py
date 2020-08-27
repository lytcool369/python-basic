# 문제8. 문자열을 입력 받아, 해당 문자열의 문자 순서를 뒤집어서 반환하는 함수 reverse(s)를 작성하세요.

input_str = input('입력> ')

def reverse(s):

    lst_str = []
    lst_str = list(s)
    lst_str.reverse()
    rev_str = ''.join(lst_str)

    return rev_str

print('결과> ', reverse(input_str))
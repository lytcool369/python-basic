import keyword

# 변수 이름은 문자, 숫자, _로 구성된다.
friend = 1
a = 1
my_name = '안대혁'
_yourName = '둘리'

# 에러 케이스
# friend$ = 1   --> 특수문자는 "_" 만 사용 가능
# a! = 2
# 1abc = 10     --> 숫자는 앞에 올수 없음
# def           --> keyword(예약어)는 변수 이름으로 사용할 수 없음

print(keyword.kwlist)

# 한글이름 변수 사용하기
가격1 = 2000
print(가격1)
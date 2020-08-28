# 생성
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

d2 = {}
print(d2, type(d2))

d3 = dict()
print(d3, type(d3))

d4 = dict(one=1, two=2, three=3, four=4, five=5)
print(d4, type(d4))

d5 = dict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
print(d5, type(d5))
print('')

# index 대신 key로 요소값(데이터)에 접근한다
d6 = {'basketball': '농구', 'baseball': '야구'}
print(d6['basketball'])

# 크기
print(len(d6))

# in, not in : key의 존재 여부
print('soccer' not in d6)
print('baseball' in d6)
print('')

# 다양한 타입의 key를 사용할 수 있다
d7 = {}
print(d7)
d7['twenty'] = 20   # str
d7[True] = 'treu'   # bool
d7[10] = 10           # int
print(d7)

# 키는 변경 불가능한 타입의 값을 사용해야 한다.
# d7[[1, 2, 3]] = 6
d7[(1, 2, 3)] = 6
print('')

print('================ 객체 함수 ================')
# keys()
k = d7.keys()
print(k, type(k))
for key in k:
    print(key, d7[key])
print('')

# values()
v = d7.values()
print(v, type(v))
for value in v:
    print(value)
print('')

# items()
items = d7.items()
print(items, type(items))
for item in items:
    print(item)
print('')

phones = {'마이콜': '000-0000-0000', '둘리': '111-1111-1111', '또치': '222-2222-2222'}
print(phones['둘리'])
print(phones.get('둘리'))

# print(phones['도우넛'])  -> 없는 키값을 검색하므로 에러 발생
# get() 객체 함수를 사용하면, 존재하지 않는 값일 경우 None을 반환받을 수 있다
v = phones.get('도우넛')
if v is None:
    print('도우넛 키를 가진 값은 없습니다.')
print('')

# setDefault()는 존재하지 않는 값일 경우, Deault 값이 저장된다.
v2 = phones.setdefault('둘리', '555-5555-5555')
print(v2)
v2 = phones.setdefault('도우넛', '555-5555-5555')
print(v2)
print(phones)
print('')

# pop() : 삭제와 동시에 값을 가져온다.
v3 = phones.pop('둘리')
print(v3)
print(phones)
print('')

# popitem() : 삭제와 동시에 키, 값을 가져온다.
item = phones.popitem()
print(item)
print(phones)
print('')

# clear
phones.clear()
print(phones)
print('')

# 조회
d8 = {'c': 3, 'a': 1, 'b': 2}

for key in d8:
    print(key, end=' ')
else:
    print('')

for key in d8.keys():
    print(key, end=' ')
else:
    print('')
print('')

# items()는 두개의 값을 가지고 있기 때문에,
# 두개의 변수로 값을 받아 출력할 경우 unpacking 되어 출력된다.
for key in d8.items():
    print(key)
for key, value in d8.items():
    print(key, value)


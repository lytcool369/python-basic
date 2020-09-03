import sys

# 가변 인수
print(1)
print('hello', ' ', 'world')

# sep 기본 인수값
x = 0.2
s = 'hello'
print(str(x) + ' ' + s)
print(x, s)
print(x, s, sep=' ')
print(x, s, sep=':')
print('')

print('=== end 기본 인수값 ===')
print('hello world')
print('!!!!!!!!!!!!!!!!!')
print('hello world', end='\n')
print('!!!!!!!!!!!!!!!!!')
print('hello world', end='')
print('!!!!!!!!!!!!!!!!!')
print('')

print('=== file 기본 인수값 ===')
print('output : hello world', file=sys.stdout)
print('error : hello world', file=sys.stderr)
print('')

f = open('hello.txt', 'w')
print(type(f))
print('hello world', file=f)
f.close()

# 참고
sys.stdout.write('hello world!!!!!!!!!')

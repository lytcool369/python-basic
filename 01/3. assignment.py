print("# 치환문")
a = 1
b = a + 1
print(a, b)
print("")

# 변수 할당값 오류"
# 1 + a = c     --> 연산 방향 오류

print("# 세미클론(;)으로 치환문을 구분할 수 있다.")
e = 3.5; f = 5.3
print(e, f)
print("")

print("# 여러 개를 한번에 치환할 수 있다.")
e, f = 3.5, 5.3
print(e, f)
print("")

print("# 같은 값을 여러 변수에 할당할 수 있다.")
# x = 30
# y = 30
# z = 30
x = y = z = 30
print(x, y, z)
print("")

print("# 동적 타이핑(실행 중에 변수의 타입을 결정한다)")
a = 1
print(type(a))
a = 'hello'
print(type(a))
print("")

print("# 확장 치환문")
a = 10
print("===== a = a + 10 =====")
a += 10
print(a)
print("===== a = a - 20 =====")
a -= 20
print(a)
print("")

print("# swap")
x = 10
y = 20
temp = 0
print('===== swap =====')
temp = x
x = y
y = temp
print(x, y)

import copy

# 레퍼런스 복사
a = 1
b = a

a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = x

print(x)
print(y)
print(x is y)
print('')

# copy : 복합 개체를 복사
# 얕은 복사(swallow copy)
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.copy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])
print('')


# 깊은 복사(deep copy)
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.deepcopy(x)

print(x is y)
print(x[0] is y[0])
print('')




# 깊은복사가 복합객체만을 생성하기 때문에
# 복합 객체가 한개만 있는 경우에는
# 얕은복사와 깊은복사는 차이가 없다.
a = ['hello', 'world']
b = copy.copy(a)

print(a)
print(b)
print(a is b)
print(a[0] is b[0])
print('')


a = ['hello', 'world']
b = copy.deepcopy(a)

print(a)
print(b)
print(a is b)
print(a[0] is b[0])
print('')
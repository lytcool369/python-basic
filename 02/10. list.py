# 생성
lst1 = []
lst2 = [1, True, 'python', 3.14, ['hello', 'world']]
print('')

# 인덱싱(sequence 타입 특징)
print('# 인덱싱(sequence 타입 특징)')
print(lst2[0], lst2[1], lst2[2], lst2[3], lst2[4])
print(lst2[-1], lst2[-2], lst2[-3], lst2[-4], lst2[-5])
print('')

# slicing
print('# slicing')
print(lst2[1:4])
print(lst2[:])
print(lst2[2:])
print(lst2[4::-1])
print(lst2[len(lst2)::-1])
print('')

# 반복(sequence 타입 특징)
lst3 = lst2 * 2
print(lst3)

# 연결(sequence 타입 특징)
lst4 = lst2 + [1, 2, 3]
print(lst4)

# 길이(sequence 타입 특징)
print(len(lst4))

# in, not in(sequence 타입 특징)
print(5 not in lst4)
print('python' not in lst4)

# 삭제(변경 가능한 객체)
del lst4[2]
print(lst4)
print('')

# 변경 가능한 객체(mutable)
lst5 = ['apple', 'banana', 10, 20]
print(lst5)
lst5[2] = lst5[2] + 90
print(lst5)
print('')

print('================ slicing을 이용 ================')
# 삭제(slicing을 이용)
print('# 삭제')
lst6 = [1, 12, 123, 1234]
lst6[1:3] = []
print(lst6)
print('')

# 삽입(slicing을 이용)
print('# 삽입')
lst7 = [1, 123, 1234, 12345]

## 중간 삽입
lst7[1:1] = [12]
print(lst7)

## 마지막 삽입
lst7[5:] = [123456, 1234567]
print(lst7)

## 처음 삽입
lst7[:0] = [0]
print(lst7)
print('')

# 치환(slicing을 이용)
print('# 치환')
lst8 = [1, 12, 123, 1234, 12345]
print(lst8)

lst8[0:2] = [10, 20]
print(lst8)

lst8[0:2] = [100]
print(lst8)

lst8[1:2] = [200]
print(lst8)

lst8[2:4] = [300, 400, 500, 600]
print(lst8)
print('')


print('================ 객체 함수 ================')
lst9 = [1, 3, 4]
print(lst9)

# 중간 삽입
lst9.insert(1, 2)
print(lst9)

# 마지막 삽입
lst9.append(5)
print(lst9)

# 처음 삽입
lst9.insert(0, 0)
print(lst9)

# reverse
lst9.reverse()
print(lst9)

# 삭제(값으로 동일안 요소를 찾아 삭제한다)
try:
    lst9.remove(3)
except ValueError as e:
    print('없는 요소를 삭제할 경우 예외 발생')

#확장
lst9.extend([-1, -2, -3, -4, -5])
print(lst9)

# stack
lst10 = []
lst10.append(10)    # push
lst10.append(20)    # push
lst10.append(30)    # push
print(lst10)
print(lst10.pop())  # pop
print(lst10.pop())  # pop
print(lst10)
print('')

# queue 로 사용해보기
lst11 = [1, 2]
lst11.append(3)
lst11.append(4)
lst11.append(5)
print(lst11)
print(lst11.pop(0)) #queue
print(lst11.pop(0)) #queue
print(lst11.pop(0)) #queue
print(lst11)

# sort
lst12 = [1, 5, 3, 9, 8, 7]
lst12.sort()
print(lst12)

lst13 = [10, 2, 33, 9, 8, 4, 11]
lst13.sort(key=str)
print(lst13)

# cf: sorted 전역함수
lst14 = [19, 46, 37, 28, 91, 55, 64]
lst15 = sorted(lst14)
print(lst15)

def f(i):
    return i % 10

lst16 = sorted(lst14, key=f, reverse=False)
print(lst16)
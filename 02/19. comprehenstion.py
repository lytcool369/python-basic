results = []

for num in [1, 2, 3, 4, 5, 6, 7, 8]:
    result = num * num
    results.append(result)
print(results)

results = [num * num for num in [1, 2, 3, 4, 5, 6, 7, 8]]
print(results)
print('')

# 문자열 리스트에서 길이가 2 이하인 문자열만 새로운 리스트로 출력
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
results = [s for s in strings if len(s) <= 2]
print(results)
print('')

# 1~100 사이의 수 중에 짝수 리스트 만들기
results = [n for n in range(1, 101) if n % 2 == 0]
print(results)

# 문자열 리스트에서 각각의 문자열의 길이를 담은 리스트 만들기
results = [len(s) for s in strings]
print(results)

# 1~100 사이의 수 중에 3, 6, 9일 경우,
results = [n for n in range(1, 101) if n % 10 == 3 or n % 10 == 6 or n % 10 == 9]
print(results)
print('')

# set comprehension
s = {s for s in strings if len(s) <= 2}
print(s)

# dict comprehenshion
d = {s: len(s) for s in strings}
print(d)


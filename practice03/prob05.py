# 문제5. 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.

ary = [5, 9, 3, 8, 60, 20, 1]

print('Before Sort')
print(ary)
print('')

for i in range(len(ary) - 1, 0, -1):
    for j in range(0, i):
        if (ary[j] > ary[j+1]):
            temp = ary[j]
            ary[j] = ary[j+1]
            ary[j+1] = temp
    print('{0}회 : {1}'.format(len(ary) - i, ary))

print('')
print('After Sort')
print(ary)
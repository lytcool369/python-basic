# 문제4. 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요. 1부터 99까지만 실행하세요.

for num in range(1, 100):
    find3 = str(num).count('3')
    find6 = str(num).count('6')
    find9 = str(num).count('9')
    sound = '짝'

    if (find3 > 0):
        print('{} {}'.format(num, sound * find3))
    elif (find6 > 0):
        print('{} {}'.format(num, sound * find6))
    elif (find9 > 0):
        print('{} {}'.format(num, sound * find9))
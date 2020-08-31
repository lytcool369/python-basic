# 문제5. 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

play = 0
numbers = []

try:
    play = int(input('합산할 정수의 개수 : '))
except ValueError as e:
    print('정수로 입력해 주세요')

for i in range(0, play):
    numbers.append(int(input()))

print('합 : ', sum(numbers))

def sum(numbers):
    result = 0

    for i in numbers:
        result += int(i)

    return result

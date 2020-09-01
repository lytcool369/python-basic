# 문제4. 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다. 프로그램은 정답 여부를 다시 출력합니다.
import random

dumy = []
count = 0
select = 0

dan1 = random.randint(1, 9)
dan2 = random.randint(1, 9)
point = random.randint(1, 9)
answer = dan1 * dan2

print('{} X {} = ?'.format(dan1, dan2))
print('')

while True:
    temp = random.randint(1, 81)

    # 초기 설정 및 정답 중복 제거
    if dumy == [] or temp != answer:
        dumy.append(temp)

    # 중복 제거된 더미답안이 일정량 이상일 경우
    if len(set(dumy)) == 8:
        temp_set = set(dumy)
        dumy = list(temp_set)
        break

for i in range(1, 10):
    if i == point:
        print(answer, end='\t\t')
        count = 1
    else:
        print(dumy[i - 1 - count], end='\t\t')

    if i % 3 == 0:
        print('')

select = int(input('answer : '))

if select == answer:
    print('정답')
else:
    print('틀림')
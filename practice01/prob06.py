# 문제6. 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권,
# 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전이
# 각 몇 개로 변환 되는지 작성하시오.

have = 67879
owon = 50000
won = 10000

for i in range(1, 11):
    if(i % 2 == 1):
        print('%d원 : %d개' % (owon, have // owon))
        have = have % owon
        owon = owon / 10
    else:
        print('%d원 : %d개' % (won, have // won))
        have = have % won
        won = won / 10
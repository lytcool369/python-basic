# # 문제3. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.

star = '*'

for i in range(1, 11):
    for j in range(0, i):
        print(star, end='')
    print('')


# for문 한개로 문제풀이
# for i in range(1, 11):
#     print(star * i)
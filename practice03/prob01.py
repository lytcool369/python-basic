# 문제1. 다음 세 개의 리스트가 있을 때, 3형식 문장을 모두 출력해 보세요

subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

for i in subs:
    for j in verbs:
        for k in objs:
            print('{} {} {}'.format(i, j, k))
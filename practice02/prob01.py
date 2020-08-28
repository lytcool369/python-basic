# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
# 추가로 디렉토리 경로명과 파일명을 분리하여 출력하세요.

s = '/usr/local/bin/python'

s_splt = s.split('/')
print(s_splt[1:])

s_splt = s.rsplit('/', 1)
prt = print(s_splt)
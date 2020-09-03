
# text mode가 default(text mode) : t(생략 가능)
f = open('test_t.txt', 'wt', encoding='utf-8')
w_sz = f.write('안녕하세요.\n파이썬입니다.')      # 한글:3byte, .(아스키코드):1byte, \n:2byte
f.close()
print(w_sz)     # 글자 수


# binary mode : b
f = open('test_b.txt', 'wb')
w_sz = f.write(bytes('안녕하세요.\n파이썬입니다.', 'utf-8'))
f.close()
print(w_sz)     # byte


# read test : text mode
f = open('test_t.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)


# read test : binary mode -> copy.py

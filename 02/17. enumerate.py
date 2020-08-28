# enumerate() 함수 사용하기

index = 0
for color in ['red', 'tellow', 'blue', 'black', 'gray']:
    print(index, color)
    index = index + 1
print('')

for index, color in enumerate(['red', 'tellow', 'blue', 'black', 'gray']):
    print(index, color)

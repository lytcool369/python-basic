# input test
import sys

input_value = input('price: ')
print(a, type(a))

if input_value.isdigit() is False:
    print('숫자를 입력하세요')
    sys.exit(0)

price = int(input_value)
print('가격', ':', price)
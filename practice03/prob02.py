# 문제2. range() 함수와 유사한 frange() 함수를 작성해 보세요.
# frange() 함수는 실수 리스트를 반환합니다.

def frange(val, base=0.0, step=0.1):
    f_list = []

    if(val > base and step > 0):
        while(base < val):
            f_list.append(base)
            base += step
    elif (val > base and step < 0):
        while (base < val):
            f_list.append(val)
            val += step
    elif(val < base):
        while (val < base):
            f_list.append(val)
            val += step

    return f_list

print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))
print(frange(5.0, 1.0, -0.5))
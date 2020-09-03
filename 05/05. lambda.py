import re


def f(x):
    r = x * x
    return r


for i in range(10):
    s = '{0}:{1}'.format(i, (lambda x: x * x)(i))
    print(s)

states = ['Alabama', ' Georgia!', 'Georgia', 'georgia', 'FIOrlda', 'south carolina', 'West virginia?']


# data ---> data1 ---> data2 ---> data3
#       f1         f2         f3
def clean_strings(strings, *funcs):
    results = []
    for s in strings:
        for f in funcs:
            s = f(s)
        results.append(s)
    return results


def strip(a):
    return str.strip(a)


states = clean_strings(states, str.strip, lambda x: re.sub('[?!#*&$@]', '', s))
print(states)

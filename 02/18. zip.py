# zip() 사용 예

seq1 = {'foo', 'bar', 'baz'}
seq2 = {'one', 'two', 'three'}

z = zip(seq1, seq2)
print(z, type(z))
for t in z:
    print(t)
print('')

z = zip(seq1, seq2)
for index, t in enumerate(z):
    print(index, t)
print('')

z = zip(seq1, seq2)
for a, b in z:
    print(a, b)
print('')
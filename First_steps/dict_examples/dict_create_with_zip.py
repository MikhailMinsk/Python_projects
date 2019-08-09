a = 'abc'
b = '123'
c = list(zip(a, b))
d = dict(c)
print(d)

print(dict(list(zip(a, b))))
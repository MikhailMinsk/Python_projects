"""
Дан произвольный текст. Напечатайте все имеющиеся в нем цифры,
определите их количество, сумму и найти максимальное.
"""

text = '12312 dawdaw 1231231adwd 6546 sefse12'
out = ''
sum_ = 0
for i in range(len(text)):
    if text[i].isdigit():
        out = out + text[i]
        sum_ = sum_ + int(text[i])
        continue

print(out)
out = list(str(out))
print(out)
print(len(out))
print(max(out))
print(sum_)

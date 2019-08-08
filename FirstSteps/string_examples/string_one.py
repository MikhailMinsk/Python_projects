s = "У лукоморья 123 дуб зеленый 456"

print(s.find('я'))
print(s.count('у'))

if len(s) > 4:
    print(s.lower())

if s.isalpha() is False:
    print(s.upper())

print(s.replace('У', 'О', ))

# file = open('D:\\Python_programs\\fedorov\\txt\\1.txt', 'r')
# content = file.read()
# print(content)
# file.close()
# print()
# print()

with open('D:\\Python_programs\\fedorov\\txt\\1.txt', 'r') as file:
    content = file.readlines()
print(content)
print()
print()
out = ''
for line in sorted(content):
    for word in line:
        print(sorted(word))
    print(line.strip())
    out += line.strip()
print()
print(out)
with open('D:\\Python_programs\\fedorov\\txt\\1_out.txt', 'w') as out_file:
    out_file.writelines(sorted(content))
print()
print()
with open('D:\\Python_programs\\fedorov\\txt\\1_out.txt', 'r') as file:
    content = file.readlines()
    print(content)

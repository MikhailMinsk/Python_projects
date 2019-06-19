"""
Отсортированное по алфавиту содержимое файла plan.txt поместите в файл sort_plan.txt.
"""

with open(r'G:\ProjectPithon\Fedorov\txt\2.txt', 'r') as file:
    content = file.readlines()

print(content)

with open('G:\\ProjectPithon\\Fedorov\\txt\\2_out.txt', 'w') as output_file:
    output_file.write('sorted 2 : \n')

f = sorted(content)
print(f)
for planet in reversed(content):
    print(planet.strip())

for planet in sorted(content):
    with open('G:\\ProjectPithon\\Fedorov\\txt\\2_out.txt', 'a') as output_file:
        output_file.writelines(planet)

with open('G:\\ProjectPithon\\Fedorov\\txt\\2.txt', 'r') as file:
    for line in file:
        print(line)
        print(len(line.strip()))


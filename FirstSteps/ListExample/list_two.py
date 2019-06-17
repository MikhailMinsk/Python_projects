List_ = [3, 'hello', 7, 4, 'привет', 4, 3, -1]

if 'привет' in List_:
    List_.remove('привет')
    print(List_)
else:
    List_.append('привет')  # L.insert(2,'привет') - добавит элемент на определенную позицию

if List_.count(4) > 1:
    List_.clear()  # аналог del L[:]
print(List_)

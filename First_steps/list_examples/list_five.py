"""Дан список числовых значений, насчитывающий N элементов.
Поменяйте местами первую и вторую половины списка."""

List_ = [i + 2 for i in range(10, 50, 6)]
print(List_)
print(len(List_))
if len(List_) % 2 == 0:
    A = [i for i in List_[0:int(len(List_) / 2)]]
    B = [i for i in List_[int(len(List_) / 2):int(len(List_))]]
    List_ = B + A
    print(List_)
else:
    A = [i for i in List_[0:int(len(List_) / 2 + 1)]]
    B = [i for i in List_[int(len(List_) / 2 + 1):int(len(List_))]]
    List_ = B + A
    print(List_)

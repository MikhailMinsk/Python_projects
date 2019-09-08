def func(arr):
    """
    The maximum sum subarray problem consists in finding the maximum sum of a contiguous
    subsequence in an array or list of integers:
    maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    # should be 6: [4, -1, 2, 1]
    Easy case is when the list is made up of only positive numbers and the maximum sum is
    the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
    Empty list is considered to have zero greatest sum. Note that the empty list or array is also
    a valid sublist/subarray.

    Задача о максимальной сумме подмассива состоит в том, чтобы найти максимальную сумму
    смежной подпоследовательности в массиве или списке целых чисел:
    maxSequence ([- 2, 1, -3, 4, -1, 2, 1, -5, 4])
     должно быть 6: [4, -1, 2, 1]
    Простой случай, когда список состоит только из положительных чисел, а максимальная сумма -
    это сумма всего массива. Если список состоит только из отрицательных чисел, вместо этого возвращается 0.
    Пустой список считается имеющим нулевую наибольшую сумму. Обратите внимание,
    что пустой список или массив также является допустимым подсписком / подмассивом.
    """
    if not arr or len([i for i in arr if i > 0]) == 0:
        return 0
    a = b = 0
    for number in arr:
        b = max(b + number, 0)
        a = max(a, b)
    return a

    # max,curr=0,0
    # for x in arr:
    #     curr+=x
    #     if curr<0:curr=0
    #     if curr>max:max=curr
    # return max

if __name__ == '__main__':
    print(func([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(func([-1, -2, -3, -123]))
    print(func([]))

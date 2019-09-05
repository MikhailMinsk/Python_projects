def func(recipe, available):
    """
    Write a function , which takes the recipe (object) and the available
    ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer).
    For simplicity there are no units for the amounts
    (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
    Ingredients that are not present in the objects, can be considered as 0.

    Напишите функцию , которая берет рецепт (объект) и доступные ингредиенты (также объект)
    и возвращает максимальное количество тортов, которые Пит может испечь (целое число).
    Для простоты не существует единиц для количеств
    (например, 1 фунт муки или 200 г сахара - это просто 1 или 200).
    Ингредиенты, которых нет в объектах, можно рассматривать как 0.
    """

    list_count = []
    for key in recipe.keys():
        if available.get(key) is None:
            return 0
        list_count.append(available[key] // recipe[key])
    return min(list_count)


if __name__ == '__main__':
    print(func({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
    print(func({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
               {"sugar": 500, "flour": 2000, "milk": 2000}))

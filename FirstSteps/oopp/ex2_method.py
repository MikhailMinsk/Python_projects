class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.heigth = height

    def calculate_area(self):
        return self.width * self.heigth

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = rectangle.new_square(5)
print(square.calculate_area())


# ____________________________________________________
class pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == 'pineapple':
            raise ValueError('No pineapples!')
        else:
            return True


ingredients = ['cheese', 'onions', 'spam']
if all(pizza.validate_topping(i) for i in ingredients):
    pizza = pizza(ingredients)

print('\n', pizza.toppings)

"""конечный вариант"""
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def per_info(self):
        print(self.name, 'is', self.age)

john=person('John', 22)
lucy=person('Lucy', 21)

'''
первоначальный выриант:
class person:
    pass

john=person()
john.name='john'
john.age=22

lucy=person()
lucy.name='Lucy'
lucy.age=21

print(john.name, 'is', john.age)
print(lucy.name, 'is', lucy.age)'''

'''
___________________________________________________
следующий вариант:
class person:
    def per_info(self):
        print(self.name, 'is', self.age)

john=person()
john.name='john'
john.age=22

lucy=person()
lucy.name='Lucy'
lucy.age=21

person.per_info(john) или john.per_info()
person.per_info(lucy) или lucy.per_info()'''
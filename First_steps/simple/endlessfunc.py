
def endless_func():
    print('I am endless')
    return endless_func()


endless_func()()()()()()()()()()

x = endless_func()
print(x, x == endless_func())


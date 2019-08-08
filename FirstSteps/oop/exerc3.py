class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


class E(B, C):
    pass


class F(C, D):
    pass


class G(F, E):
    pass


def main():
    for cls in [A, B, C, D, E, F, G]:
        print(cls.__name__ + ':', cls.mro())


if __name__ == '__main__':
    main()

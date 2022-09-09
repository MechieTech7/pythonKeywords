# def,from,import,as,yield
from math import sqrt as s


def squareroot(square):
    for i in square:
        a = s(int(i))
        yield a


square = ["4", "9", "16"]
generator = list(squareroot(square))
print(generator)



# with,return,non-local,global,if,else,elif,assert

x = int(input("enter number : "))
assert 0 < x < 15, 'Number should be greater than 0 and less than 15'


def func1():
    global y
    y = "Program"
    x = "Python"

    def func2():
        nonlocal x
        x = "language"
        func2()

    return x


if x > 10:
    print(func1())
elif x < 5:
    print(func1())
    print(y)
else:
    with open('output.txt', 'w') as f:
        f.write('Hi there!')
        print("Write details in file")

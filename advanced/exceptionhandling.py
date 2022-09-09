# try,except,finally,raise,del

a = 10
b = 0
try:
    c = a + b
    print(c)
    d = b / a
except ZeroDivisionError:
    raise
finally:
    print("This is the finally after try and except block")
    print(c)
    del c


# class,none,is

class Age:
    age = None

    def __init__(self, age):
        self.age = age


a = 10
b = a
person1 = Age(20)
person2 = Age(20)
print(a is b)
print(person1 is person2)
print("Age of Person1 : {}".format(person1.age))
print("Age of Person2 : {}".format(person2.age))

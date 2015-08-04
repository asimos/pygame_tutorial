class Person():

    def __init__(self, name):
        self.__name = name

    def getname(self):
        return self.__name

p = Person('Filip')
print p.getname()

# 2nd example


def func(x):
    return x+10


class Demo:
    def func(self, x):
        return func(x) + self.__value  # uses the function outside the class + the private value self.__value

    def __init__(self, value):
        """

        :rtype : float tpye
        """
        self.__value = value

demo = Demo(2)
result = demo.func(10)

print(result)

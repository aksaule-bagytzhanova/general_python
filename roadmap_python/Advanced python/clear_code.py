#прикрой свой з** интструкциями assert

def apply_discount(product, discount):
    price = int(product['price'] * (1.0- discount))
    assert 0 <= price <= product['price']
    return price

#with

with open('hello.txt', 'w') as f:
    f.write('privet, world')


f = open('hello.txt', 'w')
try:
    f.write('hi. world')
finally:
    f.close()


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedFile('hello.txt') as f:
    f.write('hiii')


from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('jijijij, world!')



class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -=1

    def print(self, text):
        print("    " * self.level + text)


#_ and __

class ExtendedTest():
    def __init__(self):
        super().__init__()
        self.foo = 'pere'
        self._bar = 'pere'
        self.__baz = 'pere'

t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
print(t2.__baz)


import this

#def functions


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

#lambda

add = lambda x, y: x+y
add(5,3)


(lambda x,y: x+y)(5,3)

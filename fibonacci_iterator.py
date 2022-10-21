# Based on Mark Pilgrim's "Dive into Python 3".
# toto jsou iterátory, mají __iter__

class PapayaWhip:
    pass

class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

fib1000 = Fib(1000)
print (fib1000)
print (fib1000.__class__)
print (fib1000.__doc__)

fib100 = Fib(100)
print (fib100)
print (fib100.__class__)
print (fib100.__doc__)

print(next(fib100))
print(next(fib100))
print(next(fib100))
print(next(fib100))
print()

myfib = Fib(10)
while True:
    try:
        print(next(myfib))
    except StopIteration:
        print("Finish")
        break
print()

myfib = Fib(10)
while True:
    try:
        print(next(myfib))
    except Exception as e:
        print(e.__class__)
        break
print()

input("Done. Enter = konec")

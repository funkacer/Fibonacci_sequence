#toto jsou iterátory, mají __iter__

class PapayaWhip:
    pass

class Fib:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
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

for f in fib1000:
    for ff in fib100:
        print (f, ff)

print("Done")
input("Enter = konec")

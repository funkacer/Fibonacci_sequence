# Based on Mark Pilgrim's "Dive into Python 3".
# toto jsou generátory == mají yield

def fib(max):
    a, b = 0, 1
    while a <= max:
        yield a
        a, b = b, a + b

for n in fib(1000):
    print(n, end = ' ')

print()

aaa = []
aaa = list(fib(1000))
print (aaa)
print()

for a in aaa:
    print (a)
print()

for i in range(len(aaa)):
    print (aaa[i])
print()

print(list(map(lambda x: x, fib(8))))
print()

input("Press enter to quit")

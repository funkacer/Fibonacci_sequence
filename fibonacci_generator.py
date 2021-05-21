#toto jsou generátory == mají yield

#iterátor count == itertools.count(start=0, step=1)
def count(max, start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    a = start
    while a <= max:
        yield a
        a += step

for n in count(100,50,5):
    print(n, end = ' ')

print()

aaa = []
aaa = list(count(100,50,5))
print (aaa)
print()
for a in aaa:
    print (a)
print()
for i in range(len(aaa)):
    print (aaa[i])
    
'''
import itertools
itertools.count(start=0, step=1)
'''

print ("\n")

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

print(list(map(lambda x: x, fib(10))))

input("Press enter to quit")

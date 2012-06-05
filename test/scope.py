#scope

x= 1
scope = vars()
print scope['x']

def run():
    s = vars()
    x = 2
    print "local x is %d" % x
    print "global x is %d" % globals()['x']
    print s

run()
print "x is %d" % x

def factorial(n):
    if (n > 1):
        return n*factorial(n-1)
    return n

f3 = factorial(3)

print f3
print factorial(4)
print factorial(5)
print factorial(6)
print factorial(7)
print factorial(8)
f10 = factorial(10)
print f10
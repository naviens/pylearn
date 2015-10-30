__author__ = 'naveen'

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def apply(func,x,y):
    return func(x,y)

print apply(add,10,20)


def outer():
    def inner():
        print "at inner"
    return inner


osm = outer()
osm()



def outer():
    x = 1
    def inner():
        print x
    return inner


osm = outer()
osm()

# Function closures

def outer(x):
    def inner():
        print x
    return inner


osm = outer(1)
osm()

osm1 = outer(2)
osm1()


# Decorators


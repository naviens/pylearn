__author__ = 'naveen'

# Function without
def fib1():
    a, b = 0, 1
    for i in range(10):
        print b,
        a, b = b, a + b


#Function with argument
def fib2(n):
    a, b = 0, 1
    for i in range(n):
        print b,
        a, b = b, a + b


#Function with argument and with return list
def fib3(n):
    a, b = 0, 1
    output = []
    for i in range(n):
        output.append(b)
        a, b = b, a + b
    return output


fib1()
print
fib2(10)
print
print fib3(10)
print fib1
print fib2(0)



#required arguements
def func_2(arg1):
    print arg1 + 'single string'


#required plus optional arguements
def func_3(arg1, arg2='indiA'):
    print arg1 + "---" + arg2 + 'default'


#required plus optional plus variable
def func_4(arg1, arg2='indiaA', *arg3):
    print arg1 + "---" + arg2 + arg3[0] + arg3[1]


#required variable keyword arguements
def func_5(**arg4):
    print arg4['key1']
    print arg4['key2']
    print arg4['key3']
    print arg4


def func_6(*args, **wargs):
    print args
    print wargs


func_2("signle ")

func_3("senthil")
func_3('senthil', 'kumar')

func_4('senthil', 'ka', 'key1', 'key2')
func_4('senthil', 'ka', 'key1', 'key2')

func_5(key1='senthil', key2='arun', key3='arun senthil', key4='Karthikeyan')

print 'variable args'
func_6(1, 2, 3, 4, 5, k1=2, k2=3)


# Anonymous Functions

# Declared using lambda keyword
# single line functions
# lambda [arg1,arg2,....argn] : expression

sum = lambda a, b: a + b

print sum(10, 20)

# Variables scope
# Global Variables
# Local Variables

total = 0  # This is global variable.
# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    # global total
    total = arg1 + arg2  # Here total is local variable.
    print "Inside the function local total : ", total
    return total

# Now you can call sum function
sum(10, 20)
print "Outside the function global total : ", total

__author__ = 'naveen'


# Fibonacci series
a, b = 0, 1
while b < 100:
    print b
    a, b = b, a + b


# While with else statements
print "Else block will be executed once the condition become false"

count = 0

while count < 4:
    print count
    count += 1
else:
    print "Count is > 4"
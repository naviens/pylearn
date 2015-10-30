__author__ = 'naveen'
# Arithmetic Operators

a = 20
b = 10

print "Arithmetic Operators"
# + (plus)
print a + b

# - (minus)
print a - b

# * (multiply)
print a * b

# / (division)
print a / b

# % (modulo)
print a % b

# ** (Exponent)
print a ** b

# // (Floor)
print a // b

print "Comparison Operators"
# == (equal to )
print a == b

# != (not equal to)
print a != b

# > (greater)
print a > b

# < (lesser)
print a < b

# >= (greater equalto)
print a >= b

# <= (less equalto)
print a <= b

print "Logical Operators"

t = a > b
f = b > a

# and (and)
print t and f

# or (or)
print t or f

# not (not)
print not t

print "Assignment Operators"

# +=
a += b
print a

# -=
a -= b
print a

# *=
a *= b
print a

# /=
a /= b
print a

# %=
a %= b
print a

# **=
a **= b
print a

# //=
a //= b
print a

print "Bitwise Operators"

# Bits that are set on both a and b
print a & b

# Bits that are set on a or b
print a | b

#Bits that are set on either a or b , not on both
print a ^ b

#Bits that are set a are not set viceversa
print ~b

#Shifts Bits of a by 1 step left
print a << 1

#Shifts Bits of a by 1 step right
print a >> 1

print "Conditional Operators"

print 'true' if True else 'false'

print 'true' if False else 'false'


# Example
if False:
    print '1'

else:
    print '2'
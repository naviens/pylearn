__author__ = 'naveen'

tuple1 = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')

print tuple1
print tuple1[0]
print tuple1[0:2]
print tuple1[0:]
print tuple1[:2]
print tuple1[:-1]

# updating tuple will throw error ie tuples are immutable
# tuple1[5]='saturday'

tuple2 = ('saturday', 'sunday')
print tuple1 + tuple2

# delete tuple
del tuple1
# print tuple1


# Swap Values
a, b = 10, 100

a, b = b, a

print a
print b

# Built in functions

# cmp(tuple1, tuple2)
# len(tuple)
# max(tuple)
# min(tuple)
# tuple(seq)

# Packing
t2 = "A", "B"
t1 = 1, 2

t3 = t1 + t2
print t3

# Unpacking
w, x, y, z = t3
print z
print y
print x
print w

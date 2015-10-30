__author__ = 'naveen'

# Sets
# unordered collection of immutable objects
# Doesnt allow duplicate values

a = set()

a = {1, 2, 3, 4, 2, 4}

print a

a.add(10)

print a

# Set as immutable object is frozen set

b = frozenset(a)
# this will show error
# b.add(10)

# Examples

mySet = {False, 4.5, 3, 6, 'cat'}
yourSet = {99, 3, 100}

print "Union"
print mySet.union(yourSet)

print "Or"
print mySet | yourSet

print "Intersection"
print mySet.intersection(yourSet)

print "And"
print mySet & yourSet

print "difference"
print mySet.difference(yourSet)

print "Minus"
print mySet - yourSet

print "subset"
print {3, 100}.issubset(yourSet)

print "<="
print {3, 100} <= yourSet

print "Add Method"
mySet.add("house")
print mySet

print "Remove Method"
mySet.remove(4.5)
print mySet

print "Pop Method"
mySet.pop()
print mySet

print "Clear Method"
mySet.clear()
print mySet
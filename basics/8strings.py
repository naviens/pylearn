# -*- coding: iso-8859-15 -*-
name = "welcome india"

print name
print name.strip() + ' sam'
print name[8]
print name[1:]
print name[:5]
print 'this is slice ' + name[:5]
print name[8:15]
print name[-5:]
print name[:-5]
print 'length is ' + str(len(name))

name2 = 'india'
print name2[0]
print name2[4]
print name2[-1]

# unicode

name3 = u"naveen"
print name3
print type(name3)
print str(name3)
print type(str(name3))
name4 = u"äöü"
print name4.encode('utf-8')

# String operators

a = "hello"

print a + a
print a * 2
print 'h' in a
print 'h' not in a

# %

print "Hello i am %d old from %s" % (20, "india")

print "Hello i am {0} old from {1}".format(20, "india")

itemdict = {"item": "banana", "cost": 24}

print("The %(item)s costs %(cost)7.1f cents" % itemdict)

a = """Triple quotes
        string """

print a

# Escape Characters

# \s, \t,\b

# some string functions
a = "welcome to my india "
print a.lower()
print a.upper()
print a.strip()
print a.split(" ")
print a.isupper()
print a.islower()
print a.replace('y', 'Y')

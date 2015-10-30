__author__ = 'naveen'

words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)


# Insert items
for w in words[:]:
    print w, len(w)
    if len(w) > 6:
        words.insert(0, w)
print words


#Range

print range(10)
print range(5, 10)

for i in range(len(words)):
    print i, words[i]


# for loop with else statement
print "Else part is executed when loop has exhausted iterating the list. "

for i in range(10):
    print i
else:
    print "i am for loop else err "


# without exhaust

for i in range(10):
    print i
    # Break statement
    break
else:
    print "i am for loop else "


# Nested Loops

# Continue Statement

# pass statement

if 20 > 10:
    pass

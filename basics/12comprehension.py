__author__ = 'naveen'

# List comprehension

# Multiples of 2

s = [x * 2 for x in range(10)]

print s


# Dict Comprehension
word = 'google'

print {item: word.count(item) for item in word}


def countChar(word):
    return dict((item, word.count(item)) for item in set(word))


print countChar('google')

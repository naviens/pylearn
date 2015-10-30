__author__ = 'naveen'

mydict = {'suresh': 24, 'tamil': 22, 'sunil': 32, 'kumar': 27}

# Accessing Values

print mydict['suresh']


# Updating Dict

mydict['suresh'] = 50  # updating old values

mydict['ram'] = 40  # adding new values

print mydict

# delete dict values

del mydict['tamil']  # deletes tamil key in dict

mydict.clear()  # clears the entire dict

del mydict  # delete dict itself


# Built in methods

# cmp(dict1, dict2)
# len(dict)
# str(dict)
# type(variable)
# dict.clear()
# dict.copy()
# dict.fromkeys()
# dict.get(key, default=None)
# dict.has_key(key)
# dict.items()
# dict.keys()
# dict.update(dict2)
# dict.values()

list1 = ['one', 'two', 'three']
print list1
print list1[0]
print list1[0:2]
print list1[0:]
print list1[:2]
print list1[:-1]

# Assignment
list1[3:5] = [10, 20]
print list1

#Replace
list1[3:5] = [100, 200]
print list1

#Remove
list1[3:5] = []
print list1

#copy Insert
list1[:0] = list1
print list1

#Clear
print len(list1)
list1[:] = []
print list1

#update
list2 = [1, 2, 3, 4]
list2[1] = "Updated"
print list2

#Delete

print list2
del list2[2]
print list2

#Length
print len([1, 2, 3])
#Concatenate
print [1, 2, 3] + [4, 5, 6]
#Repeat
print ['Hi!'] * 4
#Search
print 3 in [1, 2, 3]
#iterate
for x in [1, 2, 3]: print x,

#list methods
# cmp(list1, list2)
# len(list)
# max(list)
# min(list)
# list(seq) - type conversion
# list.append(obj)
# list.count(obj)
# list.extend(seq)
# list.index(obj)
# list.insert(index, obj)
# list.pop(obj=list[-1])
# list.remove(obj)
# list.reverse()
# list.sort([func])



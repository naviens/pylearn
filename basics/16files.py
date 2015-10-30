__author__ = 'naveen'
import os

# Files
# Syntax - file Object = open(file_name, [access_mode], [buffering])
# access_modes - r,rb,r+,rb+,w,wb,w+,wb+,a,ab,a+,ab+,

# Open a file
fo = open("foo.txt", "w+")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace


# Writing to file

fo.write("hello Python")
# CLose the file
fo.close()

# reading from file
foor = open("foo.txt", "r+")

strs = foor.read(10)
print strs

# Renaming the files

os.rename("foo.txt", "foo1.txt")

# Remove the files
os.remove("foo1.txt")


# Directories in python

# Create dir
os.mkdir("MYPYTHON")

# Change Dir
os.chdir("MYPYTHON")
# get Current Dir
print os.getcwd()
os.mkdir("MYPYTHON1")

# Delete dir

os.rmdir("MYPYTHON1")

os.chdir("../")
# get Current Dir
print os.getcwd()
os.rmdir("MYPYTHON")
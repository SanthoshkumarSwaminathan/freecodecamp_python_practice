my_str = "Hello World"

print(my_str[0])
print(my_str[6])
print(my_str[-1])


#String slicing lets you extract a portion of a string or work with only a specific part of it. Here's the basic syntax:

#string[start:stop]

print(my_str[1:4])

#Note that the stop index is non-inclusive, so [1:4] just extracted the characters from index 1, and up to,
#but not including, the character at index 4.

#You can also omit the start and stop indices, and Python will default to 0 or the end of the string, respectively.
#For example,
#here's what happens if you omit the start index:

print(my_str[:5])
print(my_str[:8])

#This extracts everything from index 0 up to (but not including),
#the character at index 7. And here's what happens if you omit the stop index:

print(my_str[3:])

#This extracts everything from the character at index 3 until the end of the string.


#You can also omit both the start and stop indices, which will extract the whole string:

print(my_str[:])

#Apart from the start and stop indices,
#  there's also an optional step parameter,
#  which is used to specify the increment between each index in the slice.

#Here's the syntax for that:

#string[start:stop:step]

#In the example below, 
# the slicing starts at index 0, 
# stops before 11, 
# and extracts every second character:

print(my_str[0:11:2])

#A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, 
# and leaving start and stop blank:

print(my_str[::-1])
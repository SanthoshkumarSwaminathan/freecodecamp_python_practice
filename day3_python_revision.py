my_str_1 = "Hello"
my_str_2 = "World"

str_plus_str = my_str_1+' '+my_str_2
str_plus_str_without_space = my_str_1 + my_str_2
print(str_plus_str)
print(str_plus_str_without_space)

# TypeError

'''
name = 'santhosh'
age = 15

name_and_age = name + age
print(name_and_age)

'''

# this happens because python does not automatically convert other data types like integers into strings when you concatenate them. python requires all elements to be strings before it can concatenate them. to fix that, you can convert the number into a string with the built-in str() fucntion, which returns the string reqpresentation of the given object withotut modifying the orignal object.

name = 'Santhosh Kumar S'
age = 25

name_and_age = name + ' ' + str(age)
print(name_and_age) 


# you can also use the augmented assignment operator for concatenation. this is represented by a plus and equals sign (+=), and performs both concatenation and assignment in one step.

name_and_age=name
name_and_age+=str(age)
print(name_and_age)

# The process of inserting variables and experssions into a string is called string string interpolation. python has a category of string called f-strings (short for formatted string literals), which allows you to handle interpolation with a compact and readable syntax.

# F-strings start with f (either lowercase or uppercase) before the quotes, and allow 

name_and_age = f"My name is {name} and i am {age} years old"
print(name_and_age)

num1 = 24
num2 = 1

print(F"Number one is {num1} and number two is {num2} the total of these number is {num1+num2}")

# Note how you don't need to covert non-string types with the str() function. In the example above, the values of the age, num1, and num2 variables is converted under the hood into a string during the interpolation process.

# What is string slicing and how does it work /

# In a previous lesson you learned how each charcters in a string can be identified by it's index (starting from zero), and accessed using the bracket notation:

my_str = "Hello world"

print(my_str[0])
print(my_str[6])
print(my_str[-1])

# String slicing let's you extract a portion of a string or work with only a specific part of it.

# string[start:stop]

# if you want to extract characters from a certain index to another, you just separate the start and stop indices with a colon;

print(my_str[0:5])
print(my_str[1:4])

#Note that the stop index is non-inclusive,so [1:4] just extracted the characters from index 1, and up to, but not including, the chracter at index 4

#You can also omit the start and stop indices, and python will defailt to 0 or the end of the string, respectively.For example, here's what happens if you omit the start index:

my_str = 'hello world'
print(my_str[:10])

#This extracts everything from index 0 upto (but not including), the character at index 10.And here's what happends if you omit the stop index:

print(my_str[6:])

#This extracts everything from the chracter at index 6 until the end fo the string.

#Note that slicing a string does not modify the original string:

print(my_str[8:])
print(my_str)

#you can also omit both the start and stop indices, which will extract the whole string:

print(my_str[:]) 

#Apart from the start and stop indices, there's also an optional step parameter, which is used to specify the increment between each index in the slice.

# here is the syntax for that

# string[start:stop:step]

# In the example below, the slicing starts at index 0, stops before 11, and extracts every second character:

print(my_str[0:11:2])

# A helpful trick you can do with the step parameter is to reverse a string by setting step to -1, and leaving the start and stop blank:

my_str = "Hello World"
print(my_str[::-1])

# What Are Some Common String Methods?

#Python provides a number of built-in methods that make working with strings a breeze. They include, but are not limited to, the following:
# ---> upper(): Returns a new string with all characters converted to uppercase.

print(my_str)  # Hello World

uppercase_my_str = my_str.upper()
print(uppercase_my_str)

# ---> lower(): Returns a new string with all characters converted to lowercase.

print(my_str)

lowercase_my_str = my_str.lower()
print(lowercase_my_str)

#---> strip(): Returns a new string with the specified leading and trailing chracters removed. if no argument is passed it removes leading and trailng whitespace.

my_str = '  hello world   '
print(my_str)
trimmed_my_str = my_str.strip()
print(trimmed_my_str)

my_str = "HHHhello H World hHHHH"

trimmed_my_str = my_str.strip("H")
print(trimmed_my_str)

#---> replace(old,new): Returns a new string with all occurences of old replaced by new.

my_str = "Hello World"
replaced_my_str = my_str.replace("Hello", "Hi")
print(replaced_my_str)

#---> split(separator): Splits a string on a specified separator into a list of strings. if no seprator is specified,it splits on whitespace.

my_str = 'hello world'

split_words = my_str.split()
print(split_words)

#---> join(iterable): Joind elements of an iterable into a string with a separator.

my_list = ['hello', 'I am santhosh']

joined_my_str = ' '.join(my_list)
print(joined_my_str)

#---> startwith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

starts_with_hello = my_str.startswith("hello")
print(starts_with_hello)

#---> endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.


ends_with_the_world = my_str.endswith("world")
print(ends_with_the_world)

#---> find(substring): returns the index of the first occurence of the substring, or -1 if it doesn't find one.

world_index = my_str.find("r")
print(world_index)

#---> count(substring): Returns the number of times a substring appears in a string.

my_str = 'hello world'
o_count = my_str.count("o")
print(o_count)
l_count = my_str.count("l")
print(l_count)

#---> capitalize(): Returns a new string with the first chracter captilized and the other characters lowercased.

my_str = 'heLlo woRld'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)

#---> isupper(): Returns True if all letters in the string are uppercase and False if not.

my_str="HELLO WORLD"
is_all_uppercase = my_str.isupper()
print(is_all_uppercase)

my_str="hello world"
is_all_uppercase = my_str.isupper()
print(is_all_uppercase)

#---> islower(): Returns True if all letters in the string are lowercase and False if not.

is_all_lowercase = my_str.islower()
print(is_all_lowercase)

#---> title(): Returns a new string with the first letter of each word capitalized.

my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)
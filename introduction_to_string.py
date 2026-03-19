#What Are String Concatenation and String Interpolation?

# string concatenation to combine two string (+) sign can be used


my_str_1 = 'Hello'
my_str_2 = 'World'

str_plus_str = my_str_1+" "+my_str_2
print(str_plus_str)

#TypeError

name = "Santhosh Kumar"
age = 25

#name_and_age = name + age
#print(name_and_age)

# this will give this error TypeError: can only concatenate str (not "int") to str 

'''
This happens because Python does not automatically convert other 
data types like integers into strings when you concatenate them. 
Python requires all elements to be strings before it can concatenate them. 
To fix that, you can convert the number into a string with the built-in str() function, 
which returns the string representation of the given object without modifying the original object:'''

name_and_age= name + str(age)
print(name_and_age)

# You can also use the augmented assignment 
# operator for concatenation. 
# This is represented by a plus and equals sign (+=), 
# and performs both concatenation and assignment in one step

name_and_age = name
name_and_age +=str (age)
print(name_and_age)

# The process of inserting variables and expressions into a string is called string interpolation. 
# Python has a category of string called f-strings (short for formatted string literals), 
# which allows you to handle interpolation with a compact and readable syntax.

# F-strings start with f (either lowercase or uppercase) before the quotes, 
# and allow you to embed variables or expressions inside replacement fields indicated by curly braces ({}). 

name_and_age = f"My name is {name} and I am {age} years old"
print(name_and_age)\

num1=23
num2=34

print(f"sum of {num1} and {num2} is {num1+num2}")

# Note how you don't need to convert non-string types with the str() function. 
# In the example above, 
# the value of the age, 
# num1, 
# and num2 variables is converted under the hood into a string during the interpolation process.


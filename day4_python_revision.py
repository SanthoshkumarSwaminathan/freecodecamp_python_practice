# How Do you work with integers and floating point numbers?

#Integers and floats are the primary numeric data types in python. With them, you can store numeric data and perform mathematical operations.

#Let's look at what integers and floats are, how to perform arithmetic calculations with them, and at several methods python provides for working with both.

#Integers are whole numbers without decimal points, either positive or negative

my_int_1 = 34
my_int_2 = -3


print(my_int_1)
print(type(my_int_1))
print(type(my_int_2))

#here's how to perform an addition operation with integers:

my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2

print("Integer Addition:",sum_ints)

#here's how to perform a subtraction with integers:

#subtraction
diff_ints = my_int_1 - my_int_2
print("Integer subtraction : ",diff_ints)

#Here's how to perform a multiplication operation with integers;

#Multiplication 
product_ints=my_int_1*my_int_2
print("Integer Multiplicaton : ",product_ints)

#And here's how to perform a division operation with integers:

# Division

div_ints = my_int_1/my_int_2
print("Division : ",div_ints)

#Floats are positive or negative numbers with decimal points, like 3.14, -0.5 or 0.0

my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1))
print(type(my_float_2))

#Here's an addition operation with floats

my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1+my_float_2
print('Float Addition:', float_addition)

#here's a subtraction operation with floats:

my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2-my_float_1
print("Float Subtraction : ",float_subtraction)

#Here's a multiplication operation with floats:

float_multiplication = my_float_2 * my_float_1
print('Float Multiplicaton : ',float_multiplication)

#And here's a division operation with floats:

float_division = my_float_2/my_float_1
print("Float Division:", float_division)

#If you add an integer and a float, the result is automatically converted to a float;

my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float)
print(type(sum_int_and_float))

#This is true for other basic arithmetic operations, too, like subtraction, multiplication, and division.If you mix integers and floats, Python will return a float as the result.

#you can also perform more complex arithmetic calculations such as getting the remainder of two numbers with the modulo operator,floor division,and exponentiation with both integers and floats.

#The modulo operator (%) returns the remainder when the value on the left is divided by the value on the right:

my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints)
print('Float Modulo:', mod_floats)

#Floor division divides two numbers and returns the greatest integer less than or equall to the result. This is done with the double forward slash operator(//):

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integers Floor Division:', floor_div_ints)
print('Float Floor Division:', floor_div_floats)

#Exponentiation raises a number to the power of another, and is done with the double asterisk operator(**):

my_int_1 = 4
my_int_2 = 3

my_float_1 = 5.4
my_float_2 = 5.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation : ', exp_ints)
print('Float Exponentiation : ', exp_floats)

#Sometimes, you might notice that the result of an operation involving floats has more decimal digits than expected.For example,the sum 0.1 + 0.2 equals 0.30000000000000004 instead of 0.3

#This happens beacuse numbers are stored in binary format, and some fractions cannot be respresented exactly in binary. As a result,they are stored as finite approximations, in the same way the fraction 1/3 cannot be represented with a finite number of digits in decimal and is truncated after a certain number of its infinite digits(0.33333...)

#This leads to small rounding errors.

#python also provides built-in functions for converting either numeric data or strings into into integers or floats.

#The float() function returns a floating-point number constructed from the given number:

my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)
print(type(my_float_1))

#The int() function returns an integer constructed from the given number:

my_float = 12.923
my_int = int(my_float)

print(my_int)
print(type(my_int))

#Also, you can use the same built-in functions to convert a string into either a float or integer:

my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))
print(converted_float, type(converted_float))

#Here are some methods python provides working with integers and floats.

#---> round() : Rounds a number to the specified number of decimal places.By default this function rounds to the nearest integer, and returns a whole number with on decimal places:

my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2,1)

print(rounded_int_1)
print(rounded_int_2)

#---> abs() : returns the absolute value of a number,

num = -12
absolute_value = abs(num)
print(absolute_value)

#---> pow(): raises a number to the power of another or performs modular exponentiation.

result1=pow(2,3) #Equivalent to 2**3
print(result1)

result2=pow(2,3,5) # (2**3)%5
print(result2)
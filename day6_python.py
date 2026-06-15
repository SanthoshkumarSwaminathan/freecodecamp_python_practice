#How DO Conditonal Statement and Logical Operators Work

# Conditional statements, or conditionals, let you control the flow of your program based on whether certain condtions are true or false.

#But before we get into all that, let's go over the basic building blocks of condtional statements, starting with comparison operators. Comparison operators are operators that let you compare two or more values, and return a boolean value.

#In a previsous lesson, you learned that booleans are one of the data types in python, and can only be True or False.

#Here's a table with the comparison operators in python:



# Operator	Name	                    Description

# ==	    Equal	                    Checks if two values are equal
# !=	    Not equal	                Checks if two values are not equal
# >	        Greater than	            Checks if the value on the left is greater than the value on the right
# <	        Less than	                Checks if the value on the left is less than the value on the right
# >=	    Greater than or equal	    Checks if the value on the left is greater than or equal to the value on the right
# <=	    Less than or equal	        Checks if the value on the left is less than or equal to the value on the right

# Here are some of the expressions that evaluate to True or False:

print(1 > 4)
print(3 < 5)
print(1 == 2)
print(3 == 3)
print(1 != 2)
print(1 >= 2)
print(1 <= 3)

#These operators can be used in conditionsals to compare values and run certain code base on whether the condtional evaluates to True or False.

#In Python, the most basic condtional is the if statement. Here's the basic syntax:

# if condition:
#     pass

# if statements starts with th if keyword.
# condition is a an expression that evaluates to True or False, followed by a colon(:).
# The body of the if statement constitues a code block, which is a group of statements that belong together.In python, the level of indentation is what defines a code block.

#In the example above, the body of the if statement contains a pass statement. when a pass statement is executed, nothing happens. This is a special keyword that can be used as a placeholder for future code and it is useful when empty code blocks are not allowed.

#The code within the body of the if statement runs only when the condtion evaluates to True. 

age = 18

if age >= 18:
    print('You are an adult')

#Notice the indentation before print('You are an adult). while other programming languages use chracters like curly braces to define code blocks, and just use indentation for readability, in python, code blocks are determined by indentation.

#The following code would raise an IndentationError, which is python's way to signal that indentation is required at a ceratain point of the code:

#age = 18

#if age >= 18:
#print('you are an adult')

# Though you can use any number of spaces (as long as you are consistent) to determine each level of indentation, the python sytle guide recommends using four spaces.

# Blocks are also found in loops and functions, which you'll learn about in future lessons.
 
# Going back to our examle, if age is anything less than 18, nothing is printed in the terminal:

age = 12

if age >=18:
    print('You are an adult') 

#But what if you also want to print something if age is less than 18? That's where the else clause comes in. The else clause runs when the if condtion is false. here's the syntax for an if....else statement:

'''

if condition:
    pass # code to execute if condtion is True
else:
    pass # code to execute if condtion is False
    
'''

#For example;

age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult')

#Note that you cannot place any statements between the if block and the else clause. The following code would raise a SyntaxError:

'''
age=12

if age>18:
    print("You are an adult")
print('Almost there!')
else: # SyntaxError: invalid syntax
    print('You are not an adult yet')
'''

#There might be situations in which you want to account for multiple conditions. To do that python, lets you extend your if statement with the elif(else if) keyword.

'''

if  condition1:
    pass #Code to execute if condtion1 is True.
elif condition2: 
    pass #Code to execute if condtiio1 flase and condition2 is True
else :
    pass #Code to execute if all condtions are False

'''

#For example:

age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('you are a child')

# Note that you can use as many elif clauses as you want:

age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are an young adult')
elif age >= 12:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant')

#Now that you understand how comparison operators and conditional statements work in python, you can start writing programs that make decisions based on logic and input. Whether you're comparing values or branching through multiple condtions, these tools are the foundation to writig flexible, responsive code.

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# What Are Truthy and Falsy Values, and How Do Boolean Operators and Short-Circuiting Work?
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# In the previous lesson, you learned how to use comparison operators and condtional statements to control the flow of yours programs.

# While those are very powerful, you will often run into situations where you need to compare multiple values at once. This can lead to nested condtional statements, for example:

is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote')
else:
    print('You are not eligible to vote')

# The above example will first check if is_citizen is True. If so, it will then go to the nested if statement and check if age is greater than or equal to 18. Since age is greater than or equal to 18, the message printed to the terminal will be You are eligible to vote. If is_citizen were False, then the message printed to the terminal would have been You are not eligible to vote.

# If you are working with more complex conditional statements, then you can use Python’s and, or, and not operators.

# But before we dive into those operators, let's take a look at what thruthy and falsy values are.

# In Python, every value has an inherent boolean value, or a built-in sense of whether it should be treated as True or False in a logical context. Many values are considered truthy, that is, they evaluate to True in a logical context. Others are falsy, meaning they evaluate to False.

'''
Here are a few falsy values:

None
False
Integer 0
Float 0.0
Empty strings ""

Other values like non-zero numbers, and non-empty strings are truthy.

If you want to check whether a value is truthy or falsy, you can use the built-in bool() function. It explicitly converts a value to its boolean equivalent and returns True for truthy values and False for falsy values. Here are a few examples:
'''

print(bool(False))
print(bool(0.0))
print(bool(0))
print(bool(""))
print(bool(None))

print("Now true values")

print(bool(True))
print(bool(1))
print(bool('Hello hi'))
print(bool(0.1))
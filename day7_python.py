# continuation of What Are Truthy and Falsy Values, and How Do Boolean Operators and Short-Circuiting Work?

# There are three boolean operators in python: and, or ,and not.

# Let's first take a look at the and operator.

# The and operator takes two operands and returns the first operand if it is falsy, otherwise, it returns the second operand. Both operands must be truthy for an expression to result in a truthy value.

is_citizen = True
age = 25

print(is_citizen and age)

# In the above example, the number 25 is printed to the terminal because the and operator will evaluate the second operand if the first operand is True the and operatoris known as a short-circuit means python checks values from left to right and stops as soon as it determines the final result.

# You'll often use and and within if statements to check if multiple condtions are met.  here's how you can refactoi the earlier exampler at use the and opertory insted of nested if statements

is_citizen = True
age=25

if is_citizen and age >=18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

#In the example above, is_citizen is True, and age>=18 evaluaes to True.Since both operands of the and operator are truthy,the condtion is_citizen and age >= 18 evaluates to True, and the print call in the if block is executed.

#Now let's take a look at the or operator. This operator returns the first operand if it is truthy, otherwise, it returns the second operand. An or expression results in a truthy value if at least one operand is truthy. The or operator is also known as a short-circuit operator. Here is an example:

age = 19
is_employed = False

print(age or is_employed)

# The following code will print the number 19 because the first operand age is truthy.

# If you need to check if one or more expressions is True, then you can use the or operator in an condtional like this:

age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount')
else:
    print('You are not eligible for a student discount')

#In this case, age < 18 is False, but is_student is True. Since at least one condition is true, the entire or expression evaluates to True, and the discount message in the if block is printed.

# The last operator we will look at is the not operator which takes a single operand and inverts its boolean value. It converts truthy values to False and falsy values to True. Unlike the previous operators we looked at, not always returns True or False.

#Here are a few examples:

print(not '')
print(not 'Hello')
print(not 0)
print(not 1)
print(not False)
print(not True)

#It is common to use the not operator in conditionals to check if something is not True or False, like this:

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.')
else:
    print('Welcome, Administrator!')

#Since is_admin is False, then not is_admin is saying not False which is True. So the message Access denied for non-administrators. will be printed.\

# Now that you understand truthy and falsy values, the and, or, and not operators, and how short-circuiting works, you can write more flexible and readable conditional logic.


 
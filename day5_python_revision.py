#----------------------------------------
#----------------------------------------
#---How Do Augmented Assignments Work?---
#----------------------------------------
#----------------------------------------

#Augmented assignment combines a binary operation with an assignment in one step.It takes a variables, applies an operation to it with another value, and stores the result back into the same variable.

#If you're familiar with a language like javaScript, you've probably heard of the addition assignment operator (+=) or subraction assignment (-=), and others. Those exist in python, too. The only difference is that they're referred to as augmented assignments.

# syntax of an augmented assignment looks like this :

#variable <operator>= value

#which is more efficient way of doing this:

#variable = variable <operator> value

#For example,here's an example of using augmented assignment to add 5 to an exsisting variable:

my_var = 17
my_var+=5
print(my_var)

#And here is the same thing, but without augmented assignment:

my_var = 12
my_var = my_var + 5
print(my_var)

#The advantage of augmented assignment is that it provides a concise and readable way to update a variable value without repeating the variable name.In turn, this reduces redundancy and potential errors that might arise from a typo or something similar.

#Every operator can use an augmented assignment. we've looked at the addition assignment operator(+=),so let'd look at others.

#The Subtraction assignment operator (-=) subtracts the right operand from the left variable and stores the difference in the left variable:

count = 14
count -= 2
print(count)

#The multiplication assignment operator (*=) multiplies the left variable by the right operand and stored the product bank in the left variable:

product=5
product*=5
print(product)

#The division assignment operator (/=) divides the left variable by the right and stores the result back in the left variable:

price=100
price/=4
print(price)

#The floor division operator (//=) floor-divides the left variable by the right and stores the result back in the left variable:

total_page = 23
total_page//=4
print(total_page)

#The modulo assignment operator (%=) computes the remainder of the left variable divided by the right and stored it back in the left variable:

bits = 35
bits %= 2

print(bits)

# The exponentiation assignment operator (**=) raises the left variable to the power of right and stores the result back in the left variable:

power = 3
power **= 2
print(power)

# You can use some augmented assignment operators with strings, too.For example, the addition operator makes it easy to concatenate strings;

greet = "Hello"
greet+=" World"
print(greet)

# And the multiplication assignment operator can be used to repeat a string:

greet="Hello"
greet*=3
print(greet)

#other augmented assignment throw a TypeError when you use them with strings:

#greet = "Hi"
#greet-= "World"

#print(greet) 

#greet = 'Hello'
#greet /= "World"
#print(greet)

#If you're wondering if increment and decrement operators (++ and --) work in python, they don't. That's because Python deliberately avoids C- style increment and decrement shortcuts in order to keep the language clear and explicit.

#Instead of x++, you can simply write x+=1, which makes it obvious that you're incrementing the value of x by 1.

#Writing ++x in python just applies the unary plus twice, and does not increment anything:

my_var = 5

print(+my_var)
print(++my_var)
print(+++my_var)

my_var += 1

print(my_var)
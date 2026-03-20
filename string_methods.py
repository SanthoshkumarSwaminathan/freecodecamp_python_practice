my_str = 'Santhosh Kumar S'


#upper(): Returns a new string with all characters converted to uppercase.

upper_my_string = my_str.upper()
print(upper_my_string)

#lower(): Returns a new string with all characters converted to lowercase.

lower_my_string = my_str.lower()
print(lower_my_string)


#strip(): Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.
my_str = "   Hello boy  "

trimmed_my_str = my_str.strip()

print(trimmed_my_str)

my_strip_str = "111 hello eee"

trim_my_strip_str = my_strip_str.strip("111, ,eee")
print(trim_my_strip_str)

#replace(old, new): Returns a new string with all occurrences of old replaced by new.

my_str = 'hello santhosh'
print("Before replace my_str variable contains : ",my_str)
replaced_my_str = my_str.replace('hello','I am')
print("After replace:",replaced_my_str)

#split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.

split_words = my_str.split()
print(split_words) #['hello', 'santhosh']

#join(iterable): Joins elements of an iterable into a string with a separator.

my_list = ["Hello", "World"]
joined_my_str = " ".join(my_list)
print(joined_my_str)

#startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix.

my_list = "Hello World"
starts_with_hello = my_list.startswith("Hello")
print(starts_with_hello)

#endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.

ends_with_world = my_list.endswith("World")
print(ends_with_world)

#find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one.

my_str = "My name is Santhosh Kumar"

world_index = my_str.find("name")
print(world_index)

#count(substring): Returns the number of times a substring appears in a string.

my_str = "Hello Santhosh"
o_count = my_str.count("h")
print(o_count)

#capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.

my_str = "hello abi"

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)

#isupper(): Returns True if all letters in the string are uppercase and False if not.

is_all_upper = my_str.isupper()
print(is_all_upper)

#islower(): Returns True if all letters in the string are lowercase and False if not.

is_all_lower = my_str.islower()
print(is_all_lower)

#title(): Returns a new string with the first letter of each word capitalized.

title_case_my_str = my_str.title()
print(title_case_my_str)
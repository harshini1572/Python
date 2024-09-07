#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Q1. Write a Python program to print numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)


# In[ ]:


#Q2. Explain the difference between a for loop and a while loop in Python.

A for loop iterates over a sequence (like a list or range), while a while loop continues to execute as long as 
its condition remains true.


# In[8]:


#Q3. Write a Python program to calculate the sum of all numbers from 1 to 100 using a for loop.

total = 0
for i in range(1, 101):
    total += i
print(total)


# In[9]:


#Q4. How do you iterate through a list using a for loop in Python?

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)


# In[10]:


#Q5. Write a Python program to find the product of all elements in a list using a for loop.

numbers = [1, 2, 3, 4]
product = 1
for num in numbers:
    product *= num
print(product)


# In[11]:


#Q6. Create a Python program that prints all even numbers from 1 to 20 using a for loop.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# In[12]:


#Q7. Write a Python program that calculates the factorial of a number using a for loop.

n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)


# In[13]:


#Q8. How can you iterate through the characters of a string using a for loop in Python?

my_string = "hello"
for char in my_string:
    print(char)


# In[14]:


#Q9. Write a Python program to find the largest number in a list using a for loop.

numbers = [3, 1, 4, 1, 5, 9]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(largest)


# In[15]:


#Q10. Create a Python program that prints the Fibonacci sequence up to a specified limit using a for loop.

limit = 10
a, b = 0, 1
while a <= limit:
    print(a)
    a, b = b, a + b


# In[16]:


#Q11. Write a Python program to count the number of vowels in a given string using a for loop.

my_string = "hello world"
vowels = "aeiou"
count = 0
for char in my_string:
    if char in vowels:
        count += 1
print(count)


# In[17]:


#Q12. Create a Python program that generates a multiplication table for a given number using a for loop.

num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# In[18]:


#Q13. Write a Python program to reverse a list using a for loop.

my_list = [1, 2, 3, 4]
reversed_list = []
for item in my_list:
    reversed_list.insert(0, item)
print(reversed_list)


# In[19]:


#Q14. Write a Python program to find the common elements between two lists using a for loop.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = []
for item in list1:
    if item in list2:
        common_elements.append(item)
print(common_elements)


# In[20]:


#Q15. Explain how to use a for loop to iterate through the keys and values of a dictionary in Python.

my_dict = {'a': 1, 'b': 2}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


# In[21]:


#Q16. Write a Python program to find the GCD (Greatest Common Divisor) of two numbers using a for loop.

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print(gcd(48, 18))


# In[22]:


#Q17. Create a Python program that checks if a string is a palindrome using a for loop.

my_string = "radar"
is_palindrome = True
for i in range(len(my_string) // 2):
    if my_string[i] != my_string[-i - 1]:
        is_palindrome = False
        break
print(is_palindrome)


# In[23]:


#Q18. Write a Python program to remove duplicates from a list using a for loop.

my_list = [1, 2, 2, 3, 4, 4]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)


# In[24]:


#Q19. Create a Python program that counts the number of words in a sentence using a for loop.

sentence = "This is a sentence."
words = sentence.split()
count = 0
for word in words:
    count += 1
print(count)


# In[25]:


#Q20. Write a Python program to find the sum of all odd numbers from 1 to 50 using a for loop.

total = 0
for i in range(1, 51):
    if i % 2 != 0:
        total += i
print(total)


# In[26]:


#Q21. Write a Python program that checks if a given year is a leap year using a for loop.

year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[27]:


#Q22. Create a Python program that calculates the square root of a number using a for loop.

import math
number = 16
sqrt = math.sqrt(number)
print(sqrt)


# In[28]:


#Q23. Write a Python program to find the LCM (Least Common Multiple) of two numbers using a for loop.

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

print(lcm(4, 5))


# In[29]:


###If-Else


# In[30]:


#Q1. Write a Python program to check if a number is positive, negative, or zero using an if-else statement.

num = 3
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# In[31]:


#Q2. Create a Python program that checks if a given number is even or odd using an if-else statement.

num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# In[32]:


#Q3. How can you use nested if-else statements in Python, and provide an example?

num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Non-Positive")


# In[33]:


#Q4. Write a Python program to determine the largest of three numbers using if-else.

a, b, c = 5, 10, 7
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# In[34]:


#Q5. Write a Python program that calculates the absolute value of a number using if-else.

num = -5
if num < 0:
    print(-num)
else:
    print(num)


# In[35]:


#Q6. Create a Python program that checks if a given character is a vowel or consonant using if-else.

char = 'e'
if char in 'aeiou':
    print("Vowel")
else:
    print("Consonant")


# In[36]:


#Q7. Write a Python program to determine if a user is eligible to vote based on their age using if-else.

age = 20
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# In[37]:


#Q8. Create a Python program that calculates the discount based on the purchase amount using if-else.

amount = 150
if amount > 100:
    discount = amount * 0.1
else:
    discount = 0
print("Discount:", discount)


# In[38]:


#Q9. Write a Python program to check if a number is within a specified range using if-else.

num = 15
if 10 <= num <= 20:
    print("Within range")
else:
    print("Out of range")


# In[40]:


#Q10. Create a Python program that determines the grade based on the score using if-else.

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# In[41]:


#Q11. Write a Python program to check if a string is empty or not using if-else.

string = ""
if not string:
    print("String is empty")
else:
    print("String is not empty")


# In[42]:


#Q12. Create a Python program that identifies the type of a triangle (e.g., equilateral, isosceles, or scalene) 
# based on input values using if-else.

a = 5
b = 5
c = 7
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# In[43]:


#Q13. Write a Python program to determine the day of the week based on a user-provided number using if-else.

day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")


# In[44]:


#Q14. Create a Python program that checks if a given year is a leap year using both if-else and a function.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# In[45]:


#Q15. How do you use the "assert" statement in Python to add debugging checks within if-else blocks? 

The assert statement is used to test if a condition is true. If the condition is false, it raises an AssertionError.

num = 10
assert num > 0, "Number must be positive"


# In[46]:


#Q16. Create a Python program that determines the eligibility of a person for a senior citizen discount based on age using if-else.

age = 70
if age >= 65:
    print("Eligible for senior citizen discount")
else:
    print("Not eligible for senior citizen discount")


# In[47]:


#Q17. Write a Python program to categorize a given character as uppercase, lowercase, or neither using if-else.

char = 'a'
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("Lowercase")
else:
    print("Neither uppercase nor lowercase")


# In[48]:


#Q18. Write a Python program to determine the roots of a quadratic equation using if-else.

import math

a = 1
b = -3
c = 2

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots are {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Root is {root}")
else:
    print("No real roots")


# In[49]:


#Q19. Create a Python program that checks if a given year is a century year or not using if-else.

year = 1900
if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")


# In[50]:


#Q20. Write a Python program to determine if a given number is a perfect square using if-else.

import math

num = 25
sqrt = math.sqrt(num)
if sqrt.is_integer():
    print("Perfect square")
else:
    print("Not a perfect square")


# In[51]:


#Q21. Explain the purpose of the "continue" and "break" statements within if-else loops.

The continue statement skips the rest of the code inside the loop for the current iteration and moves to the 
next iteration.
The break statement exits the loop entirely.


# In[52]:


#Q22. Create a Python program that calculates the BMI (Body Mass Index) of a person based on their weight and 
# height using if-else.

weight = 70  # in kilograms
height = 1.75  # in meters
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")



# In[ ]:


#Q23. How can you use the "filter()" function with if-else statements to filter elements from a list?

The filter() function can use a lambda function or named function with an if-else condition to filter elements.

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]


# In[53]:


#Q24. Write a Python program to determine if a given number is prime or not using if-else.

num = 29
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")


# In[54]:


###MAP


# In[ ]:


#Q1. Explain the purpose of the map() function in Python and provide an example of how it can be used to apply a 
# function to each element of an iterable.

The map() function applies a given function to each item of an iterable (like a list) and returns a map object
(an iterator). 

def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16]


# In[55]:


#Q2. Write a Python program that uses the map() function to square each element of a list of numbers.

numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16]


# In[ ]:


#Q3. How does the map() function differ from a list comprehension in Python, and when would you choose one over the other?

map() applies a function to each item of an iterable and returns an iterator. It is useful when you already have 
a function defined.
List comprehensions are more readable and can include more complex logic, including conditional statements.


# In[56]:


#Q4. Create a Python program that uses the map() function to convert a list of names to uppercase.

names = ["alice", "bob", "charlie"]
uppercase_names = map(lambda name: name.upper(), names)
print(list(uppercase_names))  # Output: ['ALICE', 'BOB', 'CHARLIE']


# In[57]:


#Q5. Write a Python program that uses the map() function to calculate the length of each word in a list of strings.

words = ["apple", "banana", "cherry"]
lengths = map(len, words)
print(list(lengths))  # Output: [5, 6, 6]


# In[58]:


#Q6. How can you use the map() function to apply a custom function to elements of multiple lists simultaneously
# in Python? 

def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(add, list1, list2)
print(list(result))  # Output: [5, 7, 9]


# In[59]:


#Q7. Create a Python program that uses map() to convert a list of temperatures from Celsius to Fahrenheit.

celsius = [0, 10, 20, 30]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))  # Output: [32.0, 50.0, 68.0, 86.0]


# In[60]:


#Q8. Write a Python program that uses the map() function to round each element of a list of floating-point 
# numbers to the nearest integer.

floats = [1.2, 2.5, 3.7, 4.8]
rounded_numbers = map(round, floats)
print(list(rounded_numbers))  # Output: [1, 2, 4, 5]


# In[61]:


## REDUCE


# In[ ]:


#Q1. What is the reduce() function in Python, and what module should you import to use it? 
# Provide an example of its basic usage.

The reduce() function applies a function cumulatively to the items of an iterable, reducing it to a single value.
It is imported from the functools module. 

from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24


# In[62]:


#Q2. Write a Python program that uses the reduce() function to find the product of all elements in a list.

from functools import reduce

numbers = [2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24


# In[63]:


#Q3. Create a Python program that uses reduce() to find the maximum element in a list of numbers.

from functools import reduce

numbers = [1, 5, 3, 9, 2]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # Output: 9


# In[64]:


#Q4. How can you use the reduce() function to concatenate a list of strings into a single string?

from functools import reduce

words = ["Hello", "world", "from", "reduce"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # Output: Hello world from reduce


# In[65]:


#Q5. Write a Python program that calculates the factorial of a number using the reduce() function.

from functools import reduce
import operator

number = 5
factorial = reduce(operator.mul, range(1, number + 1))
print(factorial)  # Output: 120


# In[66]:


#Q6. Create a Python program that uses reduce() to find the GCD (Greatest Common Divisor) of a list of numbers.

from functools import reduce
import math

numbers = [24, 60, 36]
gcd = reduce(math.gcd, numbers)
print(gcd)  # Output: 12


# In[67]:


#Q7. Write a Python program that uses the reduce() function to find the sum of the digits of a given number.

from functools import reduce

number = 1234
sum_of_digits = reduce(lambda x, y: x + y, map(int, str(number)))
print(sum_of_digits)  # Output: 10


# In[68]:


## Filter


# In[ ]:


#Q1. Explain the purpose of the filter() function in Python and provide an example of how it can be used to 
# filter elements from an iterable. 

The filter() function filters elements of an iterable based on a function that returns either True or False.

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4]


# In[69]:


#Q2. Write a Python program that uses the filter() function to select even numbers from a list of integers.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]


# In[70]:


#Q3. Create a Python program that uses the filter() function to select names that start with a specific letter 
# from a list of strings.

names = ["Alice", "Bob", "Charlie", "Annie"]
starts_with_a = filter(lambda name: name.startswith('A'), names)
print(list(starts_with_a))  # Output: ['Alice', 'Annie']


# In[71]:


#Q4. Write a Python program that uses the filter() function to select prime numbers from a list of integers.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8]
primes = filter(is_prime, numbers)
print(list(primes))  # Output: [2, 3, 5, 7]


# In[72]:


#Q5. How can you use the filter() function to remove None values from a list in Python?

items = [1, None, 2, None, 3]
non_none_items = filter(lambda x: x is not None, items)
print(list(non_none_items))  # Output: [1, 2, 3]


# In[73]:


#Q6. Create a Python program that uses filter() to select words longer than a certain length from a list of strings.

words = ["apple", "banana", "cherry", "date"]
long_words = filter(lambda word: len(word) > 5, words)
print(list(long_words))  # Output: ['banana', 'cherry']


# In[74]:


#Q7. Write a Python program that uses the filter() function to select elements greater than a specified threshold 
# from a list of values.

numbers = [10, 20, 30, 40]
threshold = 25
above_threshold = filter(lambda x: x > threshold, numbers)
print(list(above_threshold))  # Output: [30, 40]



# In[75]:


### Recursion


# In[ ]:


#Q1. Explain the concept of recursion in Python. How does it differ from iteration?

Recursion is a technique where a function calls itself.


# In[76]:


#Q2. Write a Python program to calculate the factorial of a number using recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# In[77]:


#Q3. Create a recursive Python function to find the nth Fibonacci number.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8


# In[78]:


#Q4. Write a recursive Python function to calculate the sum of all elements in a list.

def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))  # Output: 10


# In[ ]:


#Q5. How can you prevent a recursive function from running indefinitely, causing a stack overflow error? 

By defining a base case that stops the recursion, you ensure the function eventually ends


# In[79]:


#Q6. Create a recursive Python function to find the greatest common divisor (GCD) of two numbers using the 
# Euclidean algorithm.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(48, 18))  # Output: 6


# In[80]:


#Q7. Write a recursive Python function to reverse a string.

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # Output: "olleh"


# In[81]:


#Q8. Create a recursive Python function to calculate the power of a number (x^n).

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2, 3))  # Output: 8


# In[82]:


#Q9. Write a recursive Python function to find all permutations of a given string.

def permutations(s):
    if len(s) == 0:
        return [""]
    perms = []
    for i, char in enumerate(s):
        for perm in permutations(s[:i] + s[i+1:]):
            perms.append(char + perm)
    return perms

print(permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


# In[83]:


#Q10. Write a recursive Python function to check if a string is a palindrome.

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))  # Output: True


# In[85]:


#Q11. Create a recursive Python function to generate all possible combinations of a list of elements.

def combinations(lst):
    if len(lst) == 0:
        return [[]]
    first = lst[0]
    rest = combinations(lst[1:])
    return rest + [comb + [first] for comb in rest]

print(combinations([1, 2, 3]))  


# In[86]:


###Basics of Functions


# In[ ]:


#Q1. What is a function in Python, and why is it used?

A function is a reusable block of code that performs a specific task. It is used to avoid code repetition and
improve code organization.


# In[87]:


#Q2. How do you define a function in Python? Provide an example.

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!


# In[ ]:


#Q3. Explain the difference between a function definition and a function call.

A function definition specifies the function's name and behavior, while a function call executes the function.


# In[88]:


#Q4. Write a Python program that defines a function to calculate the sum of two numbers and then calls the function.

def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8


# In[ ]:


#Q5. What is a function signature, and what information does it typically include?

A function signature includes the function's name, parameters, and return type.


# In[89]:


#Q6. Create a Python function that takes two arguments and returns their product.

def multiply(a, b):
    return a * b

print(multiply(4, 5))  # Output: 20


# In[90]:


## Function Parameters and Arguments


# In[ ]:


#Q1. Explain the concepts of formal parameters and actual arguments in Python functions.

Formal parameters are variables listed in the function definition. Actual arguments are the values passed to the 
function when called.


# In[91]:


#Q2. Write a Python program that defines a function with default argument values.

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!


# In[92]:


#Q3. How do you use keyword arguments in Python function calls? Provide an example. 

Keyword arguments allow you to specify arguments by name.

def greet(name, age):
    return f"Name: {name}, Age: {age}"

print(greet(age=25, name="Alice"))  # Output: Name: Alice, Age: 25


# In[93]:


#Q4. Create a Python function that accepts a variable number of arguments and calculates their sum.

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10


# In[ ]:


#Q5. What is the purpose of the *args and **kwargs syntax in function parameter lists?

*args allows a function to accept a variable number of positional arguments, while **kwargs allows it to accept
a variable number of keyword arguments.


# In[ ]:


#6. Create a Python function that takes two arguments and returns their product.
def product(a,b):
    return a*b
a=2
b=3
product(a,b)


# In[94]:


###Return Values and Scoping


# In[95]:


#Q1. Describe the role of the return statement in Python functions and provide examples.

The return statement sends a result back to the caller. 

def square(x):
    return x * x

print(square(4))  # Output: 16


# In[ ]:


#Q2. Explain the concept of variable scope in Python, including local and global variables.

Local variables are defined within a function and are accessible only inside it. Global variables are defined 
outside any function and are accessible throughout the module.


# In[96]:


#Q3. Write a Python program that demonstrates the use of global variables within functions.

global_var = 10

def print_global():
    global global_var
    print(global_var)

print_global()  # Output: 10


# In[97]:


#Q4. Create a Python function that calculates the factorial of a number and returns it.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# In[ ]:


#Q5. How can you access variables defined outside a function from within the function? 

By using the global keyword to indicate that a variable is global.


# In[ ]:


###Lambda Functions and Higher-Order Functions


# In[ ]:


#Q1. What are lambda functions in Python, and when are they typically used?

Lambda functions are small anonymous functions defined with the lambda keyword. They are used for simple 
operations that can be defined in a single line.


# In[98]:


#Q2. Write a Python program that uses lambda functions to sort a list of tuples based on the second element.

data = [(1, 3), (2, 2), (4, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(4, 1), (2, 2), (1, 3)]


# In[99]:


#Q3. Explain the concept of higher-order functions in Python, and provide an example. 

Higher-order functions are functions that take other functions as arguments or return them. 

def apply_func(func, x):
    return func(x)

def square(n):
    return n * n

print(apply_func(square, 5))  # Output: 25


# In[100]:


#Q4. Create a Python function that takes a list of numbers and a function as arguments, applying the function to 
# each element in the list.

def apply_to_list(lst, func):
    return [func(x) for x in lst]

numbers = [1, 2, 3]
print(apply_to_list(numbers, lambda x: x * x))  # Output: [1, 4, 9]


# In[101]:


## Built-in Functions


# In[102]:


#Q1. Describe the role of built-in functions like len(), max(), and min() in Python. 

len() returns the number of items in an object. max() returns the largest item, and min() returns the smallest item.


# In[103]:


#Q2. Write a Python program that uses the map() function to apply a function to each element of a list.

numbers = [1, 2, 3]
squares = map(lambda x: x * x, numbers)
print(list(squares))  # Output: [1, 4, 9]


# In[ ]:


#Q3. How does the filter() function work in Python, and when would you use it? 

The filter() function applies a function to each element of an iterable and returns those that return True. 
It is used to select elements based on a condition.


# In[104]:


#Q4. Create a Python program that uses the reduce() function to find the product of all elements in a list.

from functools import reduce

numbers = [2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24


# In[105]:


### Function Documentation and Best Practices


# In[ ]:


#Q1. Explain the purpose of docstrings in Python functions and how to write them.

Docstrings provide a description of what the function does. They are written inside triple quotes right after 
the function definition.


# In[106]:


#Q2. Describe some best practices for naming functions and variables in Python, including naming conventions 
# and guidelines. 

Use descriptive names, follow naming conventions like snake_case for functions and variables, and avoid using
single-letter names unless they are commonly understood.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ## 1. Intro to Python

# In[1]:


#Introduction to Python
## 1.1 What is Python

# 1.What is Python?
# Ans: Python is a popular programming language
# 2.Who created Python? 
# Ans: Python was created by Guido Van Rossum 
# 3.In which year was Python created? 
# Ans: Python was created on February 20th in 1991
# 4.Python is a programming language. (True/False) 
# Ans: True
# 5.Python is named after a type of snake. (True/False) 
# Ans: False 
# 6. Is Python used for web development? (Yes/No) 
# Ans: Yes
# 7.Is Python used in data science? (Yes/No) 
# Ans: Yes
# 8.Name one popular website that uses Python
# Ans: Netflix
# 9.Python is easy to read and write. (True/False) 
# Ans: True
# 10.Python is an interpreted language. (True/False)
# Ans: True


# In[2]:


# 1.2 Installing Python and setting up the environment

# 11. Where can you download Python from?
# Ans: Windows , MacOn and Linux 
# 12. What is the latest version of Python? (as of now)
# Ans: 3.12 Bugfix
# 13.Python can be installed on Windows, Mac, and Linux. (True/False)
# Ans: True 
# 14.What is an IDE?
# Ans: Intergrated Development Environment 
# 15.Name one popular Python IDE.
# Ans: Anaconda Navigator 
# 16.What is the command to check Python version in the command line? 
#Ans: Python --version or python -V
# 17. Write the command to start Python interactive shell.
# Ans: Start Python 
# 18.How do you exit the Python interactive shell? 
# Ans: ctrl + Z on Windows and ctrl + C on MacOs and linux
# 19.What is a virtual environment in Python
# Ans: It is a clone of your original work, virtual environment is directory containing its own Python installation and dependencies, which helps manage project specific libraries
# 20. Why should we use a virtual environment?
# Ans: It is needed that if you want to do trial and error and do a mistake you still have your original work


# ## 2. Basic Syntax

# In[3]:


# 2.1 Writing and executing your first Python program

# 1. What is the extension of a Python file?
# Ans: ".py"
# 2.Write a simple Python program that prints "Hello, World!". 
# Ans: 
print("Hello, World")


# In[8]:


# 3. What is the command to run a Python file? 
# Ans: "python" or in short "py" or python myfile.py
# 4.How do you write a comment in Python? 
# Ans: Hashtag + The comment you want to write 
# 5.What will the following code print? `print("Python is fun!")`
# Ans: Python is fun!
# 6.Comments in Python start with which symbol? 
# Ans: #
# 7.Can Python print numbers? (Yes/No)
# Ans: Yes
# 8.Write a Python program to print the sum of 2 and 3. 
# Ans: 
print(2+3)


# In[9]:


# 9.What is a syntax error? 
# Ans: It is a Error in your code / programm or Syntax errors are invalidities in the code's structure.
# 10.What will the following code print? `print(10 + 5)`
# Ans: 15
print(10+5)


# ## 2.2 Python Interactive Shell

# In[10]:


# 2.2 Python Interactive Shell

# 11. What is the Python interactive shell?
# Ans: The Python interactive console, also known as Python interpreter or Python shell,
#      provides programmers with a quick way to execute commands and try out and test code without creating a file.
# 12. How do you start the Python interactive shell?
# Ans: Start Python 
# 13. How do you print your name using the Python shell? 
# Ans: 
print("Aarush")


# In[11]:


# 14. What will the Python shell print if you type `5 * 2`?
# Ans: 10
print(5*2)


# In[14]:


# 15. Can you write multiple lines of code in the Python shell? (Yes/No)
# Ans: Yes 
# 16. What does the `>>>` symbol mean in Python shell?
# Ans: That >>> is called a prompt, which means it's something the computer displays to tell you it's ready for your instructions.
# 17. How do you clear the screen in the Python shell?
# Ans: ctrl+l or clear or cls
# 18. How do you exit the Python shell?
# Ans: ctrl + Z on Windows and ctrl + D on MacOs/linux
# 19. Can you save your work from the Python shell? (Yes/No)
# Ans: Yes(The contents of the Python window can be saved to a Python file or text file. Right-click the Python window and select Save As to save your code either as a Python file (. py) or Text file . txt
# 20.  How do you write a for loop in the Python shell?
# Ans: You write for and your statement
#Example 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)


# ## 3. Variables and Data Types

# In[15]:


# 3. Variables and Data Types

# 1. What is a variable?
# Ans: A Python variable is a reserved memory location to store values   
# 2. How do you declare a variable in Python?
# Ans: Python has no command for declaring a variable,A variable is created the moment you first assign a value to it.
# 3. Can a variable name start with a number? (Yes/No)
# Ans: No  :: Rules for Python variables: A variable name must start with a letter or the underscore character. A variable name cannot start with a number. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ), Variable names are case-sensitive (age, Age and AGE are three different variables), A variable name cannot be any of the Python keywords.
# 4. Is `myVar` a valid variable name? (Yes/No) 
# Ans: yes
# 5. Is `1stVar` a valid variable name? (Yes/No)
# Ans: No
# 6. What is the correct way to name a variable in Python?
# Ans: A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
#Rules for Python variables:
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.
# 7. Are variable names case-sensitive in Python? (Yes/No)
# Ans: Yes
# 8. What will the following code print? `x = 5; print(x)`
# Ans: 5 
x = 5
print(x)



# In[16]:


# 9. Can a variable name contain spaces? (Yes/No)
# Ans: No  (Variables can only contain letters, numbers, and underscores. Variable names can start with a letter or an underscore, but can not start with a number. Spaces are not allowed in variable names, so we use underscores instead of spaces.)
# 10.  What will the following code print? `x = "Hello"; print(x)`
# Ans: Hello 
X = "Hello"
print(X)


# ## 3.2 Basic Data Types: int, float, str, bool

# In[12]:


# 3.2 Basic Data Types: int, float, str, bool

# 1. What is an integer in Python?  
# Ans: An Integer is a Number , Int, or integer, is a whole number,
#      positive or negative, without decimals, of unlimited length
# 2. What is a float in Python?
# Ans: A Float is Number with a decimal
# 3. What is a string in Python?
# Ans: Strings in python are surrounded by either single quotation
#      marks, or double quotation marks.
# 4. What is a boolean in Python?
# Ans: True or False 
# 5.  What will the following code print? `x = 10; print(type(x))`
# Ans: <class 'int'>
x = 5
print(type(x))


# In[19]:


# 6.  What will the following code print? `x = 10.5; print(type(x))`
# Ans: <class 'float'>
x = 10.5
print(type(x))


# In[20]:


# 7. What will the following code print? `x = "Python"; print(type(x))`
# Ans: <class 'str'>  
x = "python"
print(type(x))


# In[21]:


# 8. What will the following code print? `x = True; print(type(x))`
# Ans: <class 'bool'>
x = True
print(type(x))


# In[ ]:


# 9.. Can a string contain numbers? (Yes/No)
# Ans: Yes
# 10. Can a boolean be either True or False? (Yes/No)
# Ans: Yes


# In[23]:


# Type Conversion

# 1. What is type conversion?
# Ans: Type conversion in Python refers to the direct conversion of object of one data type to another data type
# 2. How do you convert an integer to a string in Python?
# Ans: You can convert an integer to a string using the str() function.
x = str(1)
print(x)


# In[24]:


# 3. What will the following code print? `x = 5; y = str(x); print(type(y))`
# Ans:<class 'str'>
x = 5
y = str(x)
print(type(y))


# In[26]:


# 4. How do you convert a string to an integer in Python?
# Ans: You have to use the built-in int() function
x = int(1)
print(x)


# In[27]:


# 5. What will the following code print? `x = "10"; y = int(x); print(type(y))`
# Ans: <class 'int'>
x = 10
y = int(x)
print(type(y))


# In[28]:


# 6. Can you convert a float to an integer? (Yes/No)
# Ans: Yes
# 7. What will the following code print? `x = 10.5; y = int(x); print(y)`
# Ans: 10 
x = 10.5
y = int(x)
print(y)


# In[29]:


# 8. How do you convert an integer to a float in Python?
# Ans: You have to use the float() function 
x = float(1)
print(x)


# In[30]:


# 9. What will the following code print? `x = 5; y = float(x); print(y)
# Ans: 5.0
x = 5
y = float(x) 
print(y)


# In[ ]:


# 10. Can you convert a boolean to an integer? (Yes/No)
# Ans: Yes 


# ## 4. Operators

# In[32]:


# 4.1 Arithmetic Operators

# 1. What are arithmetic operators?
# Ans: They are Symbols or functions that perform mathematical operations such as addition  subtraction (-), multiplication (*), division (/), modulo (%), and exponentiation (**).
# 2. What is the addition operator in Python?
# Ans: You can add two numbers to get the sum
#example x+y
x = 5
y = 3
print(x + y)


# In[33]:


# 3. What is the subtraction operator in Python?
# Ans: You can subbract two numbers to get the difference
#example 
x = 5
y = 3
print(x - y)


# In[34]:


# 4. What is the multiplication operator in Python?
# Ans: You can multiply two numbers to get the product
x = 5
y = 3
print(x *y)


# In[35]:


# 5.What is the division operator in Python?
# Ans: You can divide two numbers to get the quotient
x = 12
y = 3
print(x  /y)


# In[36]:


# 6. What is the modulus operator in Python?
# Ans: The modulus operator is the percentage 
x = 5
y = 2
print(x % y)



# In[37]:


# 7. What is the exponentiation operator in Python?
# Ans: It is the ** sign in python it multiplies everything 3 times
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2


# In[38]:


# 8. What is the floor division operator in Python?
# Ans: It rounds the division up to a full number from a decimal number
x = 15
y = 2
print(x // y)#the floor division // rounds the result down to the nearest whole number


# In[39]:


# 9. What will the following code print? `print(5 + 3)`
# Ans: 8
print(5 + 3)


# In[40]:


# 10.What will the following code print? `print(10 - 2)`
# Ans:8
print(10 - 2)


# ## 4.2 Comparison Operators

# In[1]:


# 4.2 Comparison Operators

# 1. What are comparison operators?
# Ans: They are operators that compare values and return true or false

# 2. What is the equality operator in Python?
# Ans: It checks if two variables or values are equal. ,x == y
x = 5
y = 3
print(x == y)# returns False because 5 is not equal to 3


# In[2]:


# 3. What is the inequality operator in Python?
# Ans: It checks if two variables or values are not equal,  x != y
x = 5

y = 3

print(x != y)# returns Ture because 5 is not equal to 3



# In[3]:


# 4. What is the greater than operator in Python?
# Ans: It checks if the value on the left side is greater than the value on the right side
#example :x > y
x = 5
y = 3
print(x > y)# returns True because 5 is greater than


# In[5]:


# 5. What is the less than operator in Python?
# Ans: It checks whether the value on its left side is smaller than the value on its right side
x = 5
y = 3
print(x <  y)# # returns False because 5 is not less than3


# In[6]:


# 6.  What is the greater than or equal to operator in Python?
# Ans:It returns True if the value on its left side is greater than or equal to the value on its right side, False otherwise.
x = 5
y = 3
print(x >= y) # returns True because five is greater, or equal, to 3
 


# In[7]:


# 7. What is the less than or equal to operator in Python?
# Ans: It returns True if the value on its left side is greater than or equal to the value on its right side,False otherwise.
x = 5
y = 3
print(x <= y)# returns False because 5 is neither less than or equal to 3



# In[8]:


# 8. What will the following code print? `print(5 == 5)`
# Ans: True 
print(5 == 5)


# In[9]:


# 9. What will the following code print? `print(5 != 3)` 
# Ans: True 
print(5 != 3)


# In[10]:


# 10. What will the following code print? `print(5 > 3)` 
# Ans: True
print(5 >3)


# ## 4.3 Logical Operator

# In[13]:


# 4.3 Logical Operator
# 1. What are logical operators?
# Ans: It evaluates multiple conditions and determine an expression's overall truth value
# 2. What is the AND operator in Python?
# Ans: It is a logical operator that returns True if both the operands are true
#example 
x = 5
print(x > 3 and x < 10)# returns True because 5 is greater than 3 AND 5 is less than 10


# In[14]:


# 3. What is the OR operator in Python?
#Ans :Returns True if one of the statements is true
x = 5
print(x > 3 or x < 4)# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


# In[15]:


# 4.What is the NOT operator in Python? 
#Ans : Reverse the result, returns False if the result is true
x = 5
print(not(x > 3 and x < 10))# returns False because not is used to reverse the result


# In[16]:


# 5. What will the following code print? `print(True and False)`
#Ans : False
print(True and False)


# In[17]:


#6. What will the following code print? `print(True or False)` 
#Output : True
print(True or  False)


# In[18]:


#7. What will the following code print? `print(not True)` 
#Output : false 
print(not True)


# In[19]:


#8.What will the following code print? `print(5 > 3 and 3 > 1)`
#Output : True
print(5 > 3 and 3 > 1)


# In[20]:


#9.What will the following code print? `print(5 > 3 or 3 < 1)` 
#Output : True
print(5 > 3 or 3 < 1)


# In[21]:


#10.What will the following code print? `print(not (5 > 3))`
#Output : True
print(not (5 > 3))


# ## 4.4 Assignment Operators 

# In[22]:


# 1.What are assignment operators? 
# Ans : Assignment operators are used to assign values to variables
#2. What is the assignment operator in Python? 
#Ans : =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=
#3.What does `+=` do in Python?
#Ans : x += 3 #same as x = x + 3
x = 5
x += 3
print(x)


# In[23]:


#4. What does `-=` do in Python? 
#Ans : x -= 3 #same as x = x – 3
x = 5
x -= 3
print(x)


# In[24]:


#5. What does `*=` do in Python? 
#Ans :      x *= 3 # same as x = x * 3
x = 5
x *= 3
print(x)



# In[25]:


#6. What does `/=` do in Python? 
#Ans : x /= 3 #same as x = x / 3
x = 5
x /= 3
print(x)


# In[26]:


#7. What will the following code print? `x = 5; x += 3; print(x)` 
x = 5
x += 3
print(x)


# In[27]:


#8. What will the following code print? `x = 5; x -= 2; print(x)` 
x = 5
x -= 3
print(x)


# In[28]:


#9. What will the following code print? `x = 5; x *= 2; print(x)` 
x = 5
x *= 2
print(x)


# In[29]:


#10. What will the following code print? `x = 5; x /= 2; print(x)`
x = 5
x /= 2
print(x)


# ## 5. Control Flow

# In[11]:


#5.1 Conditional Statements: if, elif, else
#1. What is a conditional statement?
#Ans : Conditional statements (if, else, and elif) are fundamental programming constructs that allow you to control the flow of your program based on conditions that you specify.

#2. How do you write an if statement in Python?

#Ans : An "if statement" is written by using the if keyword.
#Example : 
a = 33
b = 200
if b > a:
   print("b is greater than a")


# In[21]:


#3. What does elif stand for?
#Ans : The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
#Example:  
a = 33
b = 33
if b > a:
 print("b is greater than a")
elif a == b:
   print("a and b are equal")


# In[32]:


#4. How do you write an else statement in Python?
#Ans : The else keyword catches anything which isn't caught by the preceding conditions.
#Example : 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# In[34]:


#5. What will the following code print? 
x = 5 
if x > 3: 
print("x is greater than 3") 
#Output : IndentationError: expected an indented block



# In[35]:


#5.1 Correct via need space at line 3 being of print statment
x = 5 
if x > 3: 
  print("x is greater than 3") 


# In[37]:


#6. What will the following code print? 
x = 5 
if x > 5: 
print("x is greater than 5") 
else: 
print("x is not greater than 5") 


# In[36]:


#Correction : line 4th and 6th line need space at the being of the print statment
x = 5 
if x > 5: 
 print("x is greater than 5") 
else: 
 print("x is not greater than 5")


# In[39]:


#7. What will the following code print? 
x = 5 
if x > 5: 
print("x is greater than 5") 
elif x == 5: 
print("x


# In[41]:


#correction in the line 3 space being of the print statement, 6th line “ is missing and ) and print space 
#correct : 
x = 5
if x > 5:
 print("x is greater than 5")
elif x == 5:
 print("x")


# # End of Python Summer Holidays Assignment 2024 

# ## Python Code 

# In[30]:


def multiply(x, y , z):
    print("Multiply {} {} {}".format(2, 3, 4))
    result = 2 * 3 * 4
    return result
output = multiply(2, 3, 4)
print("Result:", output)


# In[32]:


def multiply(x, y):
    print("Multiply {} and {}".format(x, y))  
    result = x * y
    return result
output = Add(3, 4)
print("Result:", output)


# In[34]:


def Add(a, b, c):
    print("Add {} {} {}".format(a, b, c))  
    result = a + b + c
    return result
output = Add(367, 344, 129)
print("Result:", output)


# In[36]:


def Subtract(a, b, c):
    print("Subtract {} {} {}".format(a, b, c))  
    result = a - b - c
    return result
output = Subtract(367, 344, 129)
print("Result:", output)


# In[11]:


def Multiply(a, b, c):
    print("Multiply {} {} {}".format(a, b, c))  
    result = a * b * c
    return result
output = Multiply(367, 344, 129)
print("Result:", output)


# In[13]:


def Multiply(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
    print("Multiply {} {} {}".format(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z))  
    result = a * b * c * d * e * f * g * h * i * j * k * l * m * n * o * p * q * r * s * t * u * v * w * x * y * z
    return result
output = Multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 19, 91, 21, 12, 31, 13, 51, 15)
print("Result:", output)


# ### Define Function
# 

# In[8]:


def greet(mywish):
    print(" Hello " + mywish + "*")
greet("Aarush")
greet("Mama")
greet("Papa")


# In[10]:


def hi(Astro):
    print(" Sup " + Astro + "!")
hi("Atharv")
hi("Purav")
hi("Wynnen")


# In[11]:


print ("HelLo")


# In[13]:


def hi(Astro):
    print(" Sup " + Astro + "!")
hi("Atharv , Wynnen , and Purav")
def bye(Badminton):
    print(" Age: " + Badminton + "!")
bye("Atharv 11")
bye("Purav 13")
bye("Wynnen 10")


# In[20]:


name = input() 
age = int(input())
school = input() 
standard = int(input())
weight = float(input()) 
print("The name of the person is", name, end=' ') 
print("and the age is", age, end='. ')
print("and class in", standard, end='. ')
print("Weighs about", weight, end='. ')


# # Printing Numbers with for loop
# 

# In[28]:


# Printing numbers in a loop from 1-5
def print_numbers():
    for number in range(1,6):
        print(number)
# Calling the function
print_numbers()


# In[32]:


# Printing Fruits in Loops from a list
def print_fruits():
   fruits = ["apple", "banana","orange","grape"]
   for fruit in fruits:

    print(fruit)
# Call the function
print_fruits()


# In[33]:


# Printing Racket brands in a for loop from a list
def print_rackets():
   rackets = ["Li Ning", "Yonex", "Huncred","Victor","Oliver"]
   for rackets in rackets:

    print(rackets)
# Call the function
print_rackets()


# In[39]:


# Printing Racket brands in a for loop from a list
def print_rackets():
   rackets = ["Li Ning", "Yonex", "Huncred","Victor","Oliver"]
   for rackets in rackets:

    print(rackets)
# Call the function
print_rackets()

# Player using each brand
print("Li Ning - Chirag Shetty")
print("Yonex - Lin Dan")
print("Huncred - Lakshya Sen")
print("Victor - Victor Axelson")
print("Oliver - Kento Momata")


# In[ ]:





# In[30]:


def multiplication_table_9():
    for y in range(1,11):
        print(f"9 x {y} = {9 * y}")
multiplication_table_9()


# In[2]:


def countdown():
    for number in range(1,11):
       print(number)
countdown()


# In[47]:


def reverscountdown():
    for number in reversed(range(1,11)):
       print(number)
reverscountdown()


# ## Question 4

# In[3]:


def greet(name="Best Friend"):
  print("Hello, " + name + "!")

greet()
greet("Parents")
  


# ## Question 5
# 

# In[21]:


import random

def guess_the_number():
  secret_number=random.randint(1,12)
  guess=int(input("Guess the number beetween 1 and 12: "))
    
  if guess==secret_number:
     print("You got it right , Buddy") 
  else:
     print("Buddy , how hard was it to guess the right number!")
        
guess_the_number()


# ## Add a own Function to Question 5

# In[ ]:


import random

def guess_the_number():
  secret_number=random.randint(1,12)
  guess=int(input("Guess the number beetween 1 and 12: "))
    
  if guess==secret_number:
     print("You got it right , Buddy") 
  else:
     print("Buddy , how hard was it to guess the right number!")
     print("The secret number was :  ") 
     print(secret_number)
    
guess_the_number() 


# ## Question 6

# In[11]:


def print_table(number):
    for x in range(1, 12):
      print(number, "x",x,"=",number*x)
    
print_table(4)    


# # Finding Prime Numbers

# In[79]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True   


# In[77]:


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False       
    return True


# # Prime number upto
# 

# In[80]:


def print_primes_up_to(n):
    for num in range(2, n+1):
        if is_prime(num):
            print(num, "is a prime number")

print_primes_up_to(20) 


# # Multiplication Table

# In[47]:


def print_multiplication_table(number, up_to):
    for i in range(1, up_to + 1):
     print(f"{number} x {i} = {number * i}")

print_multiplication_table(5, 12)


# # Calculate Factorial

# In[37]:


def calculate_factorial(number):
 factorial = 1
 for i in range(1, number + 1):
   factorial *= i
 return factorial 

print("Factorial of 5 is", calculate_factorial(5))


# # Fibonacci Sequence

# In[71]:


def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci_sequence(10)


# #  Scheduling Based on Conditions

# In[1]:


def schedule(day):
    day = day.lower()
    if day in ["monday", "wednesday", "friday"]:
        print(f"{day.title()}: Math class")
    elif day in ["tuesday", "thursday"]:
        print(f"{day.title()}: Science class")
    else:
        print(f"{day.title()}: Chill time")

schedule("Monday")
schedule("Saturday")


# In[7]:


def schedule(day): 
    day = day.lower()
    if day in ["monday", "wednesday", "friday"]:
        print(f"{day.title()}: Smashminton time")
    elif day in ["saturday","sunday"]:
        print(f"{day.title()}: Tournament")
    else:
        print(f"{day.title()}: Chillax")
        
schedule("Monday")
schedule("Tuesday")
schedule("Wednesday")
schedule("Thursday")
schedule("Friday")
schedule("Saturday")
schedule("Sunday")


# In[2]:


def custom_schedule():
    day=input("Enter a day of the week:").lower()
    
print(schedule(monday))

custom_schedule()  


# In[ ]:


def homework_timetable(day):
    day = day.lower()
    if day in ["monday","wednesday","fiday"]
        print(f"{day.title()}:Do English homework!")
    elif day in ["tuesday", "thursday"]:
        print(f"{day.title()}: Do Maths homework!")
    elif day =="saturday":
        print(f"{day.title()}: Study for Exam, there is no home work  today!")
    elif day =="sunday":
        print(f"{day.title()}: Relax, there is no work today!")
    else:
        print(f"{day.title()}: There is no day like that!")
        
homework_timetable("monday")


# # Dictionary

# In[4]:


# Dictionary is like a real life dictionary where you look up a word
homework_dict = {
    "Math": "Practice for KP",
    "Science": "Do an experiment about dustparticles",
    "Physics": "Caluclate the speed of your bedroom light",
    "Chemistry": "Dip a carrot into liquid nitrogen",
    "Biology": "Learn about Venus Fly Trap"
    "History": "Explain why Adolf Hitler killed himself"
    "Geography": "Give the exponents of Hawai on the world map"
    "English": "Practice for KP"
    "Music": "Compose your own Music"
    "French": "Learn the verb form etre"
    "Sport": "Play Badminton"
    "Art": "Complete Picasso Mindmap"
    "Badminton": "Go to Tagestraining of Tobias in the TSG Halle"
    "Abacus": "Practice the decimal division"
    "Swimming": "Swim 100 metres freestyle"
    "TD": "Check oponents for next Tournament"

def do_homework(subject):
    subject = subject.title()
    if subject in  homework_dict:
        print(f"Homework for {subject}: {homework_dict[subject]}")
        
do_homework("Chemistry")


# # Homework Of Wedding
# 

# In[8]:





# In[ ]:


#1. What is the purpose of an if statement?
Options:
(a) To repeat code
(b) To make decisions
(c) To create a list
(d) To write functions
Hint: It's used to make decisions.
    Answer : B


# In[8]:


#2. Write an if statement to print 'Welcome!' if age is greater than or equal to 18.
#Hint: Use `if age >= 18:`.
age = int(input('Please enter a persons age.'))
if age >= 18: print('Welcome to adult.')
else: print ('The person is not a adult.')


# In[6]:


#3. What will this code output?
x = 10
if x < 5:
 print("Small")
elif x == 10:
 print("Equal")
else:
 print("Large")
#Options:
#(a) Small
#(b) Equal
#(c) Large
#(d) Error
#Hint: Check the `elif` block.


# In[1]:


#4. Create an if-else statement to print 'Even' if a number is even and 'Odd' if it's not.
#Hint: Use `if num % 2 == 0:`.
num = int(input('Please enter a digit.'))
if num % 2 == 0:
 print("number is even")
else: print ('number is odd')


# In[13]:


#5. What is the output of the following code?
num = 15
if num > 10:
 print("Above 10")
if num > 5:
 print("Above 5")
else:
 print("5 or less")

#Options:
#(a) Above 10
#(b) Above 5
#(c) Above 10\nAbove 5 -- Answer is C
#(d) 5 or less
#Hint: Each if statement runs separately.


# ## Section 2: Loops (for, while)

# In[14]:


#6. Write a for loop to print numbers from 1 to 10.
#Hint: Use `range(1, 11)`.
for i in range(1, 11):
    print(i)


# In[16]:


#7. What will the output be for this code?
for i in range(4):
 print(i * 2)
#Options:
#(a) 0 2 4 6 -- Answer 
#(b) 2 4 6 8
#(c) 0 1 2 3
#(d) Error
#Hint: Multiply each number in the range by 2.


# In[17]:


#8. Write a while loop that prints 'Python' 5 times.
#Hint: Use a counter variable and `while counter < 5:`.
a=input("Enter your name:")
b=1
while b<=5:
    print(a) 
    b=b+1


# In[ ]:


#9. What is the difference between a for loop and a while loop?
#Options:(b)
#(a) for loops run indefinitely, while loops do not
#(b) for loops are for fixed iterations, while loops run until a condition is met -- 
#(c) Both are the same
#(d) for loops are used for lists only
#Hint: Think about how each loop runs.


# In[ ]:


# 10. What does `break` do inside a loop?
#Options:(b)
#(a) Skips the current iteration
#(b) Stops the loop completely
#(c) Starts the loop over
#(d) Ends the program
#Hint: It exits the loop.


# ## Section 3: Lists and Tuples

# In[4]:


#11. Create a list of 5 fruits and print the second fruit.
#Hint: Use `print(fruits[1])`.
fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
print("List of Fruits are", fruits) 
print("Second Fruit is",fruits[1])


# In[ ]:


#12. How do you add an item to a list?
#Options: B
#(a) `list.add(item)`
#(b) `list.append(item)`
#(c) `list.insert(item)`
#(d) `list.put(item)`
#Hint: Use the `append()` method.


# In[22]:


#13. What will this code output?
my_list = [10, 20, 30, 40]
print(my_list[2])
#Options: C
#(a) 10
#(b) 20
#(c) 30  --
#(d) 40
#Hint: Indexing starts from 0.


# In[24]:


#14. Write a program to remove the last item from a list.
#Hint: Use `list.pop()`.
fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
print("List of Fruits are", fruits) 
return_value = fruits.pop(4)
print('Return Value:', return_value)


# In[6]:


#15. What is the difference between a tuple and a list?
#Options: B
#(a) Tuples are mutable; lists are immutable
#(b) Lists are mutable; tuples are immutable
#(c) Both are mutable
#(d) Both are immutable
#Hint: Tuples cannot be changed after creation
# Answer is B


# # #Section 4: Dictionaries

# In[50]:


#16. Create a dictionary with keys 'name', 'age', and 'hobby'.
#Hint: Use `{}` with key-value pairs.
my_dict = {"name": "Aarush", "age": 10,}
my_dict["hobby"] = "Badminton"
print(my_dict)  


# In[54]:


#17. How do you access the value of 'name' in `my_dict = {'name': 'Alice', 'age': 12}`?
#Options:D
#(a) `my_dict.get('name')`
#(b) `my_dict.name`
#(c) `my_dict['name']`
#(d) Both (a) and (c)  
#Hint: Access with square brackets or `get()`.
my_dict = {'name': 'alice', 'age': 12}
#my_dict.get('name')
#my_dict['name']


# In[ ]:


#18 . What will `my_dict['age'] = 13` do?
Options:B
(a) Add a new key
(b) Change the value of 'age' to 13
(c) Remove 'age'
(d) Return an error
Hint: Updates the value for an existing key.


# In[59]:


#19. Write a loop to print all keys in `my_dict`.
#Hint: Use `for key in my_dict:`.

my_dict = {
   'Name': 'Aarush',
   'year': '2013',
   'School': 'JSS',
   'hobby': 'Badminton'
}

print(my_dict.keys())
print(my_dict.items()) #For 20th Question


# In[58]:


get_ipython().run_line_magic('pinfo', 'return')
Options: C
(a) A list of keys
(b) A list of values
(c) A list of key-value pairs
(d) An error
Hint: It shows key-value pairs.


# # # Section 5: Problem Solving

# In[62]:


#21. Write a program to count the number of even numbers in a list.
#Hint: Use a loop with `if num % 2 == 0:`.
# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 1]
 
even_count, odd_count = 0, 0
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
 
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


# In[9]:


#22. Create a list of numbers from 1 to 20 and use a loop to print only numbers divisible by 3.
#Hint: Use `range()` and `if num % 3 == 0:`.

for num in range(1,21): # Numbers between 1 to 20
    if num % 3 == 0:  # If num is divisible by 3 ,then print it
      print(num)


# In[77]:


#23. Create a dictionary to store names and their favorite colors. Print each name with their color.
#Hint: Use a loop with `for name, color in fav_colors.items():`.
fav_colors = {
    "Varun": "blue",
    "Aarush": "red",
    "Swapna": "Blue"
}

for name, color in fav_colors.items():
    print(name + " favorite color is " + color + ".")


# In[1]:


#24. Write a program that takes a number input and prints 'Positive', 'Negative', or 'Zero'.
#Hint: Use if-elif-else.

number = float(input("Enter a number: "))
# Check if the number is positive, negative, or zero
if number > 0:
  print("Positive")
elif number < 0:
  print("Negative")
else:
  print("Zero")


# In[ ]:


#25. What will `for i in range(1, 10, 2): print(i)` print?
Options:B
(a) 1 2 3 4 5 6 7 8 9
(b) 1 3 5 7 9
(c) 2 4 6 8 10
(d) None
Hint: The third argument in `range()` is the step.


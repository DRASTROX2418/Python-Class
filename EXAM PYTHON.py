#!/usr/bin/env python
# coding: utf-8

# ## List

# In[7]:


# A list in Python is a way to store many values in one place
Aarush_Bag = ["Laptop","Pencil Case","Mouse","Spinner"]

print(Aarush_Bag)


# In[9]:


Aarush_Bag = ["Laptop","Pencil Case","Mouse","Spinner"]

print(Aarush_Bag[2])


# In[10]:


Aarush_Bag = ["Laptop","Pencil Case","Mouse","Spinner"]

if "Juice" in Aarush_Bag:
    print("Yes it is in his Bag")
    
else:
    print("No it is not in his Bag")


# In[19]:


Students = ["Aarush","Arnav","Adhitya","Liam"]
Present = ["Aarush","Arnav"]
Absent = ["Adhitya","Liam"]

if "Liam" in Present:
    print("He is a GOOD BOY")
    
if "Liam" in Absent:
    print("He is a BAD BOY")


# In[35]:


Students = ["Aarush","Arnav","Adhitya","Liam"]

for Liam in Students:
    print("He is absent")
    


# ##  Tuples
# 

# In[2]:


# Use Tuple when data should not change
Pancakes = ("Eier","Weizmehl","Banana","Chocosyrup")

print(Pancakes)


# ## Dictionary

# 
# Student_ID = {"Name": "Aarush",
#               "Age": 12,
#               "Class": 7
#              }
# 
# print(Student_ID)

# In[43]:


A LIST CAN CHANGE 
A TUPLE CANNOT
A DICTIONARY EXPLAINS


# # Topic...........Keyword.............Memory Trick

# In[1]:


Loop           for and while              repeat
Condition       if                        decide
Function       def                        make your own tool


# In[ ]:





# In[9]:


student = {
    "name": "Aarush",
    "marks": [80, 75, 90]
}

total = 0
for m in student["marks"]:
    total += m

avg = total / len(student["marks"])

if avg >= 80:
    print("Excellent!")
else:
    print("Good, keep practicing!")


# In[2]:


light = "red" 

if light == "red":
     print("STOP")
elif light == "yellow":
     print("Wait")
else:
    print("GO")


# In[16]:


temperature =input("Enter temp:")
+print(type(temperature))  #Class 'str'

temperature = int(temperature)
print(type(temperature)) # Class 'int'

if temperature >= 0 and temperature <= 10:
    print("AVERAGE GERMANY")
elif temperature >= -10 and temperature < 0:
    print("TOO COLD LETS GRIND FN")
elif temperature > 10 and temperature <= 30:
    print("GOOD DAY TO GO WALK")
elif temperature > 30 and temperature < 100:
    print("PERFECT DAY TO RELAX OUTSIDE")
elif temperature > 100 and temperature < 1000:
    print("BRING A EGG WITH YOU")
else:
    print("LETS HANG OUTSIDE")


# # Type of Datatype

# In[2]:


value = 7.0
print(type(value))


age = int(input("Enter age: "))
print(age + 5)   # 


#temperature checker 
temp = float(input("Enter temperature: "))
if temp < 0:
    print("Freezing ❄️")
else:
    print("Okay 🌤️")


# In[9]:


#Score_1 = int(input("Scored by Messi:"))
#Score_2 = int(input("Scored by Ronaldo:"))

#info
messi_goals = 1
messi_matches = 1000

ronaldo_goals = 1001
ronaldo_matches = 1000

messi_avg = messi_goals/messi_matches
ronaldo_avg = ronaldo_goals/ronaldo_matches

print("Messi average is:", messi_avg)
print("Ronaldo average is:", ronaldo_avg)

#accuracy
messi_accuracy = (messi_goals/messi_matches)*100
ronaldo_accuracy = (ronaldo_goals/ronaldo_matches)*100

print("Messi accuracy is:", messi_accuracy)
print("Ronaldo accuracy is:", ronaldo_accuracy)


# In[2]:


distance = float(input("Enter distance in meters: "))
time = float(input("Enter time in seconds: "))


speed = distance /time

print ("Distance =", distance, "meters")
print("Time =", time, "seconds")


# In[7]:


import matplotlib.pyplot as plt
distance = float(input("Enter distance in meters: "))
time = float(input("Enter time in seconds: "))
time_values= [0,time]
distance_values= [0,distance]

speed = distance /time

print ("Distance =", distance, "meters")
print("Time =", time, "seconds")
print("Speed is:", speed, "m/sec")

plt.plot(time_values, distance_values, marker = 'o')
plt.xlabel("Time (Seconds)")
plt.ylabel("Distance (Meters)")
plt.title("Distance - Time Graph")

plt.grid(True)
plt.show()


# # 

# In[3]:


#Concatinate means joining two datatypes together 

Aarush = "Hello"
Arnav = "World"
print(Aarush+" "+Arnav) #String concatenation


# In[4]:


#Concatenate integers? No it is not Concatenation this is addition

#Data
#1. String + String           -Yes we can concatenate with +
#2. Integer + Integer         -No this is addition
#3. String + Integer          -No
#4. String + String(Integer)  -Yes
#5. print("text,int")         -Yes


# In[5]:


# Concatenate examples

name = "Aarush"
score = 19
#print(type(score))
print(name,"scored" , str(score))


# # Attendance Checker

# In[2]:


# Total school days in a year = 188
# Sick days = some number -> Caluculate days you have attended, percentage and good or poor

total_days = 188
sick_days = int(input("Enter number of sick days in the year:"))
skipped_days = int(input("Enter number of skipped days in the year:"))
attended_days = total_days - sick_days - skipped_days

attendance_percent = (attended_days/total_days)*100

print("sick days taken:", sick_days)
print("Days attended:", attended_days)
print("Attendance %:", round(attendance_percent,2),"%")

if attendance_percent >= 75:
    print("Attendance status: GOOD!")

else:
    print("Attendance status: POOR!")


# In[11]:


target_steps = int(input("Enter your Target:"))
steps_today = int(input("Enter number of steps in a day:"))
step_percent = (steps_today / target_steps)*100 
 
print("Your target was:", target_steps)
print("You walked ", steps_today,"steps.")
print("Steps walked in %:", round(step_percent,2),"%")

if step_percent <= 500 and >= 4999:
    print("Please complete your goal and thank me later🙄 ")

elif step_percent >= 5000 and <= 9000:
    print("You could have walked a few more minutes🤪")
    
elif step_percent >= 9001 and <= 9999:
    print("You tried so hard 😤")
    
elif step_percent <= 10000:
    print("You completed your goal 🎉")

else:
    print("You are too lazy 🩴")


# In[2]:


a = "10"
b = "5"
print(a+b)


# In[5]:


temp = ("36.5")
print(float(temp) +1)


# In[8]:


score = 95 
print("Your score is " + str(score))


# In[10]:


x = input("Enter something:")
print(type(x))


# In[16]:


a = input("enter number:")
b = 20.5
print(int(a)+b)


# In[17]:


num = int(3.5)
print(num)


# In[18]:


num = float(3.5)
print(num)


# In[19]:


x = input("enter number:")
print(x*3)


# In[1]:


x = input("enter number:")
y = 20 
print(int(x) + y)


# In[23]:


# Age , Temperature , Name , Price (99.99)\

# int ---> whole number
# float ---> when decimals are possible
# str ---> join in or textmessages


# # If inside If

# In[ ]:


marks = int(input("Enter your marks:"))
if marks >= 50:
    if marks >= 90:
        print("Excellent")
        
    else:
        print("Good Job")
        
else:
    print("Fail")


# In[3]:


points = int(input("Enter your points:"))
if points >= 15:
    if points >= 20:
        print("Excellent")
        
    else:
        print("Good Job")
        
else:
    print("Fail")


# In[ ]:





# In[2]:


homework_done = True 
weekend = False

if homework_done or weekend:
    print("Netflix")
else:
    print("No Netflix")


# In[4]:


has_ticket = False
is_vip = True 

if has_ticket or is_vip:
    print("Permit")
else:
    print("Stop")


# In[ ]:


password = "python"
guess = 3

while guess > 0:
    user_input = input("Enter password:")
    
    if user_input == password:
        print("Access granted")
        break
    else:
        guess -= 1
        print("Wrong password")
        print("Attempts left:", guess)
        
if guess == 0:
    print("System locked")


# In[2]:


def login_system(password, max_attempts=3):
    attempts = max_attempts
    
    while attempts > 0:
        user_input = input("Enter password:")
        
        if user_input == password:
            return "Access granted"
        
        attempts -= 1
    return"System locked"
   
print(login_system("python"))


# In[6]:


def login_system(password, max_attempts=3):
    attempts = max_attempts
    
    while attempts > 0:
        user_input = input("Enter password:")
        
        if user_input == password:
            change = input("Do you want to change password (yes/no)") 
        return "Access granted"
        if change.lower() == "yes":
            new_password = input("Enter new password:")
            print("Password changed successfully")
            return new_password
        
        attempts -= 1
    return"System locked"
   
print(login_system("python"))


# # Simple Function Example

# In[6]:


def square(num):
    return num*num

result = square(6)
print("Square is", result )


# In[7]:


def cube(num):
    return num*num*num

result = cube(4)
print("Cube is", result )


# In[12]:


def multiply(a,b):
    return a*b

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

print(multiply(4,17))
print(add(4,17))
print(subtract(4,17))


# In[19]:


def is_pallindrome(word):
    return word == word[::-1]

word = input("Enter a word  ")

if is_pallindrome:
    print("Is a pallindrome")
    
else:
    print("Not a pallindrome")
    


# In[6]:


def is_pallindrome(word):
    word = word.lower()
    reversed_word = ""
    for sh in word:
        reversed_word = sh + reversed_word
        
    return word == reversed_word

word = input("Enter Word")

if is_pallindrome(word):
    print("Yes")
else:
    print("Nope")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


1+1


# In[3]:


2+2


# In[4]:


3+3


# #### 

# In[5]:


4+4


# 5+5

# # Line of Numbers

# In[6]:


print("Hello Everyone ")


# ### I HAVE TWO GLASSES OF WATER I DRINK EACH THIRTY MINUTES HOW MANY GLASSES OF WATER DO I DRINK IN TWENTYFOUR HOURS

# In[1]:


# Number of minutes in 24 hours 
minutes_in_a_day = 24 * 60 


# In[2]:


# Interval in which you drink a glass of water 
interval_minutes = 30


# In[7]:


# Calucalate the total number of glasses of water you would drink in 24 hours
total_glasses = minutes_in_a_day 


# ## Data Types
# Int

# In[ ]:





# In[1]:


# Assigning a integer value to a variable 
How_many_tournaments= 100
#Printing the value of the variable
print("I have played",How_many_tournaments,"tournaments")


# # Float 

# In[2]:


# Floats are numbers that have decimals . They are used for measurments involving fraction 


# In[7]:


#Step:1 Assigning a float value to a variable 
height_cm = 200.11
#Step:2 Printing the value of the variable
print("Tallest guy is",height_cm,"cm tall")


# # Complex

# In[9]:


# complex numbers have a real part and a imaginary part . They are used in advanced mathematical caluclations

# Step1: Assigning a complex value to a variable 
complex_num = 4 + 10j

#Step2: Printing the value of the variable
print("The complex num is" , complex_num)


# In[1]:


https://teams.live.com/l/message/19:meeting_MmZhMDAxODgtOTAxNi00OWEwLTljOTQtYjQ1NTk3ZjU1YzNk@thread.v2/1713001014106?context=%7B%22contextType%22%3A%22chat%22%7D


# In[2]:


https://teams.live.com/l/message/19:meeting_MmZhMDAxODgtOTAxNi00OWEwLTljOTQtYjQ1NTk3ZjU1YzNk@thread.v2/1713001014106?context=%7B%22contextType%22%3A%22chat%22%7D


# In[3]:


https://teams.live.com/l/message/19:meeting_MmZhMDAxODgtOTAxNi00OWEwLTljOTQtYjQ1NTk3ZjU1YzNk@thread.v2/1713001014106?context=%7B%22contextType%22%3A%22chat%22%7D


# Guess the Animal Game

# # In this game, the computer will randomly  select an animal from a list
# # The player will have three chances to guess the animal.After each guess 
# # the game will provide a hint about the animal's charecteristics.

# In[ ]:





# In[5]:


import random 

# Function to play the Guess the Animal Game
def guess_the_animal():
    # List of animals
    animals = ["Tiger","Lion","Monkey","Gorilla","Cheetah","Pig","Aarush"]
    
    # Generate a random animal
    secret_animal = random.choice(animals)
    
    # Initialize the number of attempts 
    attempts = 0 
    
    # Game instructions 
    print("Welcome to guess the Animal Game!")
    print("You have 3 chances to guess the secret animal.")
    
    # Game loop
    while attempts <3:
        # Get 
        # Provide hint 
        if guess < secret_animal:
            print("The secret animal is alphabetically higher than your guess.")
        else:
            print("The secret animal is alphabetically lower than your guess.")
            
            # Check if the player ha s attempts left 
            if attempts < 3:
                print("Try Again")
            
            # If all attempts are used and the animal is not guessed
            
            if attempts == 3:
                print("Sorry you have used all your attempts.The secret animal was", secret_animal )
                
                
 # start the game
guess_the_animal()    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


Astro_int=11-1
print ("I have subtracted 1 from the Astro integer:",Astro_int)


# In[18]:


# Binary (Base 2)
binary_int = 0b1010 # Prefix 0b indicates binary
print("Binary Integer:", binary_int)


# In[26]:


# Octal (Base 8)
octal_int = 0o222 # Prefix 0o indicates octal
print("Octal Integer:", octal_int)


# In[9]:


# Hexadecimal (Base 16)
hexadecimal_int = 0x155 # Prefix 0x indicates hexadecimal
print("Hexadecimal Integer:", hexadecimal_int)


# In[ ]:


import tkinter as tk

def display_color(hex_color):
    root = tk.Tk()
    root.geometry("100x100")
    color_label = tk.Label(root, bg=hex_color, width=20, height=10)
    color_label.pack()
    root.mainloop()

# Input a hexadecimal color code
hex_color = input("Enter a hexadecimal color code (e.g., #FF0000 for red): ")

# Display the color
display_color(hex_color)
cgq-jopp-btg


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import tkinter as tk

def display_color(hex_color):
    root = tk.Tk()
    root.geometry("100x100")
    color_label = tk.Label(root, bg=hex_color, width=20, height=10)
    color_label.pack()
    root.mainloop()

# Input a hexadecimal color code
hex_color = input("Enter a hexadecimal color code (e.g., #FF0000 for red): ")

# Display the color
display_color(hex_color)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


import tkinter as tk

def display_color(hex_color):
    root = tk.Tk()
    root.geometry("100x100")
    color_label = tk.Label(root, bg=hex_color, width=20, height=10)
    color_label.pack()
    root.mainloop()

# Input a hexadecimal color code
hex_color = input("Enter a hexadecimal color code (e.g., #FF0000 for red): ")

# Display the color
display_color(hex_color)


# # 18 May 2024

# #### Create Bio Data

# In[ ]:


def generate_bio_data(): 
    #Ask for user inputs
    Name = input("Enter your Name:")
    Country_born = input("Enter the Country you were born in:")
    Age = int(input ("Enter your age:"))
    School = input("In which school are you studying:")
    Studying = input("In which grade are you studying:")
    Location = input("Enter you current location of which country you live")
    Hobbies = input("Enter your hobbies (seperated by commas):").split(',')
    
    #create a dictionary to store bio-data
    bio_data = {
        "Name" : Name,
        "Country born" : Country_born,
        "Age" : Age,
        "School" : School,
        "Studying" : Studying,
        "Location" : Location,
        "Hobbies" : [hobby.stript() for hobby in hobbies], # Strip any extra spaces
        
    }
    
    return bio_data

# Generate and display bio_data
bio_data = generate_bio_data()

#Display bio-data in a nicely formated way
print("\nBio-Data of User")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
for key, value in bio_data.items():
    if isinstance(value, list):
        value = ','.join(value)
    print(f"{key}: {value}" )    
    
        


# In[3]:


def generate_bio_data(): 
    #Ask for user inputs
    Name = input("Enter your Name:")
    Country_born = input("Enter the Country you were born in:")
    Age = int(input ("Enter your age:"))
    School = input("In which standard are you studying:")
    Studying = input("In which grade are you studying:")
    Location = input("Enter you current location of which country you live")
    Hobbies = input("Enter your hobbies (seperated by commas):").split(',')
    
    #create a dictionary to store bio-data
    bio_data = {
        "Name" : Name,
        "Country born" : Country_born,
        "Age" : Age,
        "School" : School,
        "Studying" : Studying,
        "Location" : Location,
        "Hobbies" : [hobby.stript() for hobby in hobbies], # Strip any extra spaces
        
    }
    
    return bio_data

# Generate and display bio_data
bio_data = generate_bio_data()

#Display bio-data in a nicely formated way
print("\nBio-Data of User")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
for key, value in bio_data.items():
    if isinstance(value, list):
        value = ','.join(value)
    print(f"{key}: {value}" )    
    


# In[ ]:





# In[ ]:





# In[ ]:


def generate_bio_data():
    #Ask for user inputs
    name = input("Enter your Name:")
    Country_born = input("Enter your country of Origin:")
    age = int(input("Enter your Age:"))
    school = input("Enter the name of your School:")
    Studying = input("In which standard are you Studying:")
    location = input("Enter the location where you currently live:")
    hobbies = input("Enter your hobbies (separated by commas):").split(',')
    
    #create a dictionary to store bio-data 
    bio_data = {
        "Name" : name,
        "Country Born": Country_born,
        "Age": age,
        "School": school,
        "Studying": Studying,
        "Location": location,
        "Hobbies" : [hobby.strip() for hobby in hobbies], # Strip any extra spaces
        
    }
    
    return bio_data

# Generate and display bio-data
bio_data = generate_bio_data()

#Display bio-data in a nicely formatted way

print("\nBio-Data of User")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
for key, value in bio_data.items():
    if isinstance(value, list):
        value = ','.join(value)
    print(f"{key}: {value}" )
    


# In[1]:


import random

class ChildBioData:
    def _init_(self):
        self.name = ""
        self.country_born = ""
        self.age = 0
        self.school = ""
        self.studying_studied = ""
        self.location = ""
        self.hobbies = []

    def input_data(self):
        self.name = input("Enter the child's name: ")
        self.country_born = input("Enter the country where the child was born: ")
        self.age = int(input("Enter the child's age: "))
        self.school = input("Enter the name of the child's school: ")
        self.studying_studied = input("Is the child currently studying or studied? (Enter 'studying' or 'studied'): ")
        self.location = input("Enter the location where the child currently lives: ")
        hobbies = input("Enter the child's hobbies (separated by commas): ").split(',')
        self.hobbies = [hobby.strip() for hobby in hobbies]  # Strip any extra spaces

    def display_data(self):
        print("\nBio-Data of the Child")
        print("---------------------")
        print(f"Name: {self.name}")
        print(f"Country Born: {self.country_born}")
        print(f"Age: {self.age}")
        print(f"School: {self.school}")
        print(f"Studying/Studied: {self.studying_studied}")
        print(f"Location: {self.location}")
        print(f"Hobbies: {', '.join(self.hobbies)}")

def create_group_bio_data(num_children):
    children = []
    for _ in range(num_children):
        child = ChildBioData()
        child.input_data()
        children.append(child)
    return children

def display_group_bio_data(children):
    print("\nGroup Bio-Data of Children")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    for i, child in enumerate(children, start=1):
        print(f"\nChild {i}")
        child.display_data()

children = 6 = int(input("How many children's bio-data would you like to create? "))
children = create_group_bio_data(num_children)
display_group_bio_data(children)


# 

# In[ ]:





# In[ ]:





# 

# In[1]:


import random

class ChildBioData:
    def _init_(self):
        self.name = ""
        self.country_born = ""
        self.age = 0
        self.school = ""
        self.studying_studied = ""
        self.location = ""
        self.hobbies = []

    def input_data(self):
        self.name = input("Enter the child's name: ")
        self.country_born = input("Enter the country where the child was born: ")
        self.age = int(input("Enter the child's age: "))
        self.school = input("Enter the name of the child's school: ")
        self.studying_studied = input("Is the child currently studying or studied? (Enter 'studying' or 'studied'): ")
        self.location = input("Enter the location where the child currently lives: ")
        hobbies = input("Enter the child's hobbies (separated by commas): ").split(',')
        self.hobbies = [hobby.strip() for hobby in hobbies]  # Strip any extra spaces

    def display_data(self):
        print("\nBio-Data of the Child")
        print("---------------------")
        print(f"Name: {self.name}")
        print(f"Country Born: {self.country_born}")
        print(f"Age: {self.age}")
        print(f"School: {self.school}")
        print(f"Studying/Studied: {self.studying_studied}")
        print(f"Location: {self.location}")
        print(f"Hobbies: {', '.join(self.hobbies)}")

def create_group_bio_data(num_children):
    children = []
    for _ in range(num_children):
        child = ChildBioData()
        child.input_data()
        children.append(child)
    return children

def display_group_bio_data(children):
    print("\nGroup Bio-Data of Children")
    print("-------------------------")
    for i, child in enumerate(children, start=1):
        print(f"\nChild {i}")
        child.display_data()

# Function to filter and display children from India
def filter_and_display_by_country(children, country):
    filtered_children = [child for child in children if child.country_born.lower() == country.lower()]
    if filtered_children:
        print(f"\nChildren from {country}")
        print("-------------------------")
        for i, child in enumerate(filtered_children, start=1):
            print(f"\nChild {i}")
            child.display_data()
    else:
        print(f"\nNo children from {country} found.")

# Fun task: Create and display bio-data for a group of children
num_children = int(input("How many children's bio-data would you like to create? "))
children = create_group_bio_data(num_children)
display_group_bio_data(children)

# Filter and display children from India
filter_and_display_by_country(children, "India")


# In[2]:


import matplotlib.pyplot as plt 
from collections import Counter

#Generate Superhero Bio-Data
superheroes = [
    {"name": "Aarush", "age": 11, "powers": ["Undestructable Astronaut Suit", "Flying", "Fast as Light"],
    "affilation": "Avengeres"},
    {"name": "Atharv", "age": 12, "powers": ["Undestructable Astronaut Suit", "Flying", "Fast as Light"],
    "affilation": "Avengeres"},
    {"name": "Arnav", "age": 12, "powers": ["Undestructable Dance", "Flying", "Fast as Light"],
    "affilation": "Avengeres"},
]

#Visualize Superhero Powers 
all_powers = [power for hero in superheroes for power in hero["powers"]]
power_counts = Counter(all_powers)

# Plotting
plt.figure(figsize=(11,5))
plt.barh(list(power_counts.keys()), list(power_counts.values()), color='skyblue')
plt.xlabel('Number of Superheroes')
plt.ylabel('Powers')
plt.title('Distribution of Superhero Powers')
plt.show()

# Customizing colors
colors = ['red','blue', 'green', 'orange', 'purple']
plt.barh(list(power_counts.keys()), list(power_counts.values()), color=colors)

# Fun Task 2

# Extracting names and ages
names = [hero["name"]for hero in superheroes]
ages =  [hero["age"]for hero in superheroes]

#Plotting ages
plt.figure(figsize=(10,6))
plt.plot(names, ages, marker='*', linestyle='-',color='b')
plt.xlabel('Superheroes')
plt.ylabel('ages')
plt.title('Comparision of Superhero ages')
plt.grid(True)
plt.show()


# In[1]:


print("hi")


# 

# ### Turtle Dyna

# In[18]:


import turtle
import random

# Set up Screen

wn = turtle.Screen
wn.title("Catch the turtle game")
wn.setup(width=880, height=600) 

# Create the turtle

catch_turtle = turtle.Turtle()
catch_turtle.shape("turtle")
catch_turtle.color("red")
catch_turtle.penup()
catch_turtle.speed(0)

# Define the function to move turtle
def move_turtle():
    x = random.randint(-390,390)
    y = random.randint(-290,290)
    catch_turtle.goto(x,y)
    
# Define the function to catch the turtle 
def catch(x,y):
    move_turtle()
    print("Hey , you caught the Turtle! Sike!")

# Set turtle to respond to respond clicks
catch_turtle.onclick(catch)

# Initial move 
move_turtle()

# I will keep the windows open 
wn.mainloop()


# In[20]:


import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Catch the Turtle Game")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)

# Create the turtle
catch_turtle = turtle.Turtle()
catch_turtle.shape("turtle")
catch_turtle.color("green")
catch_turtle.penup()
catch_turtle.speed(0)

# Define the function to move the turtle to a random location
def move_turtle():
    x = random.randint(-390, 390)
    y = random.randint(-290, 290)
    catch_turtle.goto(x, y)

# Define the function to catch the turtle
def catch(x, y):
    move_turtle()
    print("You caught the turtle! Sike")

# Set the turtle to respond to clicks
catch_turtle.onclick(catch)

# Initial move
move_turtle()

# Keep the window open
wn.mainloop()


# In[17]:


import tiger
import random

# Set up the screen
wn = tiger.Screen()
wn.title("Catch the Roar!!!")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Create the tiger
catch_tiger = tiger.Tiger()
catch_tiger.shape("tiger")
catch_tiger.color("orange")
catch_tiger.penup()
catch_tiger.speed(0)

# Define the function to move the tiger to a random location
def move_tiger():
    x = random.randint(-390, 390)
    y = random.randint(-290, 290)
    catch_tiger.goto(x, y)

# Define the function to catch the tiger
def catch(x, y):
    move_tiger()
    print("You caught the Tiger!")

# Set the tiger to respond to clicks
catch_tiger.onclick(catch)

# Initial move
move_tiger()

# Keep the window open
wn.mainloop()


# In[15]:


# Create Scoreboard

import random

scoreboard = {
    "Aarush":0,
    "Atharv":0
             }
# Simulate the match

def simulate_match():
    scoreboard["Aarush"] = random.randint(20,21) # Random score beetween 0 and 21
    scoreboard["Atharv"] = random.randint(0,19) # Random score beetween 0 and 21
#simulate_match()

# Caluculate the probability

def calculate_probability(scoreboard): 
    aarush_score =scoreboard["Aarush"]
    atharv_score =scoreboard["Atharv"]
    
    if aarush_score > atharv_score:
        probability = 0.51 #Higher probability of winning 
  
    else:
        probability = 0.49 #Lower probability of winning 
        
    return probability

# Calacalate the winning probability 
winning_probability = calculate_probability(scoreboard)
    
#Display the scoreboard and winning probability
print("scoreboard")
print(f"Aarush:{scoreboard['Aarush']}")
print(f"Atharv:{scoreboard['Atharv']}")


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





# In[3]:


### Print a welcome message
print("Welcome to the Haunted Mansion!")
print("You are a distnt family member of a rich millionare who has just passed away, leaving this mansion to you")
print("As the newfound owner, you decide to pay a visit to the mansion.")
print("The house is dated, creaky, and falling appart. You walk in the front door.")
print("Do you want to enter the living room or the dining room?")

### Prompt user for a choice
roomChoice = input("> ")

if(roomChoice == "living room"):
    print("You entered the living room.")
    print("As you walk in, you see a sleeping pitbull guarding some gold jewelry")
    print("Do you want to steal the jewelry from the pitbull?")
    
    pitBullChoice = input("> ")
    
    if(pitBullChoice == "yes"):
        print("You attempt to steal the jewelry, but it wakes up and rises to shreds.")
        print("You are now dead.")
    elif(pitBullChoice == "no"):
        print("You decide to not steal the dog's jewelry.")
        print("You turn around and leave the house safely.")
    else:
        print("Invalid choice. Please enter yes or no.")
elif(roomChoice == 'dining room'):
    print("You choose to go into the dining room.")
    print("As you walk in, you see a shiny vase on the table.")
    print("Do you want to open the vase?")
    
    vaseChoice = input("> ")
    
    if(vaseChoice == 'yes'):
        print("You open the vase and find a pile of bones!")
    elif(vaseChoice == 'no'):
        print("You decide not to open the shiny vase.")
        print("As you turn to leave, you hear a cracking from the corner.")
        print("A dark figure with glowing red eyes launches at you, knocking you unconcious")
        print("You wake up in your bed. It was all a dream.")
    else:()
    print("Invalid choice. Please enter yes or no.")
else:
    print("Invalid choice. Please enter living room or dining room.")


# In[ ]:





# In[1]:


#a simple Python code template to create a basic UNO game. Here's an example to get you started:


import random

# Initialize the deck with cards of different colors and values
deck = ["0 Red", "1 Red", "2 Red", "3 Red", "4 Red", "5 Red", "6 Red", "7 Red", "8 Red", "9 Red",
        "0 Blue", "1 Blue", "2 Blue", "3 Blue", "4 Blue", "5 Blue", "6 Blue", "7 Blue", "8 Blue", "9 Blue",
        "0 Green", "1 Green", "2 Green", "3 Green", "4 Green", "5 Green", "6 Green", "7 Green", "8 Green", "9 Green",
        "0 Yellow", "1 Yellow", "2 Yellow", "3 Yellow", "4 Yellow", "5 Yellow", "6 Yellow", "7 Yellow", "8 Yellow", "9 Yellow"]

# Function to deal cards to each player
def deal_cards(num_players):
    players = [[] for _ in range(num_players)]
    for _ in range(7):
        for i in range(num_players):
            card = random.choice(deck)
            players[i].append(card)
            deck.remove(card)
    return players

# Sample gameplay
num_players = 2
players = deal_cards(num_players)

# Display each player's hand
for i, player in enumerate(players):
    print(f"Player {i+1} hand: {player}")


# # Quiz
# 

# ### Total fruit consumption per kid?

# ### Plotting the total consumption of each type of fruit?

# In[17]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

#Generate Kids Bio-Data
superheroes = [
    {"name": "Alice", "fruits eaten a day": ["10 apples", "10 strawberries"],
    },
    {"name": "Ethan", "fruits eaten a day": ["10 bananas", "10 oranges"],
    },
    {"name": "Charlie",  "fruits eaten a day": ["10 bananas", "10 grapes"],
    },
    {"name": "Bob", "fruits eaten a day": ["10 grapes", "10 strawberries"],
    },
    {"name": "Daisy", "fruits eaten a day": ["10 oranges", "10 apples"],
    }

]

# Plotting
plt.figure(figsize=(11,5))
plt.barh(list(fruit_counts.keys()), list(fruit_counts.values()), color='skyblue')
plt.xlabel('Number of kids')
plt.ylabel('Fruits')
plt.title('Distribution of kids fruits')
plt.show()

# Customizing colors
colors = ['red','blue', 'green', 'orange', 'purple']
plt.barh(list(fruit_counts.keys()), list(fruit_counts.values()), color=colors)


# In[ ]:





# # Recap
# 

# ### Basic

# In[3]:


# Basic Syntax
print("Hello Aarush")


# ### Variables and Data Type 

# In[8]:


# Integer
age = 11
print(type(age))


# In[12]:


# Float 
price = 1000.00
print(type(price))


# In[13]:


# String 
name = "Sai uncle hid my ball"
print (type(name))


# In[13]:


# Boolean
Am_I_a_good_boy = True
print(type(Am_I_a_good_boy))


# In[17]:


# Operaters
sum_result = 100*10
print(sum_result)


# In[25]:


# Control Flow
x = 10 
if x>0:
    print("x is positive")
    
elif x == 0:
        print("x is zero")
        
else:
        print("x is negativ")


# In[3]:





# ### 29 Question

# In[11]:


for i in range(5):
   if i == 3:
       break
print(i)


# In[1]:


print(5==5)


# In[2]:


print(True and False)


# In[3]:


print(5 > 3 and 3 > 1)


# In[4]:


print(5 > 3 or 3 < 1)


# In[5]:


print(not (5 > 3))


# In[6]:


x = 5; x += 3; print(x)


# In[6]:


print(2+3)


# In[7]:


print(True or False)


# In[ ]:





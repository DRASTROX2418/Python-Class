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


# ### I HAVE TWO GLASSES OF WATER I DRINK EACH EACH THIRTY MINUTES HOW MANY GLASSES OF WATER DO I DRINK IN TWENTYFOUR HOURS

# In[1]:


# Number of minutes in 24 hours 
minutes_in_a_day = 24 * 60 


# In[2]:


# Interval in which you drink a glass of water 
interval_minutes = 30


# In[3]:


# Calucalate the total number of glasses of water you would drink in 24 hours
total_glasses = minutes_in_a_day //


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





# In[36]:


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





# In[ ]:





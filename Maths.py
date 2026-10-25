#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Sum of Squares 

total = 0 
for i in range (1,49):
    total += i**2 
print("Sum of Squares which Aarush could not answer=", total)

#1^2+2^2+3^2+......48^2


# In[5]:


total = 0 
for i in (100,200):
    total += i**2
print("Result=", total)


# In[7]:


total = 0 
for i in range(100,201,100):
    total +=i**2
print(total)


# In[8]:


print(sum(i**2 for i in [100,200]))


# In[15]:


def table(n):
    for i in range(1,11):
        print(n,"x",i, "=",n*i)
        
table(10)


# In[16]:





# In[ ]:





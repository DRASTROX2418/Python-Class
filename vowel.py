# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:13:07 2026

@author: aarus
"""

# word = "aarush"
#        #012345
# print(word[2])
# print(word[4])

# #String slicing
# #show how python can extract parts of strings
# print(word[0:3])
# print(word[2:5])

def count_vowels(word):
    count=0
    
    for ch in word:
        if ch in "a,e,i,o,u":
            count +=1
    return count

print(count_vowels(""))
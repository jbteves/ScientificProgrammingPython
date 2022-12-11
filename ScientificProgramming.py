#!/usr/bin/env python
# coding: utf-8

# # Scientific Programming in Python Tutorial

# ## Introduction

# This notebook is designed to introduce you to some of the basics of scientific python and programming.  It will follow along with the structure of our Bootcamp lecture, as well as alert you to additional tips and tricks you may use in python. We encourage you to run this notebook cell by cell (using Shift + Enter) or by typing out the code separately into an interactive python terminal or separate notebook, so that you can get accustomed to typing out code with the correct syntax. At various points, there are lines of code that produce commonly-encountered errors.  These errors and other questions for you to play around with and answer are labeled "Exercise" -- feel free to "Ctrl-F" to search for the mini-exercises and work on them later.
# When in doubt, play around in the notebook, and during lecture or in your own time you can add notes as comments (use # to write a comment) to save for later.  You can also type 'help(function)', with the name of any function in the notebook for a detailed explanation.  Especially as you continue to use python or other programming languages, you can also use Google to troubleshoot issues you run into (you may find questions and answers on a site like Stack Overflow).  Googling is very common for coders of all levels : - )
# Happy Pythoning!
# 
# This notebook made as inspired from a Matlab Boot Camp by: Kelly Martin, Marissa Laws, Tyler Ketchabaw, Flo Martinez Addiego, and Plamen Nikolov
# 
# Author: Joshua B. Teves

# ## Data Types and Assigning Variables
# 
# ### What are Data Types? What are variables?
# 
# Python stores different types of data (numbers, strings, lists, and dictionaries) in different ways.  Certain functions and things you can do to your data depend on which data type they are.  Variables are a named location to store the data.  To the left of the equals sign is a variable name. The general form for this is 
# ```
# name = value
# ```
# For example:

# In[6]:


# Assign the value of 1 to the name x
x = 1
x


# You can re-assign a variable, changing its value. This erases the previous value for most types.

# In[7]:


# Assign the value of 2 to the name x
x = 2
x


# You can also delete a variable with the del operator, removing its name. The below cell will cause a NameError.

# In[10]:


del x
x


# We will now go over the most common python types. In scientific programming, the standard package for performing math is NumPy. Because NumPy is not built in, we will need to import it. In order to import a package, we use the format
# ```
# import package_name
# ```

# In[11]:


import numpy


# ### Lists
# In Python, lists are a collection of elements that occur in some order. In order to define a list, elements must be separated by commas and enclosed in square brackets, like this:
# ```
# my_list = [1, 2, 3, ...]
# ```
# In order to access a particular element, you have to use an index, or the number of places from the start that the element is located at. For example, the "first" element is 0, the "second" is 1, and so on. You must access the element by placing the name to the left of square brackets enclosing the index, like this:
# ```
# my_list[index]
# ```
# You can also count the number of positions from the end with a negative index; -1 indicates the "last" element.
# ```
# my_list[-1]
# ```

# In[16]:


# define a list containing the first 4 positive integers
my_list = [1, 2, 3, 4]
# and access its first element
print(f'The first element of my list is {my_list[0]}')
# and its last
my_list[-1]
print(f'The last element of my list is {my_list[-1]}')


# In[ ]:





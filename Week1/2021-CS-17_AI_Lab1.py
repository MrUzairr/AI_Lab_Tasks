#!/usr/bin/env python
# coding: utf-8

# # <center>Artificial Intelligence</center>  <center>Fall 2023</center>
# ## Lab 01
# #### Name: Muhammad Uzair
# #### Roll nber: 2021-CS-17
# 

# Take weight in kgs and convert it into pounds. 1 pound = 1 kg 2.2046 **(2 marks)**

# In[1]:

## add code here
kg = float(input("Enter weight in kilograms: "))
pounds = kg * 2.2046
print(f"{kg} kilograms is equal to {pounds} pounds")



# Calculate the cost of all the items in a shopping cart. **(2 marks)**

# In[2]:

## add code here
prices =[20,50,80,10,56,89]
totalCost = sum(prices)
print(f"The total cost of all items in the shopping cart is: ${totalCost}")



# Write a function that returns the maximum of two numbers. **(2 marks)**

# In[3]:


## add code here
def findMaximum(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

solution = findMaximum(10, 20)
print(f"The maximum number is: {solution}")

# Write a function called **deepmind** that takes a number  **(4 marks)**
# * If the number is divisible by 3, it should return deep.
# * If it is divisible by 5, it should return mind.
# * If it is divisible by both 3 and 5, it should return deepmind.
# * Otherwise, it should return the same number.
# 
# 
# 

# In[4]:


## add code here
def deepmind(number):
    if number % 3 == 0 and number % 5 == 0:
        return "deepmind"
    elif number % 3 == 0:
        return "deep"
    elif number % 5 == 0:
        return "mind"
    else:
        return number

result = deepmind(15)
print(result) 

result = deepmind(9)
print(result) 

result = deepmind(10)
print(result)

result = deepmind(7)
print(result)  

# **listA** =  [1,2,3,4,5,6,7,8,9,10]  
# 
# If an element of **listA** is smaller than 5, replace it with 0. And if an element of x is bigger than 5, replace it with 1. (**2 marks**)

# In[5]:


## add code here
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(listA)):
    if listA[i] < 5:
        listA[i] = 0
    elif listA[i] > 5:
        listA[i] = 1
print(listA)


# Compute the square of **listA** elements in one line. (**2 marks**)
# 

# In[6]:

## add code here
listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredListA = [x**2 for x in listA]
print(squaredListA)


# Concatenate b1 and b2. (**2 marks**)

# In[7]:

## add code here
b1 = ['Hello', 'in','first']
b2 = ['Students','the','recitation']
concatenatedList = b1 + b2
print(concatenatedList)


# Create a dictionary of student **Ali** where the keys are courses and values are total and obtaining marks in each course. Print the dictionary items subjects wise **(2 marks)**

# In[8]:


## add code here

aliMarks = {
    'Math': {'Total': 100, 'Obtained': 90},
    'Science': {'Total': 90, 'Obtained': 85},
    'History': {'Total': 80, 'Obtained': 70},
    'English': {'Total': 95, 'Obtained': 88}
}

for subject, marksInfo in aliMarks.items():
    print(f"Subject: {subject}")
    print(f"Total Marks: {marksInfo['Total']}")
    print(f"Obtained Marks: {marksInfo['Obtained']}")


# Create a class 'calculator' with the following functions to compute i) addition, ii) subtraction, iii)multiplication, iv)division and v)square
# between two numbers. **(2 marks)**

# In[9]:


## add code here
class Calculator:
    def addition(self, n1, n2):
        return n1 + n2

    def subtraction(self, n1, n2):
        return n1 - n2

    def multiplication(self, n1, n2):
        return n1 * n2

    def division(self, n1, n2):
        if n2 == 0:
            return "Division by zero is not allowed."
        else:
            return n1 / n2

    def square(self, n):
        return n ** 2

calc = Calculator()

resultAdd = calc.addition(5, 3)
resultSub = calc.subtraction(10, 4)
resultMul = calc.multiplication(6, 2)
resultDiv = calc.division(8, 2)
resultSquare = calc.square(7)

print(f"Addition: {resultAdd}")
print(f"Subtraction: {resultSub}")
print(f"Multiplication: {resultMul}")
print(f"Division: {resultDiv}")
print(f"Square: {resultSquare}")



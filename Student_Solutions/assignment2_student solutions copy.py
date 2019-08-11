#Shruti Kasera
#07.08.19
#Assignment 2

#Question 1 (3/3)
def function1(input_str):
  for i in range(25):
    print(input_str)

#Question 2 (1/2)
"""
You did not answer the second half of the question which was if an infinite loop was possible using a for loop
"""
'''
An infinite loop is one that never ends. It will always continue to loop over and will never come to an end

def infinite(num):
  while num >0:
    print(num)
infinite(5)
'''


#Question 3 (3/3)
'''
Python lists are helpful for storing multiple numbers or even strings within them. Lits are mutable making them much more easy to manipulate. You can also use lists to store lists within lists.
'''

#Question 4 (1.5/3)
"""
you said "The keys have to be like variable names, they can not be numbers" which is not try. The keys can be anything
as long as the data type is immutable so numbers and strings will be fine to be a key in a key-value pair
"""
'''
Dictionaries in python are made up of two parts, a key and value. They are called key value pairs. Similar to a real dicitonary, it holds many different keys with different values to them. Almost like a word and its definition. With dictionaries in python you can store many pairs and recall them later in a function. The keys have to be like variable names, they can not be numbers. The values are like strings and can be any type.
'''

#Question 5 (0/2)
"""
Check the solution. This is an easy question. We talked about this during the first week of classes.
"""
'''
The difference between a method and function is that a method will usually end with .(). Whereas a function will not. They are both already built into python and can be called in order to write code mroe efficiently.
'''

#Question 6 (5/5)
"""
For improvement you should change empty_list to filtered_list (a better var name)
"""

def lessthan_greatherthan(num):
  empty_list = []
  for j in num:
    if j < 50 or j > 85 :
      empty_list.append(j)
  return empty_list
print (lessthan_greatherthan([1,2,5,6,77,124,45,68]))


#Question 7 (4/10)
"""
Nope this does not work. It will always return False. Can you see why?
You are on the right track though.
"""

def duplic(lists):
  for j in lists:
      if j==j:
        return False
      else:
        return True
print(duplic([1,6,7,4,4]))

#Question 8 (0/10)
"""
We will talk about this one together.
"""

#saw solution need more explaining

def check(str):
  dict={}
  for x in str:
    key=dict.keys()
    if x in key:
      dict[x]+=1
    else:
      dict[x]=1
  print(dict)
print(check("apple"))

#Question 9 (4.5/5)
"""
This is fine and works but is not the best solution.
There is no need to print the spaces as they only appear at the end of each line. 
"""
def pattern(num):
  for number in range(0, num):
      print ((num-number) * "*" + number * " ")
pattern(6)

#Question 10  (2/15)
"""
Perhaps you did not understand the question. We will go over this in class.
"""
def game(digit):
  while player2 <= 4:
    player2 = int(input("Guess what the number is?: "))


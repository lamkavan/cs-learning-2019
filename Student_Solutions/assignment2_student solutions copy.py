#Shruti Kasera
#07.08.19
#Assignment 2

#Question 1
def function1(input_str):
  for i in range(25):
    print(input_str)

#Question 2
'''
An infinite loop is one that never ends. It will always continue to loop over and will never come to an end

def infinite(num):
  while num >0:
    print(num)
infinite(5)
'''


#Question 3
'''
Python lists are helpful for storing multiple numbers or even strings within them. Lits are mutable making them much more easy to manipulate. You can also use lists to store lists within lists.
'''

#Question 4
'''
Dictionaries in python are made up of two parts, a key and value. They are called key value pairs. Similar to a real dicitonary, it holds many different keys with different values to them. Almost like a word and its definition. With dictionaries in python you can store many pairs and recall them later in a function. The keys have to be like variable names, they can not be numbers. The values are like strings and can be any type.
'''

#Question 5
'''
The difference between a method and function is that a method will usually end with .(). Whereas a function will not. They are both already built into python and can be called in order to write code mroe efficiently.
'''

#Question 6

def lessthan_greatherthan(num):
  empty_list = []
  for j in num:
    if j < 50 or j > 85 :
      empty_list.append(j)
  return empty_list
print (lessthan_greatherthan([1,2,5,6,77,124,45,68]))


#Question 7

def duplic(lists):
  for j in lists:
      if j==j:
        return False
      else:
        return True
print(duplic([1,6,7,4,4]))

#Question 8

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

#Question 9
def pattern(num):
  for number in range(0, num):
      print ((num-number) * "*" + number * " ")
pattern(6)

#Question 10

def game(digit):
  while player2 <= 4:
    player2 = int(input("Guess what the number is?: "))


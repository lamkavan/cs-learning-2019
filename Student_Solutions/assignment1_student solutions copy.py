#Question 1 (3/5)

# a) // : This will divide a number and then round down to the nearest number
print(15 // 7)
"""
This is div. You did not name it as requested.
"""

# b) ** : This is used as a squaring feature.
print (2 ** 18)
"""
No it is not a squaring feature, it is the exponential operator.
"""

# c) % : This function will divide a number and then return the remainder
print (500 % 13)
"""
This is the mod operator. You did not name it.
"""

# d) * : This is the multiplication function
print ("*" * 22)

# e) / : This function is to divide. If not an even number it will return a float.
print( 15 / 7)
"""
you wrote If not an even number it will return a float. This has nothing to do with the
operator...
"""

#Question 2 (3/3)

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name, "your age is", age)

#Question 3 (2/2)

"""
This will return a ZeroDivisionError because any number divisible by zero is not possible.
"""

#Question 4  (3/3)

'''
String: A string is immutable. It is a sequence of characters. A string is created with one, two or three quotation marks.
List: A string is mutable. It is entrapped within square brackets. Every item in a list is spaced by commas. Also strings 
can be put within a list.
Dictionary: A dictionary is put within curly brackets. It has two components, a key and a value. The key is like a word
in the dictionary and the value is the definition of it. They are listed within a dictionary and can later be altered 
or called.
'''

#Question 5 (2/2)

'''
The problem with the code is that a string and integer data type cannot be added together. They are not compatible.
'''

#Question 6 (5/5)

def lucky(num):
    if num == 50:
        print("Wow this is my lucky number")
    elif num > 50:
        print("Wow that is a big number")
    else:
        print("That is a small number")
print(lucky(50))

#Question 7 (4/5)
"""
you should have used elif instead of if for the second case in the
if clause. We talked about why this is bad. 
"""

def greater(num1, num2):
    if num1 > num2 :
        print (num1, "is greater than", num2)
    if num1 < num2 :
        print( num2, "is greater than", num1)

print(greater( 15, 6))

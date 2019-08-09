'''
Question 1
Given two strings as input return a string with the characters from the two strings, but ensure the characters are
interchanged with each other. For example, if the input strings are "cat" and "dogy" then the return string
should be “cdaotgy”. Note you are NOT allowed to use any string methods for this question.
'''

def interchange(word1, word2):
    if not word1:
        return word2
    elif not word2:
        return word1
    else:
        return word1[0] + word2[0] + interchange(word1[1:], word2[1:])

print (interchange("cat", "dogy"))


'''Question 2
Write a function that takes in one string and returns True if the string is a palindrome and False otherwise.
You are NOT allowed to use any string methods for this question. If the function get an empty string as input
then we should return False.
'''

def palindrome(word3):
    if word3 == '':
        return False

    elif word3 == word3[::-1]:
        return True
    else:
        return False
print(palindrome("tacocat"))

'''
Question 3
Write a function that takes in one word (str) and prints to the console the number of vowels and consonants in the word.
The vowels are a,e,i,o and u. You can NOT use any string methods.
'''
"""
vowel_counter = 0
alphabet = "qwertyuioplkjhgfdsazxcvbnm"
consonants = alphabet - vowels

def any_vowels(word4):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_counter = 0

    for i in word4:
        if i in vowels:
            vowel_counter += 1

print(word4 "has", str(vowel_counter) + "vowels")
print(word4 "has", str(len(word4) - vowel_counter) + "consonants")
"""


'''
Question 4
Write a function that takes a single string as input and returns the same string but with every other character capitalized.
Start by capitalizing the first character.
'''

def every_other(word5):
    switched = ""
    i = True
    for j in word5:
        if i:
            switched +=  j.upper()
        else:
            switched += j.lower()
        if j != ' ':
            i = not i
    return switched

print (every_other("hello world"))

'''
Question 5
Write a function that takes in three strings labeled str1, str2 and str3. The function will find all occurrences of
str2 in str1 going from left to right and replace it with str3 then return the final string. For example if the input
strings are hellollo, lo and bob then the return string is “helboblbob”.
'''
def replace(str1, str2, str3):
    new_string = ''
    while str1.find(str2) >= 0:
        new_string += str1[:str1.find(str2)] + str3
        str1 = str1[str1.find(str2) + len(str2):]
    new_string += str1
    return new_string
print (replace( "hellollo", "lo", "bob"))


'''
Question 6
Write a function that takes in one string and prints to the console the same string but without any white spaces.
For example if the input string is “hello world I am the best” then the function should print “helloworldIamthebest” to
the console. Do NOT use any string methods. There is already a string method that can do this but you are not allowed
to use it.
'''

def remove(word6):
    more_strings = ''

    for s in word6:
        if s != " ":
            more_strings += s
    return more_strings
print(remove("hi my name is Shruti"))

'''
Question 7
Write a function that prints to the console a star triangle given a height parameter.
For example, if the height parameter is 5 then the function should print the following to the console...
*
**
***
****
*****
'''

def height(num):
    for p in range(num):
        print("*" * (p + 1))
print(height(5))

'''
Question 8
Write a function that takes in a word (str) and prints to the console all the characters that occurred more than once
and the number of times the character appears in the string. Note that ordering does not matter and you are NOT
allowed to use string methods. You can still use dict, list, int and float methods though if you like.
'''


'''
Question 9
What are two difference between a list and a tuple?
'''

#The difference between a list and a tuple is that a tuple has curly brakcets whereas a list has square brackets.
#Also tuples are immutable and lists are mutable

'''
Question 10
What are some methods for tuples? What do you notice?
'''
#There are not many methods for tuple. The only two which are suugested by pycharm and count() and index().
#There are not many ways to alter a tuple with methods

'''
Question 11
When can tuples be useful? Give an example of when tuples are better than list.
'''
#Situations where a tuple is better than a list is when you do not want your array to be mutable.
#When you know that some data will never change, a tuple is better to store it.

'''
Question 12
Does aliasing happen with tuples?
'''
#Since tuples are immutable, aliasing will not occur with them. On the other hand with a list, being a mutable data type
#, it will be prone to aliasing

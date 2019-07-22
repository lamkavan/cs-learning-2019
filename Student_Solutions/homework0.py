# Question 1
a = "I love computer science"
# print a backwards and each letter on seperate lines

b= a[::-1]
for i in b:
    print(i)




# Question 2
# find 2 seperate new methods for lists and learn them + DEMO

# .count() returns the amount of occurences of an element in a list
seq= [1,1,3,6,5,5,5,5]
counter = seq.count(5)
print(counter)

# .reverse() returns the reverse of a list
series= ["1","2","5","2"]
series.reverse()
print(series)





# Question 3
#loop through the list and if its a string print"its a string" if its an integer print"its a number"

f= ["a", "24", "5", "6", "7", "sss", "6"]
for j in f:
    if j.isdigit():
        print(j, "its a number")
    else:
        print(j, "its a string")




"""
Comments:
You answered everything correctly. The questions are pretty easy.
However, there are two formatting errors that I want to address.
First, notice how when you do f= ["a", "24", "5", "6", "7", "sss", "6"]
for question 3 there is a yellow line around the f=. This is because you need 
a space after f and one after the = . Next, when you do series= ["1","2","5","2"]
notice how there are a bunch of yellow lines around the elements of the list.
This is because you need to add a space after each element in the list
so series= ["1", "2", "5", "2"] instead. Finally, just as a side note, if you
red lines that is very bad that means there is something wrong with the code.
Yellow lines are just warning many of which will be formatting issues which
have no effect on the execution of the program.  
"""
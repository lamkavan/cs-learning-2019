# Question 1
a = "I love computer science"
# print a backwards and each letter on seperate lines

b= a[::-1]
for i in b:
    print(i)

# Question 2
# find 2 seperate new methods for lists and learn them + DEMO

# .count() returns the amount of occurences of an element in a list
seq = [1,5,3,6,5,5,5,5]
counter= seq.count(5)
print(counter)

# .reverse() returns the reverse of a list
series= ["1","2","5","2"]
series.reverse()

print(series)

# Question 3
f = ["a", "2", "5", "6", "7", "sss", "6"]

for j in f:
    if j.isdigit():
        print(j, "its a number")
    else:
        print(j, "its a string")
#loop through the list and if its a string print"its a string" if its an integer print"its a number"



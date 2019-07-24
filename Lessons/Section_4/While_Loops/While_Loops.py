"""
Here we will take about while loops. While loops are similar to for loops, but while loops
have the ability to stop and keep going based on a condition or conditions. We will also talk
about break and continue which are useful for the more complicated problems.
"""


# Lets begin with the general structure of while loops
"""
while <Condition>:
    <Do this stuff here>
"""
# That is it. Not too bad. It will keep repeating the code inside the while loop as long as the
# condition evaluates to True. As soon as the condition is False the loop will stop.


# Now lets do an example.
"""
while 1:
    res = input("Would you like some tea my love? ")
    print("Your response is:", res)
"""

# Well looks like we are in whats called an infinite loop. This is because the condition in the
# while loop will turn False and so it is always True and as long as the condition is True we keep on
# looping.


# So lets redo the example, but ensure we stop asking once the user enters the word no (exactly)
res = ""
while res != "no":
    res = input("Would you like some tea my love? ")
    print("Your response is:", res)


# Alright so that was a pretty easy example. Now lets do a more complicated example.
# Here is what we want to do... we want to write a function that takes in a list
# and iterates through the list using a while loop. This is much easier with a for loop
# just so you know. To make it more interesting, the list will only contain numbers. If we
# encounter a float we must get out of the while loop right away and print "we hit a ugly number!"
# and if we see an int that is less than 10 do we do not print the number to the console and skip
# it
def weird_list_iteration(list_of_num):
    index = 0
    length = len(list_of_num)
    while index < length:
        element = list_of_num[index]
        if type(element) == type(1.1):
            print("We hit a ugly number!")
            break
        elif element < 10:
            index += 1
            continue
        else:
            print(element)
        index += 1

weird_list_iteration([1,2,3,4,11,12,3.3,66])
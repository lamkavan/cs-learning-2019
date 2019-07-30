"""
For this lesson we focus on drawing things out of characters.
This is something students generally find hard and is something
you the student requested. There is not much to learn here, but we
will do plenty of examples. One method that works for a lot of the
cases is to print the figure row by row. We already did star triangles
so here we focus on other things.
"""

# Question 1
# Write a function that print out a rectangle given a length and width parameter
# The rectangle will consists of stars
def draw_rectangle(length, width):
    for w in range(width):
        print("*" * length)
draw_rectangle(5, 3)
print("---------------------------------------------------")


# Question 2
# Write a function to draw a square with a diamond inside (something student requested)
# Note: the length must be odd otherwise the figure will look weird.
def draw_sqaure_diamond(length):
    num_of_spaces = 1
    delta_spaces = 2
    if length % 2 != 0:
        for level in range(length):
            if level == 0 or level == length - 1:
                print("*" * length)
            else:
                num_of_stars = length - num_of_spaces
                if num_of_stars == 2:
                    delta_spaces *= -1
                print("*" * (num_of_stars // 2) + " " * num_of_spaces + "*" * (num_of_stars // 2))
                num_of_spaces += delta_spaces
draw_sqaure_diamond(13)
print("---------------------------------------------------")


# Question 3
# Write a function to draw a trident with a width parameter.
# The width must be odd for this to work.
def draw_trident(width):
    if width % 2 != 0:
        # First we draw the teeth portion
        for i in range(3):
            num_of_spaces = width - 3
            print("*" + (" " * (num_of_spaces//2)) + "*" + (" " * (num_of_spaces//2)) + "*")
        # Now draw the bridge part
        print("*" * width)
        # Finally draw the handle
        for i in range(4):
            num_of_spaces = width - 1
            print(" " * (num_of_spaces // 2) + "*" + " " * (num_of_spaces // 2))
draw_trident(9)
print("---------------------------------------------------")

# Question 4
# Write a function to draw a letter E given a height parameter
def draw_letter_E(height):
    if height % 2 != 0:
        for row in range (height):
            if row == 0 or row == height-1 or row == height//2:
                print("*" * height)
            else:
                print ("*")

draw_letter_E(3)





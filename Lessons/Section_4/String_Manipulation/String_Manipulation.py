"""
In this section we talk about taking strings and doing interesting things
with them. Also, we practice working with strings in general since strings
are used a lot. A lot of string manipulation question such as reversing a string
may be easily done using string methods that are provided to us. However, there
are some problems that can't be solved via these methods. Furthermore, it is good
practice to be able to solve problems without having to depend on these methods
as some programming languages do not have these methods and often time you
will not be allowed to use them during tests/exams.
"""

# Lets begin by learning what a palindrome is and how to detect it
# A palindrome is a word that is the same spelled forward and backwards ie/ racecar and madam
# We will write a function for this. We will not use string methods to answer this.
def is_palindrome(str1):
    # Note if we use string methods we could just simply check if str1 == str1.reverse()
    str1_reversed = str1[::-1]
    if str1_reversed == str1:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
is_palindrome("racecar")


# Now lets write a function to print out an inverted star triangle given a height parameter
def print_inverted_star_triangle(height):
    for level in range (height, 0, -1):
        print("*" * level)
print_inverted_star_triangle(5)


# So far that was easy lets do something more intense...
# Write a function that takes a sentence and returns a str of all the words in the sentence
# without the punctuation or spaces
def remove_spaces_and_punctuation(sentence):
    # Notice the use of \. This is the esc character and is need as when we use " Python
    # thinks we are using it as part of a string construction but we actually want the "
    # to be part of the string so we must esc the " by using \
    punctuation = [".", ",", "\"", "'", ":", ";", "!", "?", "$", "@", "%", "#"]
    words = sentence.split(" ")
    word_reconstruction = ""
    for word in words:
        if word != "":
            for chr in word:
                if chr not in punctuation:
                    word_reconstruction += chr
    return word_reconstruction
remove_spaces_and_punctuation("Hello, My name is \"John\" and I love CS!!")


# Finally we write a function that takes a list of strings and returns a single big string
# with the letters from the list of words such that all the "a" are replaced with 1 and all
# "b" are replaced with 2. All other letters are capitalized. We go through the list from left to right
def get_mashup_string(list_of_strings):
    combined_str = "".join(list_of_strings)
    output_chr = ""
    for chr in combined_str:
        if chr == "a":
            output_chr += "1"
        elif chr == "b":
            output_chr += "2"
        else:
            output_chr += chr.upper()
    return output_chr
print(get_mashup_string(["Hello", "a b a b aa", "bob!"]))


"""
In this section we talk about a very important search algorithm called binary search.
This search algorithm is a bit more complicated than linear search and does not work
for all cases. We will go over the algorithm, why it is called binary search, the cases
that this algorithm will work and most importantly the advantages of binary search when it works.

The algorithm... (Feel free to search online for visuals and animations)
1) Have variables to keep track of a lower and upper bound. The bounds will help us
   define the range in the list that we are considering. At the beginning, the range will
   be the full list so lower bound is set to beginning of list and upper bound gets set to
   the end of the list. The range will get smaller as we go so we can pin point what we are
   searching for.
2) Start a loop that will search for our target. Continue searching/looping until the lower bound
   and upper bound cross each other or the lower bound > upper bound
3) For each iteration of the loop we compute the middle index from the lower to upper bound
4) If the number in the middle index is the target then we return True as we have found the number.
   If the number in the middle index is larger than the target number than move the upper bound
   to one less than the middle index
   If the number in the middle index is less than the target number than move the lower bound to
   one more than the middle index
5) If the loop finishes without finding the target then return False

The reason why this algorithm is called binary search is because we are searching for the target in a way
that allows us to not have to look at every single element in the list and in particular we are skipping half the
list at every iteration. The skipping is done by reducing the range to half the original size. The keyword there is half.
Binary means two and there are two halves. Another way to think about it is that we either change the lower bound or the
upper bound at each iteration so there are two options thus binary (two)

By the way the reason why the code is not given to you is because this is a question in the assignment and homework.

Alright, so binary search is cool, but it only works in a specific case. Binary search only works when the input list
is in sorted order from smallest to largest. The input list could be from greatest to smallest but the algorithm would
need to have a small change (Do you know what that change is? Well that is homework). The reason why the list must
be sorted for this to work is because we are skipping numbers based on the value of the middle number that is possible 
if the list is sorted as the hierarchy of the values before and after the middle one are known. 

The main advantage of using binary search when the input list is sorted is simply because it is faster then using linear
search. The reasoning is quite simple. With linear search you are basically checking each number, but with binary search
you search by looking at the middle number and skip many of the values. The less number Python has to check the
faster the program will be. Make sense?
"""
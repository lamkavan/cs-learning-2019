"""
In this section we talk about another sorting algorithm. This time we will learn about
insertion sort. This sorting is a bit harder to code, but a lot easier to understand and see why
it works. As always we begin with the algorithm, but there will be no code as I want you to do that
for homework/assignment. In addition to the algorithm we will discuss how this algorithm can be better than
bubble sort, why it is called insertion sort and the pros and cons of this algorithm.

The algorithm...
1) We will iterate over the whole list from left to right using index (no need to iterate over first value)
2) we build up the sorted list from left to right. This means there will be two sections
   in the list. A sorted section and a non-sorted section. The sorted section will be on the left
   and the non-sorted section to the right. As the number of iterations increase the sorted section on
   the left will expand and soon the whole list will be sorted
3) During the iterations the index we are currently at is the boarder between the sorted and non-sorted sections
4) The value at the index we are currently looking at will need to be inserted in to the correct position on the sorted
   side (which is to the left). We call this value the key
5) step 4) is done as follows. Iterate from the index you are at towards the start of the list. Along the way makes
   comparisons. If the key is bigger than or equal to the value we are looking at during the backwards iteration than we
   know that the key is in the correct position otherwise we push the value up one index and keep iterating. Once we get
   back to the start the index to place the key is known. Make the correct placements.

This explanation of the algorithm is not the best refer to goggle and other online resources for better explanations.
However, we will go through this during class it you will learn it there.

Confused? Here is an example
Iteration 0  (before the code even runs) ---------- [5,7,1,5,2,5,110]
Iteration 1 ---------- [5,7,1,4,2,5,110] (7 is in correct position from sublist of index 0 to 1)
Iteration 2 ---------- [1,5,7,4,2,5,110] (1 got moved to correct position from sublist of index 0 to 2)
Iteration 3 ---------- [1,4,5,7,2,5,110] (4 got moved to correct position from sublist of index 0 to 3)
                                              Notice how these numbers are the iteration number -----^

One reason why insertion sort can be better than bubble sort is that it generally does not need to make as many
comparisons as compared to bubble sort. What happens if you give insertion sort an already sorted list. What about
a reversed list. You will see that that if the list is already sorted then only n comparisons are made which is better
than n^2 from bubble sort. If the input list is reversed then insertion sort will do n^2 comparisons which is the same
as bubble sort. The reason why it is called insertion sort is because we are iterating over the values of the input list
and inserting each value into their correct spot on the sorted side.

"""
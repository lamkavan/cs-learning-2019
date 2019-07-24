"""
Tuples are basically like list but you can not change any of the elements.
tuples are also immutable so aliasing does not happen with tuples.
"""

# Below is an example of the fact that tuples have no aliasing effects
tuple1 = (1, 2, 3, "blah")
tuple2 = tuple1
tuple1 = (2, 3, 6)
print(tuple2)

# Tuples can be indexed just like list
tuple1 = (1, 2, 3, "blah")
print(tuple1[0])
print(tuple1[0:3])

# Verify that we can not change the elements of a tuple
# tuple1[0] = "a" does not work
tuple1 = (1, 2)
tuple1 = (1, 1, 1)  # This works as we are assigning a totally new tuple to tuple1


# static data is data that will not change over time. We also call these constants.
# So if you plan on collecting and storing data it might be a good idea to use a tuple
# instead of a list.

# Tuples do not have a lot of methods. There are only 2 official methods.
# 1) count
# 2) index

# A lot of the methods that exist for list do not exist for tuples since tuples are immutable.

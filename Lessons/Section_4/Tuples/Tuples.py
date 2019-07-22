"""
Tuples are basically like list but you can not change any of the elements.
tuples are also immutable so aliasing does not happen with tuples.
"""

# Below is an ex of that fact that tuples have no aliasing effects
tuple1 = (1, 2, 3, "blah")
tuple2 = tuple1
tuple1 = (2, 3, 6)
print(tuple2)

# Tuples like list can be indexed
tuple1 = (1, 2, 3, "blah")
print(tuple1[0])
print(tuple1[0:3])

# Verify that we can not change the elements of a tuple
# tuple1[0] = "a" does not work
tuple1 = (1, 2)
tuple1 = (1, 1, 1)


# static data is data that will not change over time.

# Tuples do not have a lot of methods. There are only 2 offical ones.
# 1) count
# 2) index
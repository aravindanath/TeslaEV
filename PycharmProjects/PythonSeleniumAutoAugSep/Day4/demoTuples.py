"""
The index() method searches an element in a tuple
and returns its index. In simple terms, index()
 method searches for the given element in a
 tuple and returns its position.
 However, if the same element is present more than once,
 the first/smallest position is returned.
"""

demo = (2,3,4,0,00,0,0)

dem1 = (22,22,22,22,2,34)


print(type(demo))

print(dem1.count(2))
print(dem1.index(34))
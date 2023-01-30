"""
task: add items to a tuple
"""

myTuple = ("apple", "banana", "cherry")

#solution 1
myTuple += tuple(["kiwi"])

#solution 2
myTuple = tuple(list(myTuple) + ["avocado"])

print(myTuple)

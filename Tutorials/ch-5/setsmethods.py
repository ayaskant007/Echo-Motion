s = {1, 5, 33, 5, 5, "Hello"}  # takes each value once, elements cant repeat

e = set()  # empty set

print(s) #repetion of elements not allowed

s.add(566)
# s.clear() #clears the set
print(s, type(s))
len(s) #length of set
s.remove(33)
print(s, type(s))
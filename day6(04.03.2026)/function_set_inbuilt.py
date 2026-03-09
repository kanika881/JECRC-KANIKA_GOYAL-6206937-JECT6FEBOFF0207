set={1,2,3,4,3,1.5}
set.add(8)
set.add(1.5)
print(set)
s={1,2,True,False,0,3+8j}
# it doesnt store the value in organizable way
# set is mutable 
# it takes only immutable datatype as the input
s.add(4)
print(s)
# s1={1,2,3,(23,34),{1:7,34:3}}
# TypeError: unhashable type: 'dict'
s.add((34,34))
print(s)

# add() -> 1 argument should be pass that argument should not prensent in set already because set only conatin unique element  also no changes will be show 
# remove ;- removing element should be member of its , else keyerror 

# print(s.remove(3+9j)) getting keyerror

print(s)

print(s.remove(True))
print(s)

# print(s.remove(10))     # key error 
# print(s)


# discard ;- same as remove but not show error it wil show missing element 

print(s.discard(10)) # it will not show error show none 

print(s.pop()) # randomly remove 
print(s)

# deafult value of set is set()
#set() - is a sobject beacuse call as a class 

# clear -> only empty set will remain 

print(s.clear())
print(s)



# union;- return a new set with elements from the set and all others  

s1 = {1,2,3}
print(s1)
s2 ={2,3,4}
print(s2)
s3 = s1.union(s2) # we can pass multiple arguments by using , (comas)
print(s3)
print(s1.union({1,2,3} , {3,5,6} ,{9,5,6}))

# sintersecttion - comman 

print(s1.intersection(s2))

# difference ;- not comman 
print(s1.difference(s2))
print(s2.difference(s1))

# symmetric difference ;- not comman elements in both 
print(s1.symmetric_difference(s2))


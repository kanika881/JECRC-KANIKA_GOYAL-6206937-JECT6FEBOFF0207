#  function to string data type 
# Python string methods is a collection of in-built Python functions that operates on strings.

# function for string data types 

'''
1 lower 
2 upper
3 capitalize
4 title 
4 strip 
5 lstrip 
6 isdigit 
7 isupper
8 islower
9 replace
10 index 
11 split 
12 join
13 startswith 
14 endswith 
15 endswith 
16 isalpha 
17 islower
'''

s = "PythON"
print(s.lower()) # return value

result = s.upper()
print(result)

s1 = "python"
print(s1.capitalize())

# title 
s2 = "kanika is a good girl"
print(s2.title())

#strip    only starting and ending space or character 
s3 = "   kanika is   "
print(s3.strip())

#lstrip    remove only left side whitespaces and charcter will remove 
print(s3.lstrip())

#rstrip    remove from right side 

print(s3.rstrip())
# replace
s4="kanika is going to be a software developer .. kanika is doing good"
print(s4.replace("kanika","kanika goyal"))
# index 
s5="kanika a"
print(s5.index("k"))
# in find and index there is only one differnce in case of missing word find returns -1 whereas in case of index it returns a value
print(s5.find("l"))
s6="I LOVE PYTHON PROGRAMMING LANGUAGE"
# it returns a list collection based on serpator value here the seperator is white spaces
print(f"here the seperator is white spaces:{s6.split()}")
print(f"here the seperator is PYTHON:{s6.split("PYTHON")}")

s6="I-LOVE-PYTHON-PROGRAMMING-LANGUAGE"
print(f"here the seperator is - :{s6.split("-")}")
list_OF_S6=s6.split("-")
# leanring join 
print(help(str.join))

print(f'joining the iterable list with white spaces: {" ".join(list_OF_S6)}')
print(f'joining the iterable list with @ : {"@".join(list_OF_S6)}')
# learning startswith
s7="kanika"
print(s7.startswith("ka"))
print(s7.endswith("ika"))
# checks the entire string consist of digit 
s8="23@@"
print(s8.isdigit())
print(s8.isalpha())
print(s8.isalpha())
s9="KANIKA"
print(s9.isupper())
s10="goyal"
print(s10.islower())



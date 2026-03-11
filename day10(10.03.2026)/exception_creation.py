'''
raise--> it is a keyword which helps us to throw an error in between a program
Exception Creation
1 Custom Exception (raise)
2 User- defined Exception 
3 Assertion Exception(assert)

'''

'''
Custom exception :
    1 We use pre-built Exception classes according to our requirement.
    
    raise ValueError :message
'''
# num=17
# if num>=18:
#     print("you are eligible for voting & driving")
# else:
#     # raise NameError("Age should be greater than or equal to 18")
#     raise KeyboardInterrupt("you are underage")

'''
--------------------------------------
user definded Exception
it is a type of exception in which we can create our own exception classes based upon our own requiremeny .We can also 
provide names to those classes according that user cases.
'''
# class MyException(Exception):
#     pass
# # raise MyException("this is my exception")
# # n1,n2=10,3
# n1,n2=21,0
# if n2==0:
#     raise MyException("second number should not be zero")
# else:
#     res=n1/n2
#     print(res)
'''
-----------------------------------------------
Assertion Exception -- can be created by using one keyword called "assert"

assert<condition>,print(ERROR)

'''
s=input("Enter a string:")
assert s==s[::-1] , print("it is not a palandromic string")
print("it is a palandromic string")



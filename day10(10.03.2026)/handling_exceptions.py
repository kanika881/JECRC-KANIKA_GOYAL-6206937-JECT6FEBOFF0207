import time

"""
---------------------------------------
--unauthorized event 


--flow of the execution of the program will be stopped
output error:
errorname
reason
line no

try block  we will put problem statement (block of code due to which we might get error )
else block:
alternative code of try block
if we find out any error inside try block interpreter will move forward towards else block
if code of else block is correct(output)
if code is incorrect (error)


except block we put actual solution for the error 
due to except block we can prevent the unauthorized events(errors)
if the color is purple or pink : exception
red :error
purple :warning

-resolution for error prone code
finally after getting error or after resolution forcefully if we want to execute any particular block of code then we use finally 
approaches to handr	

exception handling approaches
-->specific exception handling 
-->generic exception handling 
-->default exception handling
-------------------------------------------------------------------
"""
"""
-------------------------------------------------------------
specific exception handling:
-- if we are aware of the error or, exception then we can go with specific
try:
problem statement
except ErrorName:
    resolution / solution code
"""
# n1,n2=21,0
# # print(n1/n2)
# try:
#     result=n1/n2
#     print(result)

# except ZeroDivisionError:
#     ##solution code
#     print("please do not choose zero as the second number")
    
# print("code after try except -01")
# print("code after try except -02")
# print("code after try except -03")

# a,*b,d=1,2
# print(a,b)
# try:
#     a,b,c=1,2
# except ValueError:
#     print("for performing MVC , no of variables should ne equal to no of values")
# try:
#     print(a,b,c)
# except NameError:
#     print("Identifiers are not in the memory")
    
'''
--------------------------------------------------------------------
generic execption handling
-- it is a type of exception andling approach in which there is no need to pass any particular exception 
class name . instead of we can use parent "exception " class called "Exception"
# '''
# try:
#     a,b,c=1,2
# except Exception:
#     print("for performing MVC , no of variables should ne equal to no of values")
# try:
#     print(a,b,c)
# except Exception:
#     print("Identifiers are not in the memory")


# -- using generic exception handling we cant handle keyboard interruption 

# try:
#     while True:
#         print(time.time())
# except Exception:
#     print("loop got stopped")
# executing the same keyboard interruption using specfic exception handling 
'''
try:
    while True:
        print(time.time())
except KeyboardInterrupt:
    print("loop got stopped")
'''

'''
-------------------------------------------------------
--default exception handling 
it is a type of exception handling in which we can handle all types of errors or exception expect SyntaxError

'''


     
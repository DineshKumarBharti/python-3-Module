# import mymodule
import mymodule as m
list =[1,2,3,4,5,6]
print(list)
# print(mymodule.person)
# print(mymodule.lst)
# print(mymodule.test())

print(m.person)
print(m.lst)
print(m.test())

obj=m.A()
print(obj.test())

# OUTPUT
# [1, 2, 3, 4, 5, 6]
# {'Name': 'dinesh', 'city': 'satna', 'age': 25}
# ['ajay', 'ramesh', 'sumit', 'anuj', 'rahul']
# Hello this is a test Funtion
# This is class A !!

#  INBUILT MODULE 
import keyword
print(keyword.kwlist)

# output
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
#   'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from',
#     'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
#       'raise', 'return', 'try', 'while', 'with', 'yield']
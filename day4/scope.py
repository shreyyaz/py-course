# # Variable Scope = where a variable is visible and accessible
# # Scope Resolution = (LEGB) Local > Enclosed > Global > Built-in

# def fn1():
#     x = 1  # x is local to fn1()
#     print(x)

# def fn2():
#     x = 2  # x is local to fn2()
#     print(x)
# #fn1 and fn2 are two diffent functions, take eg of 2 alag ghar, whatev happens inside them stays there only
# x=3 #global scope of variable x
# fn1() #will use local over global
# fn2()


# #ENCLOSEDD
# def outer():

#     x = 10  # enclosed scope variable

#     def inner():
#         x=40 #local scope variable
#         print(x)  # inner() uses x from outer()

#     inner()
# x=100 #global scope variable
# outer()


from math import e
def func1():
    print(e) #built in scope varible as imported from a module
e=3 # global scope variable: that is why given priority LEGB
func1()


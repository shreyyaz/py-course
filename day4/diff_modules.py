#module = a file containing code u want to include in ur prgram
#use import to include a module built in or ur own
# print(help("modules"))
# print(help("math"))
# import math
# print(math.pi) #print pi from the math module

#can give alias to the module as well
# import math as m
# print(m.pi)

from math import e
print(e)

import example  #IMPORTING A SELF MADE MODULE.
print(example.square(2))
print(example.pi)
# QUIZ
# 
# In the function friction_coeff below, calculate 
# how the friction coefficient depends on the wheel 
# slip, then return that value.

import math

def friction_coeff(slip):
    return (-1.1*math.exp(-20*slip)) + (-0.4*slip + 1.1)
    ###### CHECK with some values of slip between 0. and 1.


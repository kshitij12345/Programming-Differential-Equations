# PROBLEM 1
#
# Modify the orbit function below to model
# one revolution of the moon around the earth,
# assuming that the orbit is circular.
#
# Use the math.cos(angle) and math.sin(angle) 
# functions in order to accomplish this.

import math
import numpy
import matplotlib.pyplot

moon_distance = 384e6 # m

def sin_cos():
    num_points = 50

    x = numpy.zeros(num_points+1)
    sin_x = numpy.zeros(num_points+1)
    cos_x = numpy.zeros(num_points+1)

    for i in range(num_points+1):
        x[i] = (2*math.pi*i/(num_points-1.))
        sin_x[i] = math.sin(x[i])
        cos_x[i] = math.cos(x[i])
    return x, sin_x, cos_x

def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    #print(x[:,0])
    
    for i in range(num_steps+1):
        angle = 2.*math.pi*i/num_steps
        x[i,0] = moon_distance*math.cos(angle)
        x[i,1] = moon_distance*math.sin(angle)
    
    #y,sin_x,cos_x = sin_cos()    
    #x[:,1] = moon_distance*sin_x
    #x[:,0] = moon_distance*cos_x
    
    
    #print (x)

    return x


x = orbit()

#@show_plot
def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()
plot_me()


# PROBLEM 5
# 
# We have a three-dimensional chaotic system.  Model this using the Lorenz system of equations
# and Heun's method with fixed step size.  Then improve upon the computation of the height
# and location of the local maxima by fitting each peak area with a parabola.  Call each newly
# calculated maximum z_current_local_max.  These will be added to a list.
#


from udacityplots import *

def lorenz_map():
    h = 0.02
    end_time = 1000.
    num_steps = int(end_time / h)
    times = h * numpy.array(range(num_steps + 1))

    sigma = 10.
    beta = 8. / 3.
    rho = 28.

    x = numpy.zeros(num_steps + 1)
    y = numpy.zeros(num_steps + 1)
    z = numpy.zeros(num_steps + 1)
    times = h * numpy.array(range(num_steps + 1))

    x[0] = 0.
    y[0] = 0.3 
    z[0] = 40.

    z_local_max_pairs = []
    z_previous_local_max = 0.
    got_previous = False
    
    for step in range(num_steps):
        # Task 1: Implement Heun's method (see Section 2.9) with fixed step size h for the Lorenz system.
        # Recall the Forwand Euler Method:
        xE = x[step] + h * sigma * (y[step] - x[step])
        yE = y[step] + h * (x[step] * (rho - z[step]) - y[step])
        zE = z[step] + h * (x[step] * y[step] - beta * z[step])
        
        x[step + 1] = x[step] + h* 0.5 * ( sigma * ( yE-xE + y[step] - x[step] ) )
        y[step + 1] = y[step] + h* 0.5 * ( xE * (rho - zE) - yE + x[step] * (rho - z[step]) - y[step] )
        z[step + 1] = z[step] + h* 0.5 * ( xE * yE - beta * zE + x[step] * y[step] - beta * z[step])
        # your code here

        if step > 0 and z[step + 1] < z[step] and z[step - 1] < z[step]:
            # Task 2: Improve this estimate of the local maximum value by fitting a quadratic parabola 
            # through z[step - 1], z[step], and z[step + 1]. 
            z[step] = z[step]
            z_current_local_max = z[step] # fill this in with a new estimate of the local maximum value
                     
            if got_previous:
                z_local_max_pairs.append([z_previous_local_max, z_current_local_max])
            z_previous_local_max = z_current_local_max
            got_previous = True
  
    return times, x, y, z, z_local_max_pairs

times, x, y, z, z_local_max_pairs = lorenz_map()

@show_plot
def plot_lorenz():
    axes = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(times[:2000], z[:2000]) # only a part of the data to more clearly show the growing oscillations
    axes.set_xlabel('Time')
    axes.set_ylabel('z')

    axes = matplotlib.pyplot.subplot(212)
    zp = numpy.array(z_local_max_pairs)
    matplotlib.pyplot.scatter(zp[:, 0], zp[:, 1], s = 2., facecolor = 'r', edgecolor = 'none')
    matplotlib.pyplot.axis('equal')
    axes.set_xlabel('Previous local max of z')
    axes.set_ylabel('Current local max of z')

plot_lorenz()



# QUIZ
# 
# Experiment with the parameter h, setting 
# it to a value that causes the seir_model 
# function to return highly unstable behavior.
# One decimal place is enough accuracy.

from udacityplots import *

###Modify the h variable below.
h = 2 # days
end_time = 60. # days
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def seir_model():
    transmission_coeff = 5e-9 # 1 / day person
    latency_time = 1. # days
    infectious_time = 5. # days

    s = numpy.zeros(num_steps + 1)
    e = numpy.zeros(num_steps + 1)
    i = numpy.zeros(num_steps + 1)
    r = numpy.zeros(num_steps + 1)

    s[0] = 1e8 - 1e6 - 1e5
    e[0] = 0.
    i[0] = 1e5
    r[0] = 1e6

    for step in range(num_steps):
        s2e = h * transmission_coeff * s[step] * i[step]
        e2i = h / latency_time * e[step]
        i2r = h / infectious_time * i[step]    
        # Note that the conservation of the total number (up to roundoff) is obvious when writing the equations this way.
        s[step + 1] = s[step] - s2e
        e[step + 1] = e[step] + s2e - e2i
        i[step + 1] = i[step] + e2i - i2r
        r[step + 1] = r[step] + i2r

    return s, e, i, r

s, e, i, r = seir_model()

@show_plot
def plot_me():
    s_plot = matplotlib.pyplot.plot(times, s)
    e_plot = matplotlib.pyplot.plot(times, e)
    i_plot = matplotlib.pyplot.plot(times, i)
    r_plot = matplotlib.pyplot.plot(times, r)
    matplotlib.pyplot.legend(('S', 'E', 'I', 'R'), loc = 'upper right')
    
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Time in days')
    axes.set_ylabel('Number of persons')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)

plot_me()



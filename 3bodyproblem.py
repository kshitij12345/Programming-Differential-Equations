# PROBLEM 4
#
# We have three stars in a three-dimensional space.  Use the symplectic
# Euler method to show how the position and velocity of these stars change
# with time.
#

from udacityplots import *
from mpl_toolkits.mplot3d import Axes3D

star_1_mass = 1e30 # kg
star_2_mass = 2e30 # kg
star_3_mass = 3e30 # kg
gravitational_constant = 6.67e-11 # m3 / kg s2

end_time = 10. * 365.26 * 24. * 3600. # s
h = 2. * 3600. # s
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def acceleration(position,mass):
    return -gravitational_constant * mass / numpy.linalg.norm(position)**3 * position



def three_body_problem():
    
    # three indices: which time, which star, xyz
    positions = numpy.zeros([num_steps + 1, 3, 3]) # m
    velocities = numpy.zeros([num_steps + 1, 3, 3]) # m / s
    positions[0] = numpy.array([[1., 3., 2.], [6., -5., 4.], [7., 8., -7.]]) * 1e11
    velocities[0] = numpy.array([[-2., 0.5, 5.], [7., 0.5, 2.], [-4., -0.5, -3.]]) * 1e3    
    
    for step in range(num_steps):
        # Task: Implement the symplectic Euler Method for the motion 
        # of three stars with the data provided above.
        positions[step+1] = positions[step] + h * velocities[step]
        #print(acceleration(positions[step+1][0]-positions[step+1][1],star_2_mass).shape)
        velocities[step+1][0] = velocities[step][0] + h *(acceleration(positions[step+1][0]-positions[step+1][1],star_2_mass)\
                                + acceleration(positions[step+1][0]-positions[step+1][2],star_3_mass))
        
        velocities[step+1][1] = velocities[step][1] + h *( acceleration(positions[step+1][1]-positions[step+1][0],star_1_mass)\
                                + acceleration(positions[step+1][1]-positions[step+1][2],star_3_mass))
        
        velocities[step+1][2] = velocities[step][2] + h *( acceleration(positions[step+1][2]-positions[step+1][0],star_1_mass)\
                                + acceleration(positions[step+1][2]-positions[step+1][1],star_2_mass))
        
         
        
    return positions, velocities

positions, velocities = three_body_problem()

@show_plot
def plot_stars():
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('x in m')
    axes.set_ylabel('z in m')
    axes.plot(positions[:, 0, 0], positions[:, 0, 2])
    axes.plot(positions[:, 1, 0], positions[:, 1, 2])
    axes.plot(positions[:, 2, 0], positions[:, 2, 2])
    matplotlib.pyplot.axis('equal')
    
plot_stars()



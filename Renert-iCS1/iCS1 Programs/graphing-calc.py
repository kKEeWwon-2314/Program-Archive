import stddraw
import math

# the functions we wish to plot
def f(x):
    return x ** 2

def g(x):
    return (x**2) * math.tan(x**2) 


def generate_x_coordinates(x_min, x_max, steps):
    """
    Generate and return an array of x-values that are between x_min
    and x_max (inclusive) with given number of steps in between.
    """
    # calculate the x step size
    x_step = (x_max - x_min) / steps
    
    # repeat for (steps+1) times:
    x_coords = []
    for i in range(steps+1):
        # calculate this x value and append to an array
        x = x_min + i * x_step
        x_coords.append(x)

    return x_coords


def plot_coordinates(x_coords, y_coords, colour, pen_radius):
    """
    Draws a series of line segments to connect the coordinates given in
    x_coords and y_coords.
    """
    stddraw.setPenColor(colour)
    stddraw.setPenRadius(pen_radius)
    for i in range(len(x_coords)-1):
        stddraw.line(x_coords[i], y_coords[i], x_coords[i+1], y_coords[i+1])


# define the domain and range over which we want to plot
x_min = -8
x_max = +8
y_min = -8
y_max = +8
stddraw.setXscale(x_min, x_max)
stddraw.setYscale(y_min, y_max)
stddraw.setCanvasSize(800, 800)

# choose a bunch of points on the function
steps = 300
x_coords = generate_x_coordinates(x_min, x_max, steps)

# evaluate functions to get y-coordinates
y_coords_for_f = []
for x in x_coords:
    y = f(x)
    y_coords_for_f.append(y)

y_coords_for_g = []
for x in x_coords:
    y = g(x)
    y_coords_for_g.append(y)

# draw coordinate axes
stddraw.setPenColor(stddraw.GRAY)
stddraw.setPenRadius(0.01)
stddraw.line(x_min, 0, x_max, 0)    # x-axis
stddraw.line(0, y_min, 0, y_max)    # y-axis

# call our functions to draw line segments connecting the points
plot_coordinates(x_coords, y_coords_for_f, stddraw.DARK_RED, 0.1)
plot_coordinates(x_coords, y_coords_for_g, stddraw.BOOK_BLUE, 0.03)

# draw some text to annotate the curves
stddraw.setFontSize(32)
stddraw.setPenColor(stddraw.DARK_RED)
stddraw.text(0, 2, 'y = x\u00b2')   # \u00b2 unicode for superscript 2
stddraw.setPenColor(stddraw.BOOK_BLUE)
stddraw.text(1.5, -5.5, 'y = x\u00b2 tan(x\u00b2)')

# show our beautiful graph to end the program
stddraw.show()
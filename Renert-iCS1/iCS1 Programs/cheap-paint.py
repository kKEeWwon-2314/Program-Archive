"""
One unbelieveably cheape paint program that will make you cringe!
NOTE: These colours are "constant" arrays of values, meaning they are
not meant to modified during the program's run, and are an example of 
an acceptable use of global variables accessible to functions. The 
convention is to use ALL CAPS for constants.
"""
import stddraw

COLOUR_KEYS = 'rgbk'
COLOURS = [stddraw.RED, stddraw.GREEN, stddraw.BLUE, stddraw.BLACK]


def colour_from_letter(letter):
    """
    Returns a colour from our palette given a corresponding letter
    from a key press.
    """
    colour_index = COLOUR_KEYS.index(letter)
    return COLOURS[colour_index]


# our paint program's state
circle_radius = 0.01
selected_colour = stddraw.BLACK
drawing_mode = 'circles'

last_mouse_x = 0.0
last_mouse_y = 0.0

# set up our main event processing loop
want_to_quit = False
while not want_to_quit:
    # 1. check for and process events

    # respond to key press events if any
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        print(key)
        if key == 'q':
            want_to_quit = True
        # press C to clear
        elif key == 'c':
            stddraw.clear()
        # use the number keys to change the size of our circle
        elif key.isdigit():
            circle_radius = float(key) / 100.0
        # use any of the keys in COLOUR_KEYS to select a new colour
        elif key in COLOUR_KEYS:
            selected_colour = colour_from_letter(key)
        # use the L and O keys to switch to line or circle drawing mode
        elif key == 'l':
            drawing_mode = 'lines'
        elif key == 'o':
            drawing_mode = 'circles'
    
    # respond to mouse click events if any
    if stddraw.mousePressed():
        x = stddraw.mouseX()
        y = stddraw.mouseY()
        stddraw.setPenColor(selected_colour)
        # if we are in circle-drawing mode, draw circle at clicked position
        if drawing_mode == 'circles':
            stddraw.filledCircle(x, y, circle_radius)
        # if we are in line-drawing mode, connect the last point with new one
        elif drawing_mode == 'lines':
            stddraw.line(last_mouse_x, last_mouse_y, x, y)
            last_mouse_x = x
            last_mouse_y = y

    # 2. do other fast computations and update visual output

    # draw a white rectangle over our previous mode indicator text
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0.0, 0.0, 1.0, 0.05)

    # switch back to black and write a message indicating the drawing mode
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setFontSize(20)
    stddraw.text(0.5, .02, drawing_mode + ' mode')

    # show updated drawing to the screen and request to get control back as soon as the show operation completes
    stddraw.show(0.0)
from PIL import Image, ImageDraw
import math


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_colour = 255
        self.im = Image.new('HSV',( self.width, self.height),( self.background_colour, self.background_colour, self.background_colour))
        self.idraw = ImageDraw.Draw( self.im )

    def setPixel( self, x, y, hue, saturation, value ):
        self.idraw.point( [x, y], (hue, saturation, value) )

    def visualise( self ):
        self.im.show()


def p5jsMap(n, start1, stop1, start2, stop2):
    # Mock functionality of the p5.js map() function
    # converts n from the start1/stop1 scale to the start2/stop2 scale

    return float( ( ( ( stop2 - start2 ) / ( stop1 - start1 ) ) * n ) + start2 )



def apply_mandelbrot_set( my_canvas, a_start, a_end, b_start, b_end):

    max_iterations = 250
    break_threshold = 16

    for x in range( 0, my_canvas.width ):
        for y in range( 0, my_canvas.height ):

            # Compute the values of a and b we will use to render a colour at position x,y on the canvas
            # The a and b values are the values tested to see if they remain bounded or tend to infinity
            a = p5jsMap( x, 0, my_canvas.width, a_start, a_end )
            b = p5jsMap( y, 0, my_canvas.height, b_start, b_end )

            # Remember the original values
            ca = a;
            cb = b;

            # Run through iterations and calculate solutions
            n = 0;
            for n in range( 0, max_iterations ):

                # Do the math
                # (a^2 - b^2) + 2abi
                aa = a * a - b * b
                bb = 2 * a * b
                a = aa + ca
                b = bb + cb

                # Does this tend to infinity?
                # If so jump out of this pixel
                break_value = a * a + b * b
                if break_value > break_threshold:
                    break

            # Calculate the hue and value for this pixel
            hue = int(255 * n / max_iterations)
            saturation = 255

            value = 0
            if n < max_iterations:
                value = 255 
            
            # Set the pixel value 
            my_canvas.setPixel( x, y, hue, saturation, value )

            # print "x=" + str(x) + " y=" + str(y) + " a=" + str(a) + " b=" + str(b) + " h=" + str(hue) + " s=" + str(saturation) + " v=" + str(value)


# This is the control code
# Everything above are just definitions

print("Starting Mandelbrot process")
print("Processing...")

my_canvas = Canvas( 800, 800 )
apply_mandelbrot_set( my_canvas, -2.0, 2.0, -2.0, 2.0 )
my_canvas.visualise()

print("Completed Mandelbrot process")


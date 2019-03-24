from PIL import Image, ImageDraw
import math


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_colour = 255
        self.im = Image.new('RGB',( self.width, self.height),( self.background_colour, self.background_colour, self.background_colour))
        self.idraw = ImageDraw.Draw( self.im )

    def setPixel( self, x, y, brightness):
        opacity = 255
        brightness = int( brightness )
        fill_colour = ( brightness, brightness, brightness, opacity )
        self.idraw.point( (x, y), fill_colour )

    def visualise( self ):
        self.im.show()


def p5jsMap(n, start1, stop1, start2, stop2):
    # Mock functionality of the p5.js map() function
    # converts n from the start1/stop1 scale to the start2/stop2 scale

    return float( ( ( ( stop2 - start2 ) / ( stop1 - start1 ) ) * n ) + start2 )



def apply_mandelbrot_set( my_canvas, start, stop ):
    a_start = start
    a_end = stop

    b_start = start
    b_end = stop

    max_iterations = 100
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

            # Calculate the brightness for this pixel
            # Could be improved by generating colour instead
            if (n == max_iterations):
                brightness = 0
            else:
                brightness = p5jsMap( n, 0.0, max_iterations, 0.0, 1.0 );
                brightness = p5jsMap( math.sqrt( brightness ), 0.0, 1.0, 0.0, 255.0 );

            # Set the pixel at x,y to the calculated brightness level
            my_canvas.setPixel( x, y, brightness)



# This is the control code
# Everything above are just definitions

print("Starting Mandelbrot process")
print("Processing...")

my_canvas = Canvas( 600, 600 )
apply_mandelbrot_set( my_canvas, 0.25, 0.50 )
my_canvas.visualise()

print("Completed Mandelbrot process")


import numpy as np

def calculate_if_is_in_mbot_set(Comp):
	# We receive a complex number as an input and return a 
	# boolean value indicating if it is in the Mandelbrot set.

	# Spoof by returning true for even numbers

	Z=np.zeros(C.shape, np.complex64)
	Re = np.linspace(xmin, xmax, xn, dtype=np.float32)
	Imag = np.linspace(ymix, ymax, yn, dtype=np.float32)
        C = Re + Imag
        C**2 = Re**2 - Imag**2 + 2*Re*Imag
        maxiter = 100
	while Comp <= maxiter:
                xmin, xmax, xn = -2.25, +0.75, 3000/2
                ymin, ymax, yn = -1.25, +1.25, 2500/2
                
                Z = 0.0
                
                C = -1

                Z = Z**2 + C

                Z = C**2 + C

                C**2 = (C**2 + C) 
                
                Z = C**2 + C 
                
		return True
	else:
                break
        
                return False


def visualise_answer( is_in_set ):
	# We visualise the result of an iteration

	if is_in_mbot_set: 
		 print str(Comp) + " Is in the Mandelbrot set"
	else:
                 print str(Comp) + " Is not in the Mandelbrot set"





while Comp <= maxiter:

  is_in_mbot_set = calculate_if_is_in_mbot_set( Comp )
  visualise_answer( is_in_mbot_set )
  Comp = Comp + 1

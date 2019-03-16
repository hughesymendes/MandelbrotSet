

def calculate_if_is_in_mbot_set( complex ):
	# We receive a complex number as an input and return a 
	# boolean value indicating if it is in the Mandrelbot set.

	# Spoof by returning true for even numbers

	if complex % 2 == 0:
		return True
	else:
		return False


def visualise_answer( is_in_set ):
	# We visualise the result of an iteration

	if is_in_set:
		 print str(complex) + " is in the Mandelbrot set"
	else:
	 print str(complex) + " is not in the Mandelbrot set"




complex = 1
while complex <= 100:

  is_in_mbot_set = calculate_if_is_in_mbot_set( complex )
  visualise_answer( is_in_mbot_set )
  complex = complex + 1

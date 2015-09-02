# Implement a function reverses a null- terminated string.
import sys

def reverse_string(input_str):
	"""
	Reverse the input string and return it
	"""
	return input_str[::-1]

if __name__ == "__main__":
	
	if len(sys.argv) != 2:
		print "Usage: python reverse_string.py <test_string>"
		exit(-1)
	
	s = sys.argv[1]
	reversed_str = reverse_string(s)
	print "Reversed string is: " + reversed_str


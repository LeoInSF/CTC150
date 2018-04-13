import sys
def unique_string(input_string):
	if not input_string:
		return 
	else:    
		str_list = list(input_string)
		unique_char = set(str_list)
		if len(str_list) == len(unique_char):
		    return True
		else:
		    return False

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Usage: python unique_string.py <String>"
		exit(-1)	
	s = sys.argv[1]
	result = unique_string(s)
	if result:
	    print "Unique string: " + s
	elif result is None:
	    print "Empty string, please provide valid string for validification" 
	else:
	    print "Duplicated string: " + s


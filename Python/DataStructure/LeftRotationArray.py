

# Function to leftRotate array multiple times


def leftRotate(arr, n, k):

	# get the start point of array rotated
	mod = k % n
	s = ""

	# Prints the rotated array from position at start
	for i in range(n):
		print str(arr[(mod + i) % n]),
	print
	return


# global variables
arr = [1, 6, 5, 8, 11]
n = len(arr)
k = 2

# Function Call
leftRotate(arr, n, k)



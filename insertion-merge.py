import random, time

############################################################

# merge function implementation

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

############################################################

# merge sort implementation

def mergeSort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) / 2
        a = mergeSort(x[:middle])
        b = mergeSort(x[middle:])
        return merge(a, b)
	
############################################################

# insertion sort implementation

def insertionSort(toSort):
	for i in range(1, len(toSort)):  # [1 to n-1]

		temp = toSort[i]
		j = i

		while j > 0 and toSort[j - 1] > temp:
			toSort[j] = toSort[j - 1]
			j -= 1

		toSort[j] = temp

############################################################
	
# generate sorted lists

ul = []

for n in range(1000, 11000, 1000):
	
	a = [i for i in xrange(n)]
	ul.append(a)
			
############################################################
	
# run the merge sort algorithm on the unsorted lists

#print "running merge sort on unsorted lists"
#
#t1 = time.time()
#mergeSort(list_1)
#print("%s" % (time.time() - t1))
#
#t2 = time.time()
#mergeSort(list_2)
#print("%s" % (time.time() - t2))
#
#t3 = time.time()
#mergeSort(list_3)
#print("%s" % (time.time() - t3))
#
#t4 = time.time()
#mergeSort(list_4)
#print("%s" % (time.time() - t4))
#
#t5 = time.time()
#mergeSort(list_5)
#print("%s" % (time.time() - t5))
#
#t6 = time.time()
#mergeSort(list_6)
#print("%s" % (time.time() - t6))
#
#t7 = time.time()
#mergeSort(list_7)
#print("%s" % (time.time() - t7))
#
#t8 = time.time()
#mergeSort(list_8)
#print("%s" % (time.time() - t8))
#
#t9 = time.time()
#mergeSort(list_9)
#print("%s" % (time.time() - t9))
#
#t10 = time.time()
#mergeSort(list_10)
#print("%s" % (time.time() - t10))

############################################################

# randomly swap two elements in an array
	
def swap(array):
	
	# randomly select two unique indices
	i = random.randint(0, len(array) - 1)
	j = random.randint(0, len(array) - 1)
	
	# make sure you're not swapping the same element
	while (j == i):
		j = random.randint(0, len(array) - 1)
		
	# swap the two elements
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

# generate semi-sorted lists

ul = []

for n in range(1000, 11000, 1000):
#	a = [i for i in xrange(n / 8)]    # first portion of list
#	random.shuffle(a)             # shuffle first portion of list
#	
#	b = [i for i in xrange(n / 8, n)] # second portion of list
#	ul.append(a + b)

	c = [i for i in xrange(n)]
	percent = 0.5  # percentage of shuffled array elements
	for i in range(0, int(n * percent)):
		swap(c)
	#print c
	ul.append(c)
	
############################################################

# run the insertion sort algorithm on the semi-sorted lists
	
print "\nrunning insertion sort on semi-sorted lists"

for i in range(0, 10):
	t = time.time()
	#print ul[i]
	insertionSort(ul[i])
	print("%s" % (time.time() - t))

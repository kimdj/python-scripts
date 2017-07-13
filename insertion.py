import random, time

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
		
## generate unsorted lists
#
#list_1 = [i for i in xrange(1000)]  # create an array
#random.shuffle(list_1)  # shuffle the array
#
#list_2 = [i for i in xrange(2000)]  # create an array
#random.shuffle(list_2)  # shuffle the array
#
#list_3 = [i for i in xrange(3000)]  # create an array
#random.shuffle(list_3)  # shuffle the array
#
#list_4 = [i for i in xrange(4000)]  # create an array
#random.shuffle(list_4)  # shuffle the array
#
#list_5 = [i for i in xrange(5000)]  # create an array
#random.shuffle(list_5)  # shuffle the array
#
#list_6 = [i for i in xrange(6000)]  # create an array
#random.shuffle(list_6)  # shuffle the array
#
#list_7 = [i for i in xrange(7000)]  # create an array
#random.shuffle(list_7)  # shuffle the array
#
#list_8 = [i for i in xrange(8000)]  # create an array
#random.shuffle(list_8)  # shuffle the array
#
#list_9 = [i for i in xrange(9000)]  # create an array
#random.shuffle(list_9)  # shuffle the array
#
#list_10 = [i for i in xrange(10000)]  # create an array
#random.shuffle(list_10)  # shuffle the array
#			
#############################################################
#	
## run the insertion sort algorithm on the unsorted lists
#
#print "running insertion sort on unsorted lists"
#
#t1 = time.time()
#insertionSort(list_1)
#print("%s" % (time.time() - t1))
#
#t2 = time.time()
#insertionSort(list_2)
#print("%s" % (time.time() - t2))
#
#t3 = time.time()
#insertionSort(list_3)
#print("%s" % (time.time() - t3))
#
#t4 = time.time()
#insertionSort(list_4)
#print("%s" % (time.time() - t4))
#
#t5 = time.time()
#insertionSort(list_5)
#print("%s" % (time.time() - t5))
#
#t6 = time.time()
#insertionSort(list_6)
#print("%s" % (time.time() - t6))
#
#t7 = time.time()
#insertionSort(list_7)
#print("%s" % (time.time() - t7))
#
#t8 = time.time()
#insertionSort(list_8)
#print("%s" % (time.time() - t8))
#
#t9 = time.time()
#insertionSort(list_9)
#print("%s" % (time.time() - t9))
#
#t10 = time.time()
#insertionSort(list_10)
#print("%s" % (time.time() - t10))
#
#############################################################
#
## generate sorted lists
#
#u_list_1 = [i for i in xrange(1000)]  # create an array
#u_list_2 = [i for i in xrange(2000)]  # create an array
#u_list_3 = [i for i in xrange(3000)]  # create an array
#u_list_4 = [i for i in xrange(4000)]  # create an array
#u_list_5 = [i for i in xrange(5000)]  # create an array
#u_list_6 = [i for i in xrange(6000)]  # create an array
#u_list_7 = [i for i in xrange(7000)]  # create an array
#u_list_8 = [i for i in xrange(8000)]  # create an array
#u_list_9 = [i for i in xrange(9000)]  # create an array
#u_list_10 = [i for i in xrange(10000)]  # create an array
#
#############################################################
#
## run the insertion sort algorithm on the sorted lists
#	
#print "\nrunning insertion sort on sorted lists"
#	
#t1 = time.time()
#insertionSort(u_list_1)
#print("%s" % (time.time() - t1))
#
#t2 = time.time()
#insertionSort(u_list_2)
#print("%s" % (time.time() - t2))
#
#t3 = time.time()
#insertionSort(u_list_3)
#print("%s" % (time.time() - t3))
#
#t4 = time.time()
#insertionSort(u_list_4)
#print("%s" % (time.time() - t4))
#
#t5 = time.time()
#insertionSort(u_list_5)
#print("%s" % (time.time() - t5))
#
#t6 = time.time()
#insertionSort(u_list_6)
#print("%s" % (time.time() - t6))
#
#t7 = time.time()
#insertionSort(u_list_7)
#print("%s" % (time.time() - t7))
#
#t8 = time.time()
#insertionSort(u_list_8)
#print("%s" % (time.time() - t8))
#
#t9 = time.time()
#insertionSort(u_list_9)
#print("%s" % (time.time() - t9))
#
#t10 = time.time()
#insertionSort(u_list_10)
#print("%s" % (time.time() - t10))

############################################################

# generate semi-sorted lists

ul = []
x = 0

for n in range(1000, 11000, 1000):
	a = [i for i in xrange(n / 2)]    # first portion of list
	b = [i for i in xrange(n / 2, n)] # second portion of list
	random.shuffle(b)             # shuffle second portion of list
	
	ul.append(a + b)
	x += 1

############################################################

# run the insertion sort algorithm on the semi-sorted lists
	
print "\nrunning insertion sort on semi-sorted lists"

t1 = time.time()
insertionSort(ul[0])
print("%s" % (time.time() - t1))

t2 = time.time()
insertionSort(ul[1])
print("%s" % (time.time() - t2))

t3 = time.time()
insertionSort(ul[2])
print("%s" % (time.time() - t3))

t4 = time.time()
insertionSort(ul[3])
print("%s" % (time.time() - t4))

t5 = time.time()
insertionSort(ul[4])
print("%s" % (time.time() - t5))

t6 = time.time()
insertionSort(ul[5])
print("%s" % (time.time() - t6))

t7 = time.time()
insertionSort(ul[6])
print("%s" % (time.time() - t7))

t8 = time.time()
insertionSort(ul[7])
print("%s" % (time.time() - t8))

t9 = time.time()
insertionSort(ul[8])
print("%s" % (time.time() - t9))

t10 = time.time()
insertionSort(ul[9])
print("%s" % (time.time() - t10))

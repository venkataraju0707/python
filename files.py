"""def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')"""


"""# Python program to demonstrate
# the working of islice

from itertools import islice


# Slicing the range function
for i in islice(range(20), 5,10): 
	print(i)
	
	
li = [2, 4, 5, 7, 8, 10, 20] 

# Slicing the list
print(list(islice(li, 1, 6, 2))) """



def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',4)



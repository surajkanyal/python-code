import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    # array = [float(i) for i in arr]
    # array = array[::-1]
    x = numpy.array(arr[::-1],dtype='float')
    return x
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
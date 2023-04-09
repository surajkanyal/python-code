import numpy
numpy.set_printoptions(legacy = '1.13')
ele_list = list(map(float,input().split()))
my_array = numpy.array(ele_list)
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))
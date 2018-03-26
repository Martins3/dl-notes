import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print(a) 
print(a.shape) # not lelements in array,but the every dimentions for a  tensor
print(type(a))
a[0] = 100
print(a)  # Change an element of the array

b = np.array([[1,2,3],[4,5,6]])
print(b.shape) 
print(type(b))

# Numpy also provides many functions to create arrays:
zeros = np.zeros((3, 3))
print(zeros)

ones = np.ones((3, 3))
print(ones)

eye = np.eye(3)
print(eye)

e = np.random.random((2,3)) # Create an array filled with random values
print(e)  

# array index
sil = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
t_sil = sil[1: , 0:2]
print("the primitive: ", sil)
print("after silcing: ", t_sil)      

# we can mix the index and the slice together
only_sil = sil[1:2, 0:]
print("silce: ", only_sil, only_sil.shape)
mix_sil_and_index = sil[1, 0:]
print("mix:", mix_sil_and_index, mix_sil_and_index.shape)

 # integer array indexing allows you to construct arbitrary arrays using the data from another array
integer_array_index = np.array([[1,2], [3, 4], [5, 6]])
a = integer_array_index
print("integer array indexing: ", integer_array_index[[0, 1, 2], [0, 1, 0]] ) # Prints "[1 4 5]"
print("this is the same as: ", np.array([a[0,0], a[1, 1], a[2,0]])) # Prints "[1 4 5]"

# the trick is selecting or mutating one element from each row of a matrix
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(a)

# Create an array of indices
b = np.array([0, 2, 0, 1])

# Select one element from each row of a using the indices in b
print(a[np.arange(4), b]) # Prints "[ 1  6  7 11]"

# Mutate one element from each row of a using the indices in b
# i had thought that it is forbiden for python to write code as below
a[np.arange(4), b] += 10
print(a)

#Boolean array indexing:
#  Boolean array indexing lets you pick out arbitrary elements of an array. 
# Frequently this type of indexing is used to select the elements of an array that satisfy some condition.
a = np.array([[1, 2 ,3], [4, 5, 6], [7, 8 ,9]])
print(a>2)
b = a[a>2]
print(b)

## -------------------------------------------data types ---------------------------------------------------------------------
# Every numpy array is a grid of elements of the same type
# numpy tries to guess a datatype when you create an array, but functions that
# construct arrays usually also include an optional argument to explicitly specify the datatype
x = np.array([1, 2])  # Let numpy choose the datatype
print(x.dtype)         # Prints "int64"

x = np.array([1.0, 2.0])  # Let numpy choose the datatype
print(x.dtype)             # Prints "float64"

x = np.array([1, 2], dtype=np.float64)  # Force a particular datatype
print(x.dtype)                         # Prints "flaot 64"


# basic operation on array are supported 
# can be  operator overloads and functions
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print("basic operation on the array!")
print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))

# what should care about is is that( * ) doesn't mean the matric product ,and we that' s the dot 
# dot can be apply in two different way
# becasue numpy support the vector * vector, so some expression make me kind of confused
x = np.array([[1,10],[100,1000]])
y = np.array([[2,4],[8,12]])

v = np.array([9,10])
w = np.array([11, 12])

print("there are  matric product")
print("m-m:", x.dot(y))
print("m-m:", np.dot(y,x))

print("m-v:", x.dot(v))


print("elementwise:")
print(x*y)

# sum 
x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0)) # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1)) # Compute sum of each row; prints "[3 7]"

# matric transform
x = np.array([[1,2], [3,4]])
print("orginal:\n", x, "after transpose: \n", x.T)
# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print("orginal:", v, "after transpose: ", v.T)

#-----------------------------------------Broadcasting--------------------------------------------------------
#Broadcasting two arrays together follows these rules:

# have different dimentions
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([-1, -2, -3])
print(a+b)

# we can really understand  the matric when we loook insight into the parameter shape
v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
print("change vector into matric and do outer product:\n", np.reshape(v, (3, 1)) * w)

# what's shape
print("1, 2: \n", np.reshape(w,(1,2)))
print("2, 3: \n",np.reshape(w,(2,1)))
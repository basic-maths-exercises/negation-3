import numpy as np

def numberOutside( data, a, b ) :
  nnn = 0
  for d in data : 
    if d<a or d>b : nnn = nnn + 1 
  return nnn
  
def negationOutside( data, a, b ) :
  # Your code goes here
  

# These lines of code allow you to check your code is working
data = np.loadtxt("mydata.dat")
print(numberOutside(data,3,7), "should equal", len(data) - negationOutside(data,3,7))

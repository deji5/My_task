###### MODULARIZING YOUR CODE 2
# Different Ways to Import module
# 1. Import the whole module
            #   square root function
import math
# Lets put it to use

print(math.sqrt(9))

# import as an alias
import math as m

print(m.sqrt(25))

# 3. Import specific function or variables
from math import sqrt, pi

print(sqrt(36))
print(pi)

# 4. Import everything from the module
from math import *

print(sqrt(49))
print(pi)


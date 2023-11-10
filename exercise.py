# Create a 5 x 5 ndarray X with consecutive integers from 1 to 25 (inclusive). Afterwards use Boolean indexing to pick out only the odd numbers in the array and assign the result to Y.


import numpy as np

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25
X = np.arange(1, 26).reshape(5, 5)

# Use Boolean indexing to pick out only the odd numbers
Y = X[X % 2 != 0]

print("Original Array (X):\n", X)
print("\nArray with Odd Numbers (Y):\n", Y)
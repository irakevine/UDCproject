# Create a 5 x 5 ndarray X with consecutive integers from 1 to 25 (inclusive). Afterwards use Boolean indexing to pick out only the odd numbers in the array and assign the result to Y.


import numpy as np

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25
X = np.arange(1, 26).reshape(5, 5)

# Use Boolean indexing to pick out only the odd numbers
Y = X[X % 2 != 0]

print("Original Array (X):\n", X)
print("\nArray with Odd Numbers (Y):\n", Y)



# What are the weights and bias for the AND perceptron?
# Set the weights (and_weight1, and_weight2) and bias (and_bias) to values that will correctly determine the AND operation as shown above. More than one set of values will work!:"

# TODO: Set and_weight1, and_weight2, and and_bias
and_weight1 = 0.0
and_weight2 = 0.0
and_bias = 0.0


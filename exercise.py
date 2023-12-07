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

and_weight1 = 0.5
and_weight2 = 0.5
and_bias = -0.7

# What are the weights and bias for the NOT perceptron?
# Set the weights (not_weight1, not_weight2) and bias not_bias to the values that calculate the NOT operation on the second input and ignores the first input.:"


# And now, your time to shine! Let's code the formula for the Softmax function in Python.
# TODO: Set not_weight1, not_weight2, and not_bias
not_weight1 = 0.0
not_weight2 = 0.0
not_bias = 0.0


not_weight1 = 0.0  # Ignored input
not_weight2 = -1.0  # Weight for the second input
not_bias = 0.5  # Bias

import numpy as np

def softmax(L):
    """
    This function takes as input a list of numbers, and returns the list
    of values given by the softmax function.
    """
    exp_L = np.exp(L)
    sum_exp_L = np.sum(exp_L)
    probabilities = exp_L / sum_exp_L
    return probabilities

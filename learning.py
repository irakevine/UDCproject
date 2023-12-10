# # Use a list comprehension to create tick_names that we will apply to the tick labels. 
# # Pick each element `v` from the `tick_props`, and convert it into a formatted string.
# # `{:0.2f}` denotes that before formatting, we 2 digits of precision and `f` is used to represent floating point number.
# # Refer [here](https://docs.python.org/2/library/string.html#format-string-syntax) for more details
# tick_names = ['{:0.2f}'.format(v) for v in tick_props]
# tick_names


# # Example 2 - Step 4. Plot the bar chart, with new x-tick labels 

# sb.countplot(data=pkmn_types, y='type', color=base_color, order=type_order);
# # Change the tick locations and labels
# plt.xticks(tick_props * n_pokemon, tick_names)
# plt.xlabel('proportion');

# # Example 3. Print the text (proportion) on the bars of a horizontal plot. 

# # Considering the same chart from the Example 1 above, print the text (proportion) on the bars
# base_color = sb.color_palette()[0]
# sb.countplot(data=pkmn_types, y='type', color=base_color, order=type_order);

# # Logic to print the proportion text on the bars
# for i in range (type_counts.shape[0]):
#     # Remember, type_counts contains the frequency of unique values in the `type` column in decreasing order.
#     count = type_counts[i]
#     # Convert count into a percentage, and then into string
#     pct_string = '{:0.1f}'.format(100*count/n_pokemon)
#     # Print the string value on the bar. 
#     # Read more about the arguments of text() function [here](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.text.html)
#     plt.text(count+1, i, pct_string, va='center')

# # Example 4. Print the text (proportion) below the bars of a Vertical plot.

# # Considering the same chart from the Example 1 above, print the text (proportion) BELOW the bars
# base_color = sb.color_palette()[0]
# sb.countplot(data=pkmn_types, x='type', color=base_color, order=type_order);


# # Recalculating the type_counts just to have clarity.
# type_counts = pkmn_types['type'].value_counts()

# # get the current tick locations and labels
# locs, labels = plt.xticks(rotation=90) 

# # loop through each pair of locations and labels
# for loc, label in zip(locs, labels):

#     # get the text property for the label to get the correct count
#     count = type_counts[label.get_text()]
#     pct_string = '{:0.1f}%'.format(100*count/n_pokemon)

#     # print the annotation just below the top of the bar
#     plt.text(loc, count+2, pct_string, ha = 'center', color = 'black')


# # import numpy as np
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import seaborn as sb
# # %matplotlib inline

# # # Read the data from a CSV file
# # # Original source of data: https://www.kaggle.com/manjeetsingh/retaildataset available under C0 1.0 Universal (CC0 1.0) Public Domain Dedication License
# # sales_data = pd.read_csv('sales_data.csv')
# # sales_data.head(10)
# # sales_data.shape
# # (8190, 12)

# # # Use either of the functions below
# # # sales_data.isna()
# # sales_data.isnull()

# # sales_data.isna().sum()

# # # Step 2 - Prepare a NaN tabular data

# # # Let's drop the column that do not have any NaN/None values
# # na_counts = sales_data.drop(['Date', 'Temperature', 'Fuel_Price'], axis=1).isna().sum()
# # print(na_counts)

# # Use seaborn.barplot()

# # Step 3 - Plot the bar chart from the NaN tabular data, and also print values on each bar 

# # The first argument to the function below contains the x-values (column names), the second argument the y-values (our counts).
# # Refer to the syntax and more example here - https://seaborn.pydata.org/generated/seaborn.barplot.html
# sb.barplot(na_counts.index.values, na_counts)

# # get the current tick locations and labels
# plt.xticks(rotation=90) 

# # Logic to print value on each bar
# for i in range (na_counts.shape[0]):
#     count = na_counts[i]
    
#     # Refer here for details of the text() - https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.text.html
#     plt.text(i, count+300, count, ha = 'center', va='top')


#     # Example 1 a. Scatter plot showing negative correlation between two variables


#     # TO DO: Necessary import

# # Read the CSV file
# fuel_econ = pd.read_csv('fuel_econ.csv')
# fuel_econ.head(10)

# # Scatter plot
# plt.scatter(data = fuel_econ, x = 'displ', y = 'comb');
# plt.xlabel('Displacement (1)')
# plt.ylabel('Combined Fuel Eff. (mpg)')

# # Example 3. Plot the regression line on the transformed data

# def log_trans(x, inverse = False):
#     if not inverse:
#         return np.log10(x)
#     else:
#         return np.power(10, x)

# sb.regplot(fuel_econ['displ'], fuel_econ['comb'].apply(log_trans))
# tick_locs = [10, 20, 50, 100]
# plt.yticks(log_trans(tick_locs), tick_locs);


import numpy as np
from data_prep import features, targets, features_test, targets_test
np.random.seed(21)
def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1 / (1 + np.exp(-x))
# Hyperparameters
n_hidden = 2  # number of hidden units
epochs = 900
learnrate = 0.005
n_records, n_features = features.shape
last_loss = None

# Initialize weights
weights_input_hidden = np.random.normal(scale=1 / n_features ** .5,
                                        size=(n_features, n_hidden))
weights_hidden_output = np.random.normal(scale=1 / n_features ** .5,
                                         size=n_hidden)
for e in range(epochs):
    del_w_input_hidden = np.zeros(weights_input_hidden.shape)
    del_w_hidden_output = np.zeros(weights_hidden_output.shape)
    for x, y in zip(features.values, targets):
        ## Forward pass ##
        # TODO: Calculate the output
        hidden_input = np.dot(x, weights_input_hidden)
        hidden_output = sigmoid(hidden_input)
        output = sigmoid(np.dot(hidden_output,
                                weights_hidden_output))

        ## Backward pass ##
        # TODO: Calculate the network's prediction error
        error = y - output
        # TODO: Calculate error term for the output unit
        output_error_term = error  *output*  (1 - output)

        ## propagate errors to hidden layer
        # TODO: Calculate the hidden layer's contribution to the error
        hidden_error = np.dot(output_error_term, weights_hidden_output)
        # TODO: Calculate the error term for the hidden layer
        hidden_error_term = hidden_error  *hidden_output*  (1 - hidden_output)
        # TODO: Update the change in weights
        del_w_hidden_output += output_error_term * hidden_output
        del_w_input_hidden += hidden_error_term * x[:, None]

    # TODO: Update weights
    weights_input_hidden += learnrate * del_w_input_hidden / n_records
    weights_hidden_output += learnrate * del_w_hidden_output / n_records

    # Printing out the mean square error on the training set
    if e % (epochs / 10) == 0:
        hidden_output = sigmoid(np.dot(x, weights_input_hidden))
        out = sigmoid(np.dot(hidden_output,
                             weights_hidden_output))
        loss = np.mean((out - targets) ** 2)
        if last_loss and last_loss < loss:
            print("Train loss: ", loss, "  WARNING - Loss Increasing")
        else:
            print("Train loss: ", loss)
        last_loss = loss

# Calculate accuracy on test data
hidden = sigmoid(np.dot(features_test, weights_input_hidden))
out = sigmoid(np.dot(hidden, weights_hidden_output))
predictions = out > 0.5
accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))
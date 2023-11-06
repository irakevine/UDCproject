# Write a script of your own
# Open up a brand new empty file in your text editor, name it and save it in the place where you're keeping the files for your Python learning. Put the following code into it.:"how_many_snakes = 1
# how_many_snakes = 3  # Change the number to the desired count of snakes

# snake_string = """
# Welcome to Python3!

#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/

# <3, Juno
# """

# print(snake_string * how_many_snakes)  # Use the variable directly, not as a string 'how_many_snakes'


# num=int(float(input('Enter a number :')) )

# print('hello'*num)

# names = input("Enter names separated by commas: ").title().split(",")
# assignments = input("Enter assignment counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")

# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))


#     While True:
# Try:    
# x= int(input('Enter a number:'))
#     break 
# except:
# print('That\'s not a valid number!)
# print('\nAttempted Input\n')


# Handling Input Errors
# The party_planner function below takes as input a number of party people and cookies and figures out how many cookies each person gets at the party, assuming equitable distribution of cookies. Then, it returns that number along with how many cookies will be left over.

# Right now, calling the function with an input of 0 people will cause an error, because it creates a ZeroDivisionError exception. Edit the party_planner function to handle this invalid input. If it runs into this exception, it should print a warning message to the user and request they input a different number of people.

# After you've edited the function, try running the file again and make sure it does what you intended. Try it with several different input values, including 0 and other values for the number of people.

# Using this workspace
# In some pages of our classroom, we'll provide you a workspace like the one below that will provide you a programming environment with a Terminal and code editor, so you can do all your work right here. Here are a few tips orienting you to this kind of workspace.

# On the top panel is a code editor where you can edit your Python file. Scroll up and down in this panel to see all the code. You can also expand or shrink this panel by clicking and dragging its bottom border.

# On the bottom panel, you can execute this Python file by clicking on New Terminal and entering python handling_errors.py on the command line.



def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")
    
    return(num_each, leftovers)

# f = open('test.py', 'r')
# file_data = f.read()
# f.close()
# print(file_data)

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

    print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()



# Function to create a dictionary from flowers.txt
def create_flower_dict():
    flower_dict = {}
    with open('flowers.txt', 'r') as file:
        for line in file:
            letter, flower = line.strip().split(': ')
            flower_dict[letter] = flower
    return flower_dict

# Function to ask for user's first and last name
def get_user_input():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name

# Function to match the user's first name with a flower name
def match_flower_name():
    first_name, _ = get_user_input()
    flower_dict = create_flower_dict()
    first_letter = first_name[0].lower()

    if first_letter in flower_dict:
        print(f"The flower name starting with '{first_letter.upper()}' is: {flower_dict[first_letter]}")
    else:
        print("Sorry, there's no flower name starting with that letter in the dictionary.")

# Main function
if __name__ == "__main__":
    match_flower_name()


class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount),


# Instantiating shirt_one and shirt_two
shirt_one = Shirt('red', 'S', 'long-sleeve', 25)
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

# Changing the price of shirt_one to 10
shirt_one.change_price(10)

# Calculating the total cost of shirt_one and shirt_two
total_cost = shirt_one.price + shirt_two.price

# Calculating the total cost after applying discounts to shirt_one and shirt_two
discount_shirt_one, = shirt_one.discount(0.14)  # Applying a 14% discount to shirt_one
discount_shirt_two, = shirt_two.discount(0.06)  # Applying a 6% discount to shirt_two
total_discount = discount_shirt_one + discount_shirt_two

# Running the tests
from tests import run_tests
shirt_one = Shirt("red", "S", "long-sleeve", 25)
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

def run_tests(shirt_one, shirt_two, total_cost, total_discount):

    # Unit tests to check your solution
    assert shirt_one.price == 25, 'shirt_one price should be 25'
    print("Shirt one price test passed.")
    assert shirt_two.price==10,'shirt_two price should be 10'
    print("Shirt two price test passed.")
    assert shirt_one.color == "red", ' shirt_one should be red'
    print("Shirt one color test passed.")
    assert shirt_two.color == "orange", ' shirt_two should be orange'  
    print("Shirt two color test passed.")
    
    assert shirt_one.style == 'long-sleeve', 'shirt_one should be long_sleeve style'
    print("Shirt one style test passed.")
    
    assert shirt_two.style == 'short-sleeve', 'shirt_two should be short_sleeve style'
    print("Shirt two style test passed.")
    # ...


run_tests(shirt_one, shirt_two, total_cost, total_discount)
   
  
# Write a SalesPerson class with the following characteristics:

# the class name should be SalesPerson
# the class attributes should include
# first_name
# last_name
# employee_id
# salary
# pants_sold
# total_sales
# the class should have an init function that initializes all of the attributes
# the class should have four methods
# sell_pants() a method to change the price attribute
# calculate_sales() a method to calculate the sales
# display_sales() a method to print out all the pants sold with nice formatting
# calculate_commission() a method to calculate the salesperson commission based on total sales and a percentage

class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants):
        self.pants_sold.append(pants)

    def display_sales(self):
        for pants in self.pants_sold:
            print(f"color: {pants.color}, waist_size: {pants.waist_size}, length: {pants.length}, price: {pants.price}")

    def calculate_sales(self):
        total = 0
        for pants in self.pants_sold:
            total += pants.price
        self.total_sales = total
        return self.total_sales

    def calculate_commission(self, percentage):
        return percentage * self.total_sales
    

#     Write a Pants class with the following characteristics:

# the class name should be Pants
# the class attributes should include
# color
# waist_size
# length
# price
# the class should have an init function that initializes all of the attributes
# the class should have two methods
# change_price() a method to change the price attribute
# discount() to calculate a discount

class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)
    

#     Docstrings and Object-Oriented Code
# Below is an example of a class with docstrings and a few things to keep in mind:

# Make sure to indent your docstrings correctly or the code will not run. A docstring should be indented one indentation underneath the class or method being described.
# You don't have to define 'self' in your method docstrings. It's understood that any method will have self as the first method input.

class Pants:
    """The Pants class represents an article of clothing sold in a store
    """

    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object

        Args: 
            new_price (float): the new price of the pants object

        Returns: None

        """
        self.price = new_price

    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)
    

    # Like in the previous question, assume the average weight of an American adult male is 180 pounds with a standard deviation of 34 pounds. The distribution of weights follows a normal distribution. What is the probability that a man weighs somewhere between 120 and 155 pounds = 0.19?

    # Now consider a Binomial distribution. Assume that 15% of the population is allergic to cats. If you randomly select 60 people for a medical trial, what is the probability that 7 of those people are allergic to cats = 0.12?

#     class Clothing:
#     def __init__(self, color, size, style, price):
#         self.color = color
#         self.size = size
#         self.style = style
#         self.price = price

#     def change_price(self, price):
#         self.price = price

#     def calculate_discount(self, discount):
#         return self.price * (1 - discount)

# class Shirt(Clothing):
#     def __init__(self, color, size, style, price, long_or_short):
#         Clothing.__init__(self, color, size, style, price)
#         self.long_or_short = long_or_short

#     def double_price(self):
#         self.price = 2*self.price

# class Pants(Clothing):
#     def __init__(self, color, size, style, price, waist):
#         Clothing.__init__(self, color, size, style, price)
#         self.waist = waist

#     def calculate_discount(self, discount):
#         return self.price * (1 - discount / 2)

# Distribution class
class Distribution:
    def __init__(self, mu=0, sigma=1):
        """ Generic distribution class for calculating and 
        visualizing a probability distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file

            """

        self.mean = mu
        self.stdev = sigma
        self.data = []

        # def read_data_file(self, file_name):
        # """Function to read in data from a txt file. The txt file should have
        # one number (float) per line. The numbers are stored in the data attribute.

        # Args:
        #     file_name (string): name of a file to read from

        # Returns:
        #     None

        # """

        # with open(file_name) as file:
        #     data_list = []
        #     line = file.readline()
        #     while line:
        #         data_list.append(int(line))
        #         line = file.readline()
        # file.close()

        # self.data = data_list

#         import math

# import matplotlib.pyplot as plt

# class Gaussian(Distribution):

#     """ Gaussian distribution class for calculating and 
#     visualizing a Gaussian distribution.

#     Attributes:
#         mean (float) representing the mean value of the distribution
#         stdev (float) representing the standard deviation of the distribution
#         data_list (list of floats) a list of floats extracted from the data file

#     """

#     def __init__(self, mu=0, sigma=1): 
#         Distribution.__init__(self, mu, sigma) 

#     def calculate_mean(self):    
#         """Function to calculate the mean of the data set. 
#         Args: 
#             None
#         Returns: 
#             float: mean of the data set
#         """

#         avg = 1.0 * sum(self.data) / len(self.data)
#         self.mean = avg        
#         return self.mean

#     def calculate_stdev(self, sample=True):
#         """Function to calculate the standard deviation of the data set.
#         Args: 
#             sample (bool): whether the data represents a sample or population
#         Returns: 
#             float: standard deviation of the data set
#         """

#         if sample:
#             n = len(self.data) - 1
#         else:
#             n = len(self.data)

#         mean = self.calculate_mean()   
#         sigma = 0

#         for d in self.data:
#             sigma += (d - mean) ** 2        

#         sigma = math.sqrt(sigma / n) 
#         self.stdev = sigma

#         return self.stdev  

#     def plot_histogram(self):
#         """Function to output a histogram of the instance variable data using 
#         matplotlib pyplot library.
#         Args:
#             None
#         Returns:
#             None
#         """

#         plt.hist(self.data)
#         plt.title('Histogram of Data')
#         plt.xlabel('data')
#         plt.ylabel('count')     

#     def pdf(self, x):
#         """Probability density function calculator for the gaussian distribution.        
#         Args:
#             x (float): point for calculating the probability density function           
#         Returns:
#             float: probability density function output
#         """        

#         return (1.0 / (self.stdev  *math.sqrt(2*math.pi)))  *math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)        


#     def plot_histogram_pdf(self, n_spaces = 50):
#         """Function to plot the normalized histogram of the data and a plot of the probability density function along the same range        

#         Args:
#             n_spaces (int): number of data points
#         Returns:
#             list: x values for the pdf plot
#             list: y values for the pdf plot
#         """

#         mu = self.mean
#         sigma = self.stdev
#         min_range = min(self.data)
#         max_range = max(self.data)

#          # calculates the interval between x values

#         interval = 1.0 * (max_range - min_range) / n_spaces

#         x = []
#         y = []

#         # calculate the x values to visualize

#         for i in range(n_spaces):
#             tmp = min_range + interval*i
#             x.append(tmp)
#             y.append(self.pdf(tmp))

#         # make the plots
#         fig, axes = plt.subplots(2,sharex=True)
#         fig.subplots_adjust(hspace=.5)
#         axes[0].hist(self.data, density=True)
#         axes[0].set_title('Normed Histogram of Data')
#         axes[0].set_ylabel('Density')

#         axes[1].plot(x, y)
#         axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')

#         axes[0].set_ylabel('Density')
#         plt.show()

#         return x, y

#     def __add__(self, other):    
#         """Function to add together two Gaussian distributions
#         Args:
#             other (Gaussian): Gaussian instance
#         Returns:
#             Gaussian: Gaussian distribution
#             """

#         result = Gaussian()
#         result.mean = self.mean + other.mean
#         result.stdev = math.sqrt(self.stdev  **2 + other.stdev**  2)

#         return result

#     def __repr__(self):
#             """Function to output the characteristics of the Gaussian instance
#        Args:
#             None
#        Returns:
#                 string: characteristics of the Gaussian
#         """
#         return "mean {}, standard deviation {}".format(self.mean, self.stdev)

#  def read_data_file(self, file_name, sample=True):
#         """Function to read in data from a txt file. The txt file should have one number (float) per line. The numbers are stored in the data attribute. After reading the file, the mean and standard deviation are calculated
#         Args:
#             file_name (string): name of a file to read from
#         Returns:
#             None
#         """
#     with open(file_name) as file:
#       data_list = []
#       line = file.readline()
#       while line:
#         data_list.append(int(line))
#         line = file.readline()
#       file.close()

#       self.data = data_list
#       self.mean = self.calculate_mean();
#       self.stdev = self.calculate_stddev(sample)

# ```


# Inheritance with the Gaussian Class
# To give another example of inheritance, take a look at the code in this Jupyter notebook. The Gaussian distribution code is refactored into a generic Distribution class and a Gaussian distribution class. Read through the code in this Jupyter notebook to see how the code works.

# The Distribution class takes care of the initialization and the read_data_file method. Then the rest of the Gaussian code is in the Gaussian class. You'll later use this Distribution class in an exercise at the end of the lesson.

# Run the code in each cell of this Jupyter notebook. This is a code demonstration, so you do not need to write any code.

class Distribution:
    
    def __init__(self, mu=0, sigma=1):
    
        """ Generic distribution class for calculating and 
        visualizing a probability distribution.
    
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
            """
        
        self.mean = mu
        self.stdev = sigma
        self.data = []


    def read_data_file(self, file_name):
    
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
                
        Args:
            file_name (string): name of a file to read from
        
        Returns:
            None
        
        """
            
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        self.data = data_list


        import math
import matplotlib.pyplot as plt

class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """
    def __init__(self, mu=0, sigma=1):
        
        Distribution.__init__(self, mu, sigma)
    
        
    
    def calculate_mean(self):
    
        """Function to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
                    
        avg = 1.0 * sum(self.data) / len(self.data)
        
        self.mean = avg
        
        return self.mean



    def calculate_stdev(self, sample=True):

        """Function to calculate the standard deviation of the data set.
        
        Args: 
            sample (bool): whether the data represents a sample or population
        
        Returns: 
            float: standard deviation of the data set
    
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
    
        mean = self.calculate_mean()
    
        sigma = 0
    
        for d in self.data:
            sigma += (d - mean) ** 2
        
        sigma = math.sqrt(sigma / n)
    
        self.stdev = sigma
        
        return self.stdev
        
        
        
    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')
        
        
        
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
        

    def plot_histogram_pdf(self, n_spaces = 50):

        """Function to plot the normalized histogram of the data and a plot of the 
        probability density function along the same range
        
        Args:
            n_spaces (int): number of data points 
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        mu = self.mean
        sigma = self.stdev

        min_range = min(self.data)
        max_range = max(self.data)
        
         # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(n_spaces):
            tmp = min_range + interval*i
            x.append(tmp)
            y.append(self.pdf(tmp))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return x, y
        
    def __add__(self, other):
        
        """Function to add together two Gaussian distributions
        
        Args:
            other (Gaussian): Gaussian instance
            
        Returns:
            Gaussian: Gaussian distribution
            
        """
        
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)
        
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Gaussian instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """
        
        return "mean {}, standard deviation {}".format(self.mean, self.stdev)

#         Summary of the Terminal Commands Used in the Video
# cd binomial_package_files
# python setup.py sdist
# pip install twine

# # commands to upload to the pypi test repository
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# pip install --index-url https://test.pypi.org/simple/ dsnd-probability

# # command to upload to the pypi repository
# twine upload dist/*
# pip install dsnd-probability


# Write a Python program to check whether a given key already exists in a dictionary.

# dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 

# Given dictionary
my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Function to check if a key exists in the dictionary
def check_key_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

# Key to check
key_to_check = 3

# Checking if the key exists in the dictionary
if check_key_exists(my_dict, key_to_check):
    print(f"The key {key_to_check} exists in the dictionary.")
else:
    print(f"The key {key_to_check} does not exist in the dictionary.")



# Write a Python program to get sum of elements in tuple.
# Note: (without built-in functions or control flow statements)

# tuplex = (4, 8, 3)

tuplex = (4, 8, 3)

# Using the sum without control flow statements or built-in functions
sum_tuple = (tuplex[0] + tuplex[1] + tuplex[2])

print("Sum of elements in the tuple:", sum_tuple)

# What is the output of the following program?

# language = ['P', 'y', 't', 'h', 'o', 'n']

# print(language[:-4])

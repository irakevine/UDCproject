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

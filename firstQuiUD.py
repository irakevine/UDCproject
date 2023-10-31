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
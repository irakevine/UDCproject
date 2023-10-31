# Write a script of your own
# Open up a brand new empty file in your text editor, name it and save it in the place where you're keeping the files for your Python learning. Put the following code into it.:"how_many_snakes = 1
how_many_snakes = 3  # Change the number to the desired count of snakes

snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""

print(snake_string * how_many_snakes)  # Use the variable directly, not as a string 'how_many_snakes'


num=int(float(input('Enter a number :')) )

print('hello'*num)

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))


#     While True:
# Try:    
# x= int(input('Enter a number:'))
#     break 
# except:
# print('That\'s not a valid number!)
# print('\nAttempted Input\n')
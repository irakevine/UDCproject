import thirdOuiUD  as tq
print(2+5)
print(tq.num)



scores = [88, 92, 79, 93, 85]

mean = tq.mean(scores)
curved = tq.add_five(scores)

mean_c = tq.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)
print(tq.__name__)

# It's your turn to import and use the math module. Use the math module to calculate e to the power of 3. And assign the answer to result.

# Refer to the math module's documentation to find the function you need!


import math

# calculate e to the power of 3 using the math module
result = math.exp(3)

print(result)  # This will display the result of e raised to the power of 3


from datetime import datetime 
import pytz 
utc = pytz.utc
ist=pytz.timezone('Asia/Kolkata')

now = datetime.now(tz=utc)
ist_now= now.astimezone(list)

print(now)
print(ist_now)

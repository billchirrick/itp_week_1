# This is a number magic trick
# Pick a number from 1 - 9
# Multiple by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number
# Final number is 5

# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!


a = input("Pick a number from 1 - 9 ") 
a=int(a)
b = a
a *= 2
a += 10
a /= 2
a = a - b
if a==5:
    print("final is always 5!")
elif a!=5:
    print("final is NOT always 5!")

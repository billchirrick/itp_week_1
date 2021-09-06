# ITP Week 1 Day 3 Exercise

# EASY

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. loop through the lowercase and print each element
for x in lowercase:
    print(x)
# 2. loop through the lowercase and print the capitalization of each element
for x in lowercase:
    print(x.upper())      

# MEDIUM

# 1. create a new variable called uppercase with an empty list
uppercase = []

# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list
for x in lowercase:
    uppercase.append(x.upper())
print(uppercase)

# for y in uppercase:
#     print(y)


# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.

# password = "MySuperSafePassword!@34"
# password = "MySuperSafePassword34"
password = input("Pick a secure password ") 

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# 1. create the following variables and assign them Booleans as False
    # has_uppercase
    # has_lowercase
    # has_number
    # has_special_char

has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False

# 2. loop through the string password (same as a list)
# OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
# password_list = list(password) prior to looping.

number = ['1','2','3','4','5','6','7','8','9','0']

password_list = list(password)
i = len(password) - 1
print(i)
while i >= 0:
    if password_list[i] in lowercase:
        has_lowercase = True
    if password_list[i] in uppercase:
        has_uppercase = True
    if password_list[i] in special_char:
        has_special_char = True
    if password_list[i] in number:
        has_number = True
    i -= 1
print("has_lowercase: ") 
print(has_lowercase)
print("has_uppercase: ") 
print(has_uppercase)
print("has_special_char: ") 
print(has_special_char)
print("has_number: ") 
print(has_number)


# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.

# NOTE: to see if it has a number, use range from 0 - 10!

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True
if final_result == True:
    print("SAFE STRONG PASSWORD")
else:
    print("Update password: too weak")
# NOTE: we can shorthand this by just checking if the variable exists (returns True)
# final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
    

# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop

# BONUS: update the password variable to take in an user input!

# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!

if has_lowercase == False:
    print("Add a lowercase character")
if has_uppercase == False:
    print("Add a uppercase character")
if has_special_char == False:
    print("Add a special character")
if has_number == False:
    print("Add a number character")


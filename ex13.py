from sys import argv
# read the WYSS section for how to run this
script, first, second, third, = argv


print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)



# python ex13.py first 2nd 3rd
# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd

#  python ex13.py stuff thongs that
# The script is called: ex13.py
# Your first variable is: stuff
# Your second variable is: thongs
# Your third variable is: that

#  python ex13.py apple orange grapefruit
# The script is called: ex13.py
# Your first variable is: apple
# Your second variable is: orange
# Your third variable is: grapefruit

#  python ex13.py
# Traceback (most recent call last):
# File "ex13.py", line 3, in <module>
# script, first, second, third = argv
# ValueError: not enough values to unpack (expected 4, got 1)
# This happens whenyou do not put enough arguments on the commend when you run it.
# (in this case just first 2nd)

# Study Drills
# 1 Try giving fewer than three arguments to your script. See that error you get? See if you can
# explain it.
# 2 Write a script that has fewer arguments and one that has more. Make sure you give the unpacked
# variables good names.
# 3 Combine input with argv to make a script that gets more input from a user. Don’t overthink it.
# Just use argv to get something, and input to get something else from the user.
# 4 Remember that modules give you features. Modules. Modules. Remember this because we’ll
# need it later.

# The difference has to do with where the user is required to give input. 
# If they give your script inputs on the command line, then you use argv. 
# If you want them to input using the keyboard while the script is running, then use input().

# When deleting the third argument from the script:
# python ex13.py apple orange banana
# Traceback (most recent call last):
# File "ex13.py", line 3, in <module>
# script, first, second = argv
# ValueError: too many values to unpack (expected 3)

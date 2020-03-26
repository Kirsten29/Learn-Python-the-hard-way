from sys import argv

script, filename = argv

txt = open(filename) 


print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)


print(txt_again.read())

#SD1 write it out
#SD4 get rid of lines 10-15 where you use input and run the script again.
#SD5 use only input and try the script that way. why is one way of getting the filename better
#than another?
#SD6 python ex15.py ex15.py
#SD7 #6 txt.close() #15 txt_again.close()
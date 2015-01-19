# imports the argv module
from sys import argv
# sets the script and filename variables to user input
script, filename = argv
# opens the file given by the user and sets it to the txt variable
txt = open(filename)
# outputs the file to the screen
print "Here's your file %r: " % filename
print txt.read()
# 
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
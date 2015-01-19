# Assigns a string value to the variable x
x = "There are %d types of people." % 10
# Same as above, except the variable is binary
binary = "binary"
# Do I really need to explain this?
do_not = "don't"
# Using string formatters to insert the values of binary and do_not into the variable y
y = "Those who know %s and those who %s." % (binary, do_not)
#Printing the vairables
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
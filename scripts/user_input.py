from getpass import getpass

print "What is your name?"
name = raw_input()

color = getpass('What is your favorite color? ')

print "Hi", name 
print "Your favorite color is: ", color

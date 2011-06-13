name = raw_input("What is your name? ")
age = raw_input("How old are you? ")
weight = raw_input("How much do you weigh? ")
height = raw_input("How tall are you? ")

from sys import argv

script, first, second, third, fourth = argv

print "This is your name:", name
print "This is you age:", age
print "This is your weight:", weight
print "This is your height:", height
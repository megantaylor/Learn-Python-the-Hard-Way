my_name = 'Megan M. Taylor'
my_age = 24 # not a lie
my_height = 74 # inches
my_weight = 151 #lbs
my_eyes = 'Green'
my_teeth = 'White'
my_hair = 'Brown'
convert_centimeters = 2.54
convert_kilos = 0.45359237


print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She weighs %d pounds." % my_weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print my_height * convert_centimeters
print my_weight * convert_kilos
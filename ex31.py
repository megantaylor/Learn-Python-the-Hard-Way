print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Ask the bear for some cake."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. You die."
	elif bear == "2":
		print "The bear eats your legs off. You die."
	elif bear == "3":
		print "Bear gives you some cake."
	else:
		print "Bear runs away."
		
elif door == "2":
	print "You stare into the endless abyss at Cthuhlu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. You are now blind."
		
else:
	print "You stumble around and fall through a trapdoor into a pit full of spikes. You die."
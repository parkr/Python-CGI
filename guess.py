#! usr/bin.python

a = 0
target = 4
counter = 0
print """
Guess a number between 1 and 10...
"""

while a != target:
	a = int(raw_input("Guess: "))
	counter+=1
	if a == target:
		break
	elif a < target:
		print "bigger..."
	else:
		print "smaller..."
else:
	print "Ack, try again"

print "\nYou got it! The number was", target, "and you tried", counter, "times."

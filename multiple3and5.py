# Multiple3and5.py

# Project 1 from ProjectEuler.net
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Request number to find all multiples of 3 and 5 below that number. 
# Also converts it to an integer.
number = int(input('Find the sum of all multiples of 3 or 5 below the following number:'))

# Define the starting values to create multiples of 3 and 5.
threes = 1
fives = 1
fifteens = 1

# Defines the variable that keeps track of the sum of all of the multiples.
answer = 0

# Sum up all the multiples of 3 and 5 below 'number'.
while threes * 3 < number or fives * 5 < number or fifteens * 15 < number:
	if threes * 3 < number:
		answer += threes * 3
		threes += 1

	if fives * 5 < number:
		answer += fives * 5
		fives += 1

	# Don't forget to subtract the multiples that are counted for twice 
	# since they are multiple of both 3 and 5 (multiples of 15).
	if fifteens * 15 < number:
		answer -= fifteens * 15
		fifteens += 1

print(answer)
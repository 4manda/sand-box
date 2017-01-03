# largestPrimeFactor.py

# Problem 3 of ProjectEuler.net
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Input number to find largest prime factor.
number = int(input('Enter number to find the largest prime factor:'))

# Very inefficient method since it goes down from half the number.
# For faster method, go to line 43
def findFactors(n):
	# Define array with primes up to 57.
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47, 51, 57]

	# Define variable to test factorization with n.
	testFactor = n

	# Checks if any of the primes in prime[] divide evenly into n.
	for a in primes:
		if n % a == 0:
			testFactor = n / a
			break
		else:
			testFactor = round(n / a)

	#Defines a variable to track the largest factor of n
	largestFactor = 1

	# Recursive loop starting with half of n and decrementing to find factors
	while testFactor >= 2:
		if n % testFactor == 0:
			largestFactor = findFactors(testFactor)
			break
		else:
			testFactor -= 1

	# Returns either the number itself if it is prime or its largest prime factor.
	if largestFactor > 1:
		return largestFactor
	else:
		return n

print(int(findFactors(number)))

# More efficient code, starting with 2 and incrementing up until factors are found.
divider = 2
while divider * divider < number:
	if number % divider == 0:
		if number == divider:
			largest = divider
			break
		number /= divider
		divider = 2
	else:
		divider += 1

print(largest)

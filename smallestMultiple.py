#Smallest Mutliple
#Project Euler problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

minrange = 1
maxrange = 20

def smallestMultiple(minrange, maxrange):
    numbers = []
    a = minrange
    upperlimit = 1
    while a <= maxrange:
        numbers.append(a)
        upperlimit = upperlimit * numbers[a-1]
        a += 1
#Multiply all primes together below 20
    b = 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2 * 2 * 3 * 2 * 2
    length = len(numbers)
    i = 0
    print(length, b, numbers, upperlimit)
    while b < upperlimit:
        while i <= length-1:
            print(b % numbers[i])
            if b % numbers[i] == 0 and i == length - 1:
                print('found something')
                return b
            elif b % numbers[i] == 0:
                print(b, i)
                i += 1
            else:
                b += 1
                i = 0
                break
    return upperlimit

print(smallestMultiple(minrange, maxrange))

# this only finds the smallest multiple between 1-20. Line 18 is the key to finding a more efficient algorithm for any set of numbers. I need to figure out how to find all the factors of each number and eliminate multiples between numbers, but not within... for example 8 and 2.. Factors of 8 are 2,2,2 and factors of 2 is 2. I don't need 4 2's, only 3 to make sure a number is a multiple of 8 and 2.

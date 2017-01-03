# Largest Palindrome Product
# ProjectEuler.net
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Function to check if a number is a palindrome


def isPalindrom(number):
    length = len(number)
    a = 0
    while a <= round(length / 2):
        if number[a] == number[length - 1 - a]:
            a += 1
        else:
            return False
    return True

# Code to help me debug if isPalindrom was working
#number = str(input("Enter number to check palindrome:"))
#if isPalindrom(number) == True:
#    print("It is a palindrome")
#else:
#    print("Not a palindrome")

# Sets a lower limit to check if factors multiply to palindrom - goes down from 999... * 999....
def palindromProd(digits):
    factor1 = int("9" * digits)
    factor2 = int("9" * digits)
    limit = int("8" + "0" * (digits - 1))
    largest = 0
    while factor1 > limit:
        while factor2 > limit:
            if isPalindrom(str(factor1 * factor2)):
                if factor1 * factor2 > largest:
                    largest = factor1 * factor2
                    print(factor1, factor2)
                    factor2 -= 1
                else:
                    factor2 -= 1
            else:
                factor2 -= 1
        factor1 -= 1
        factor2 = factor1
    print(largest)
    print("hopefully something was found")

digits = int(input("Provide the number of digits in each factor to determine which produce the largest palindrome:"))
palindromProd(digits)

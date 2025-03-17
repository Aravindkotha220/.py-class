
# 1. Find the sum of odd digits in a given number

def sum_of_odd_digits(number):
    total = 0
    for digit in str(number): 
        if int(digit) % 2 != 0: 
            total += int(digit)
    return total

num = int(input("Enter a number: "))
print("Sum of odd digits:", sum_of_odd_digits(num))


# 2. Print all the Armstrong numbers in given range





# 3. Find the smallest prime digit in a given number

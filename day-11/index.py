
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

def armstrong(num):
    num_str = str(num) 
    power = len(num_str)  
    sum_of_digits = sum(int(digit) ** power for digit in num_str) 
    return sum_of_digits == num 
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"\nArmstrong numbers between {start} and {end}:")
for num in range(start, end + 1):
    if armstrong(num):
        print(num, end=" ") 



# 3. Find the smallest prime digit in a given number

def smallest_prime_digit(num):
    prime_digits = {'2', '3', '5', '7'} 
    digits = list(str(num))  
    prime_found = [int(d) for d in digits if d in prime_digits]  
    return min(prime_found) if prime_found else None
    
num = int(input("Enter a number: "))
result = smallest_prime_digit(num)
if result is not None:
    print(f"The smallest prime digit in {num} is {result}")
else:
    print(f"No prime digits found in {num}")
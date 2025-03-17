
# Write a program to display the multiplication table of a given number. First 20

num = int(input("Enter a number:"))

print(f"\nMultiplication Table of {num} (First 20 Multiples):\n")
for i in range(1, 21):
    print(f"{num} × {i} = {num * i}")
    
# Write a program to calculate the factorial of a number using a while loop. 
    
    num = int(input("Enter a number: "))

factorial = 1
i = num
while i > 1:
    factorial *= i
    i -= 1 
print(f"\nFactorial of {num} is {factorial}")

# Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.

print("Numbers divisible by both 3 and 5 (1 to 100):")

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0: 
        print(num, end=" ")  
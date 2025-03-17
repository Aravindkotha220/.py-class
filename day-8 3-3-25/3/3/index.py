

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(min_num, max_num):
    print(f"Prime numbers between {min_num} and {max_num}:")
    for num in range(min_num, max_num + 1):
        if is_prime(num):
            print(num, end=" ")

min_num = int(input("Enter the minimum number: "))
max_num = int(input("Enter the maximum number: "))

print_primes(min_num, max_num)



# code of pin validation

# Define the correct PIN
correct_pin = "1234"
attempts = 3  

while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print(" Access Granted!")
        break 
    else:
        attempts -= 1
        if attempts > 0:
            print(f" Incorrect PIN. You have {attempts} attempts left.")
        else:
            print(" Account Blocked! Too many failed attempts.")

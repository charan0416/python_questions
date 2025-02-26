# Function to check if a number is an Armstrong number
def is_armstrong(num):
    order = len(str(num))  # Find the number of digits in the number
    temp_num = num
    sum_of_digits = 0
    while temp_num > 0:
        digit = temp_num % 10  # Get the last digit
        sum_of_digits += digit ** order  # Raise the digit to the power of 'order' and add it to sum
        temp_num //= 10  # Remove the last digit
    return num == sum_of_digits  # If the sum is equal to the number, it's an Armstrong number

# Input the interval from the user
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))

# Iterate through the numbers in the given interval
print(f"Armstrong numbers between {lower} and {upper} are:")
for num in range(lower, upper + 1):
    if is_armstrong(num):  # Check if the number is an Armstrong number
        print(num)






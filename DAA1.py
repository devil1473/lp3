#DAA1. Write a program to calculate Fibonacci numbers and find its step count.

def fibonacci(n):
    if n <= 0:
        return 0, 1  # Step count is 1 for invalid cases
    elif n == 1:
        return 1, 1  # Step count is 1 for n == 1 case

    # Initialize the first two Fibonacci numbers and step count
    a, b = 0, 1
    steps = 2  # Initializing counts as setting a and b are first steps

    for i in range(2, n + 1):
        a, b = b, a + b
        steps += 1  # Increment step count for each addition

    return b, steps

# Get input from the user
n = int(input("Enter the position of the Fibonacci number: "))
fibonacci_num, step_count = fibonacci(n)

print(f"The {n}-th Fibonacci number is: {fibonacci_num}")
print(f"Steps taken to compute: {step_count}")
#output-Enter the position of the Fibonacci number: 6
#The 6-th Fibonacci number is: 8
#Steps taken to compute: 7

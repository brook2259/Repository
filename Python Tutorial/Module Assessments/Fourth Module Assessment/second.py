def fib_seq(n):
    # Base cases: return n for 0 and 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two previous Fibonacci numbers
        return fib_seq(n-1) + fib_seq(n-2)
             
    
        
# Function to print the Fibonacci sequence up to a given limit
def print_fib_sequence(limit):
    for i in range(limit):
        print(fib_seq(i), end=" ")

# Example usage: Print the first 10 Fibonacci numbers
print_fib_sequence(10)
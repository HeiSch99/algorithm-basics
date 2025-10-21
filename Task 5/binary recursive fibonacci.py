# Binary recirsive algorithm for calculating positive Fibonacci numbers
def fib(n):
    if n < 0:
        # Error statement for negarive n, since we only consider positive values
        return f"[WARN]: F({n}) is out of range."
    if n == 0:
        # First base case
        return 0
    elif n == 1:
        # Second base case
        return 1
    else:
        # Binary recursion applies for any n >= 2
        return (fib(n - 1) + fib(n - 2))

# This calls the algorithm to calculate the sequence of Fibonacci numbers from n = 0 to n = 6
for i in range(7):
    print(f"F({i}) = {fib(i)}")


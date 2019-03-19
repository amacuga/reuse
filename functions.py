def fib(n=2000, m=30):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print('m was' , m)

# Now call the function we just defined:
fib(m=20)
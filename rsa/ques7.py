from sympy import isprime

N = 510143758735509025530880200653196460532653147

# Start checking from small primes
for i in range(2, int(N**0.5) + 1):
    if N % i == 0 and isprime(i):  # Check if i is a factor and a prime
        print("Smaller prime:", i)
        break

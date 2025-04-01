def find_prime_and_base():
    numbers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
    
    # Try all 3-digit primes
    for p in range(100, 1000):
        if not is_prime(p):
            continue
        
        # Try to find a base x
        for x in range(2, 100):
            # Check if x^k mod p generates the sequence
            sequence = [pow(x, k, p) for k in range(len(numbers))]
            if sequence == numbers:
                return p, x
    
    return None, None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

p, x = find_prime_and_base()
print(f"p = {p}, x = {x}")
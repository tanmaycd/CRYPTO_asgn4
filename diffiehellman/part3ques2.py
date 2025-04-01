def is_primitive_element(g, p):
    factors = prime_factorization(p - 1)
    
    for factor in factors:
        power = (p - 1) // factor
        if pow(g, power, p) == 1:
            return False
    
    return True

def prime_factorization(n):
    factors = set()
    
    if n % 2 == 0:
        factors.add(2)
        while n % 2 == 0:
            n //= 2
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
        i += 2
    
    if n > 2:
        factors.add(n)
        
    return factors

def find_smallest_primitive_element(p):
    for g in range(2, p):
        if is_primitive_element(g, p):
            return g
    return None

p = 28151
result = find_smallest_primitive_element(p)
print(f"The smallest primitive element of F_{p} is: {result}")

def optimized_solution():
    p = 28151
    p_minus_1 = p - 1
    
    critical_exponents = [
        p_minus_1 // 2,
        p_minus_1 // 5,
        p_minus_1 // 563,
    ]
    
    for g in range(2, p):
        is_primitive = True
        for exp in critical_exponents:
            if pow(g, exp, p) == 1:
                is_primitive = False
                break
        
        if is_primitive:
            return g
    
    return None

result_optimized = optimized_solution()
print(f"Using the optimized solution, the smallest primitive element of F_{p} is: {result_optimized}")
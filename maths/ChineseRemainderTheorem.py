def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def chinese_remainder_theorem(a, m):
    total_mod = 1 
    for modulus in m:
        total_mod *= modulus
    
    result = 0 
    
    for remainder, modulus in zip(a, m):
        partial_mod = total_mod // modulus  
        inverse = mod_inverse(partial_mod, modulus)  
        result += remainder * partial_mod * inverse
    
    return result % total_mod 


remainders = [2, 3, 5]  
moduli = [5, 11, 17]  


final_result = chinese_remainder_theorem(remainders, moduli)
print(final_result)
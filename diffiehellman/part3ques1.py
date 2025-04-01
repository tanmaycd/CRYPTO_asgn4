# Method 1: Using Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse_euclidean(g, p):
    gcd, x, y = extended_gcd(g, p)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % p

# Method 2: Using Fermat's Little Theorem
def mod_inverse_fermat(g, p):
    # In a prime field, g^(p-2) ≡ g^(-1) mod p
    return pow(g, p - 2, p)

# Given values
p = 991  # prime modulus
g = 209  # element to find inverse for

# Calculate inverse using both methods
inverse_euclidean = mod_inverse_euclidean(g, p)
inverse_fermat = mod_inverse_fermat(g, p)

print("Inverse using Extended Euclidean Algorithm:", inverse_euclidean)
print("Inverse using Fermat's Little Theorem:", inverse_fermat)

# Verification
verification = (g * inverse_euclidean) % p
print("Verification (should be 1):", verification)
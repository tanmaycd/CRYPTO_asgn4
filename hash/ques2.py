import math

def collision_probability(n, H=2048):
    return 1 - (math.factorial(H) / (math.factorial(H - n) * (H ** n)))

H = 2 ** 11  
n = 1  

while collision_probability(n, H) < 0.75:
    n += 1

print(f"Number of unique secrets needed for 75% chance of collision: {n}")
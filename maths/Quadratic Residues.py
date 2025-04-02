prime = 29
target_vals = {14, 6, 11} 

quadratic_roots = [num for num in range(1, prime) if pow(num, 2, prime) in target_vals]

print(f"Matching quadratic residues: {[pow(x, 2, prime) for x in quadratic_roots]}")
print(f"flag {min(quadratic_roots)}")

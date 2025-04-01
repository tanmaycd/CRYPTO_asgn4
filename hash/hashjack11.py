import math
N = 2**11  
k = math.log(0.5) / math.log(1 - 1/N)
print(f"Number of unique values needed for 50% chance of collision: {math.ceil(k)}")
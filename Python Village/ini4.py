# INI4 Conditions and Loops
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Read and save input.
a, b = map(int, input().split())
odd_sum = 0

# Loop through range. 
for i in range(a, b+1):
    if i % 2 != 0: # Check if odd.
        odd_sum += i

# Print final result. 
print(odd_sum)
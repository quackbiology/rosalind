# DNA Counting DNA Nucleotides
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# Read the single strand DNA string from the file. All are in uppercase already. Convert object into string and assign to 'ss_dna'.
ss_dna = open('rosalind_dna.txt', 'r').read().strip()

# Create a dictionary to hold the counts of each base.
base_count = {}

# Separate each base with a space. Loop through each and count occurences. Store counts in base_count. 
for base in ss_dna:
    if base in base_count:
        base_count[base] += 1
    else: 
        base_count[base] = 1

# Return the counts of A, T, C, G in this order occuring in ss_dna as integers.  
print(
    base_count['A']
    , base_count['C']
    , base_count['G']
    , base_count['T']
)

# Claude says I don't need to do this. 
# ss_dna.close()
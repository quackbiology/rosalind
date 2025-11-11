# REVC Complementing a Strand of DNA
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

# Read single strand DNA sequence from file. Convert object into string, strip whitespace, and assign to 'ss_dna'. 
ss_dna = open('rosalind_revc.txt', 'r').read().strip()

# Create the complement dictionary. 
base_pairs = str.maketrans("ATGC", "TACG")

# Complement each base then reverse the string. Assign to 'ss_dna_revc'
ss_dna_revc = ss_dna.translate(base_pairs)[::-1]

# Print the reverse complement string.
print(ss_dna_revc)

# Maybe output the string into a file next time? What are the pros and cons of using infile and outfile?

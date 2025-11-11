# RNA Transcribing DNA into RNA
# Given: Given: A DNA string t having length at most 1000 nt.
# Return:  The transcribed RNA string of t.

# Read the single strand DNA sequence from the file. All are in uppercase already. Convert object into string and assign to 'ss_dna'.
ss_dna = open('rosalind_rna.txt', 'r').read().strip()

# Transcribe DNA into RNA by replacing all occurences of 'T' with 'U'. Assign to 'rna'. 

for t in ss_dna:
    rna = ss_dna.replace('T', 'U')

print(rna)

# Maybe make an output file instead of just printing to console in the next ones?
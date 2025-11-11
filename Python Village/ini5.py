# INI5 Working with Files
# Given: A file containing at most 1000 lines.
# A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# Open the sample file and assign to object 'sample'. Open an output file to write result.
sample = open('rosalind_ini5.txt', 'r')
output = open('ini5_output.txt', 'w')

# Get indices and items from sample using enumerate. 
for index, line in enumerate(sample, start = 1): #1-based indexing.
    if index % 2 == 0: # Check if even-numbered line.
        output.write(line)

sample.close()
output.close()
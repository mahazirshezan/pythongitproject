def DNA_strand(dna):
    # Create a dictionary to map each nucleotide to its complement
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Use a list comprehension to create the complementary strand
    complementary_strand = [complement[nucleotide] for nucleotide in dna]
    
    # Join the list into a string and return it
    return ''.join(complementary_strand)

# Example usage
dna_strand = "ATCG"
complementary_strand = DNA_strand(dna_strand)
print(f"The complementary strand of {dna_strand} is {complementary_strand}")
from Bio.Seq import Seq 

n = int(input("Enter the number of sequence you want to input: "))

for i in range(1, n + 1):

    seq = Seq(input(f"Enter sequence {i}: ").upper())
    
    
    # Print the length 

    print(f"Length of Sequence {i}: {len(seq)}")

    # Print all nucleotide counts
    # nt = nucleotide, variable

    counts = ", ".join(f"{nt}: {seq.count(nt)}" for nt in "ATGC")
    
    print(f"Counts: {counts}\n")
    

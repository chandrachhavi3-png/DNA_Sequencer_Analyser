from dna_function import read_fasta , GC_content , count_nucleotide , transcribe , reverse_complement

TP53 = read_fasta("TP53 sequence.fasta")
print(TP53)
print("sequence length :", len(TP53))
print("count_nucleotide :", count_nucleotide(TP53))
print("GC_content :", GC_content(TP53))
print("RNA :", transcribe(TP53))
print("Reverse Complement :", reverse_complement(TP53))
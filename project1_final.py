# importing the required libraries for reading fasta files, calculating gc content and plotting
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import matplotlib.pyplot as plt

# importing the functions i built from scratch in dna_function.py
from dna_function import count_nucleotide, GC_content, reverse_complement, transcribe, read_fasta

# reading the full TP53 mRNA sequence from NCBI (accession NM_000546.6) using Biopython
tp53 = SeqIO.read("TP53_full.fasta","fasta")

# converting the Biopython Seq object to a plain string so my own functions can work on it
tp53_str = str(tp53.seq)

print("DNA SEQUENCE ANALYSIS - TP53, TUMOR SUPRESSOR GENE")
print("--------------------------------------------------")

print("   ")

# printing basic information about the sequence - id, full description and length
print("TP53 id : ",tp53.id)
print("TP53 description : ",tp53.description)
print("TP53 seq length : ",len(tp53.seq))

print("   ")

# running my own functions that i built from scratch on the TP53 sequence
print("Output got from tools in DNA SEQUENCE ANALYSER")
print("   ")
print("Nucleotide count : ",count_nucleotide(tp53_str))
print("GC_content : ",GC_content(tp53_str))
print("reverse complement : ",reverse_complement(tp53_str[:60]))
print("transcribe : ",transcribe(tp53_str[:60]))

print("   ")

# running the same analysis using biopython's built-in methods to cross validate my results
print("Output got from Biopython's in-bulit functions")
print("  ")
print("GC_content : ",gc_fraction(tp53.seq)*100)
print("reverse complement : ",tp53.seq[:60].reverse_complement())
print("transcribe : ",tp53.seq[:60].transcribe())

print("  ")

# validating that my GC_content function gives the exact same result as Biopython
print("Biopython Validation")
print("  ")
a = gc_fraction(tp53.seq)*100
b = GC_content(tp53_str)
if a == b:
    print("TRUE. Biopython GC% matches own function")
else:
    print("NOT TRUE. Biopython GC% doesn't match own function")


# plotting nucleotide composition of TP53 as a bar chart and saving it as a png
TP53 = {'A': 532, 'G': 621, 'T': 639, 'C': 720}
nucleotide = dict.keys(TP53)
composition = dict.values(TP53)
plt.bar(nucleotide,composition)
plt.xlabel("Nucleotide")
plt.ylabel("Composition")
plt.title("Nucleotide Composition of TP53")
plt.tight_layout()
plt.savefig("Nucleotide Composition of TP53.png")
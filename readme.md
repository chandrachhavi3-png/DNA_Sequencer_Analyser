# DNA Sequence Analyser
This project is based on python DNA analyser which consists of tools that are required in analysis any fasta sequence to extract essential information such as its GC content, number of each nucleotide, reverse complements etc.
It consists of functions that help extract the fasta sequence from the downloaded file.
Below are the function along with their purpose and how to run them:

1. count_nucleotide()
It returns the count of each nucleotide in dictionary {}
count_nucleotide(sequence)

2. transcribe()
It returns the RNA of the given sequence by replacing T with U.
transcribe(sequence)

3. GC_content()
It returns the GC content percentage of a given sequence by counting the total sum of GC divided by the total length of that sequence, multiplied with 100.
GC_content(sequence)

4. reverse_complement()
It returns the reverse complement of a given sequence while using a complement map.
reverse_complement(sequnece)

5. read_fasta()
It returns the fasta sequence of any file while removing any space or headers present in the file.
read_fasta(filename)

## Validated With
Tested on a real TP53 gene sequence (exon 5, partial CDS) from NCBI, accession MH011443.1.
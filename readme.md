# DNA Sequence Analyser

**Live App:** [Try the DNA Sequence Analyser here](paste_your_streamlit_url_here)

---

## About

I am a second year B.Sc. Biochemistry Honours student at Adamas University, Kolkata. During my one month cancer biology internship at University of Calcutta, I got hands-on exposure to TNBC research and wet lab techniques. That experience made me curious on what do the genes involved in cancer actually look like at the sequence level? That question led me to start learning computational biology independently, and this is my first project.

---

## What is this project

This is a DNA sequence analysis tool built entirely in Python from scratch. I wrote every function myself first without using any library, to understand what was actually happening at each step. I then validated my results against Biopython, a professional bioinformatics library, to confirm my functions were correct.

The tool takes any DNA sequence from a FASTA file and gives you:
- Count of each nucleotide (A, T, G, C)
- GC content percentage
- RNA transcript
- Reverse complement

I also built a web app using Streamlit so anyone can upload their own FASTA file and analyse it instantly without writing any code.

---

## How I applied it

I applied this tool to the complete human TP53 mRNA sequence downloaded from NCBI (accession NM_000546.6). TP53 encodes the p53 protein, known as the guardian of the genome, and is one of the most studied genes in cancer biology. I chose it because of my internship exposure to cancer research and because it is a well-documented gene to validate computational results against.

---

## What the results show

The full TP53 sequence is 2512 bases long and has a GC content of 53.38%, meaning more than half the sequence is made up of G and C nucleotides.

Breaking it down - out of 2512 bases, C appears 720 times, T appears 639 times, G appears 621 times, and A appears 532 times. C is the most frequent nucleotide.

Why does this matter? 
Regions of DNA that are high in G and C tend to have special regulatory regions near them called CpG islands. These act like switches that control whether a gene gets turned on or off. TP53 is a gene that needs very tight control in the body because it plays a key role in preventing cancer. Its high GC content is consistent with this, genes that need careful regulation tend to be GC-rich.

This is an early observation from the sequence data. A full interpretation would need comparison with other cancer-related genes and methylation data, which is exactly what the next project will explore.

![Nucleotide Composition](Nucleotide%20Composition%20of%20TP53.png)

---

## Functions

**count_nucleotide(sequence)**
Returns the count of each nucleotide (A, T, G, C) as a dictionary.

**GC_content(sequence)**
Returns GC content percentage. Formula: (G+C) / total length x 100.

**transcribe(sequence)**
Converts DNA to RNA by replacing every T with U.

**reverse_complement(sequence)**
Returns the reverse complement using a complement map dictionary.

**read_fasta(filename)**
Reads a FASTA file line by line, skips the header line starting with ">", strips newline characters from each line, and joins all sequence lines into one clean continuous DNA string.

---

## Files in this repo

- **app.py** - Streamlit web app, upload any FASTA file and get instant analysis
- **dna_function.py** - core functions built from scratch
- **project1_final.py** - terminal script applied to full TP53 RefSeq sequence
- **TP53_full.fasta** - complete human TP53 mRNA (NM_000546.6, 2512 bp)
- **requirements.txt** - libraries needed to run

---

## How to run locally

Install dependencies: pip install biopython matplotlib streamlit
Run the web app: streamlit run app.py
Run the terminal analysis: python project1_final.py

---

## Validated With

- Accession: NM_000546.6
- Description: Homo sapiens tumor protein p53 (TP53), transcript variant 1, mRNA
- Length: 2512 bp
- GC content: 53.38%

All five functions cross-validated against Biopython's built-in SeqIO and gc_fraction — results match exactly.

---

## Tools and Libraries

- Python 3.14
- Biopython (SeqIO, gc_fraction)
- Matplotlib
- Streamlit

---

## Note

This tool accepts FASTA files containing a single DNA sequence.
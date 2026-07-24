#Streamlit web app - upload any FASTA file for instant DNA analysis

import streamlit as st
import matplotlib.pyplot as plt
from dna_function import count_nucleotide, GC_content, reverse_complement, transcribe

st.title("DNA Sequence Analyser")
st.write("This tool is designed to take any DNA FASTA file and analyse the sequence to give its GC content, nucleotide composition, reverse complement and RNA transcript within seconds.")
st.write("Note: Upload a FASTA file containing a single DNA sequence.")
uploaded_file = st.file_uploader("Upload a FASTA file", type=["fasta"])
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    lines = content.splitlines()
    sequence = ""
    for line in lines:
        if not line.startswith (">"):
            sequence = sequence + line.strip()
    st.write("Sequence Successfully Loaded")

    st.write("Nucleotide Count : ")
    st.write(count_nucleotide(sequence))
    st.write("GC Content (%) : ")
    st.write(GC_content(sequence))
    st.write("RNA Transcript : ")
    st.text_area("", transcribe(sequence), height=150)
    st.write("Reverse Complement : ")
    st.text_area("", reverse_complement(sequence), height=150)
    

    #Data Visualization
    counts = count_nucleotide(sequence)
    fig, ax = plt.subplots()
    ax.bar(counts.keys(), counts.values(), color=["blue","green","red","orange"])
    ax.set_xlabel("Nucleotide")
    ax.set_ylabel("Count")
    ax.set_title("Nucleotide Composition")
    st.pyplot(fig)
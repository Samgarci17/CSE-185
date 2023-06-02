import argparse
from bwtSearch import *
import fastq as fq
import miniFasta as mf
from sequence_align.pairwise import hirschberg, needleman_wunsch

def main():
    parser = argparse.ArgumentParser(
        prog='mem',
        description='Command-line script to perform sequence alignment on fastq sequences using an index of a reference genome'
    )
    parser.add_argument('fa_file',  type=str)
    parser.add_argument('fq1_file',  type=str)
    parser.add_argument('fq2_file', nargs='?', type=str)
    args = parser.parse_args()

    genome_string = mf.read(args.fa_file, seq=True)
    genome_string = list(genome_string)
    genome_string = genome_string[0]
    fos1 = fq.read(args.fq1_file) # Iterator of fastq entries.
    if args.fq2_file:
        fos2 = fq.read(args.fq2_file)
    fos1 = list(fos1) # Cast to list
    print(genome_string)
    for x in fos1:
        seq = x.getSeq()
        print(bwtfind(genome_string, seq, len(seq)//100))

if __name__ == "__main__":
    main()

#!/usr/bin/env python

'''
Command line script to create an index file from a dna dequence as well as auxillary data structues that assist with local alignment.

'''
from pathlib import Path
from util import *
import argparse
import fastq as fq
from dnazip.encoder import FullEncoder
import miniFasta as mf



def main():
    parser = argparse.ArgumentParser(
        prog='index',
        description='Index database sequences in the FASTA format.'
    )

    outdir = os.getcwd()
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    parser.add_argument('fa',
                    type=str)
    args = parser.parse_args()

    fasta_strings = mf.read(args.fa, seq=True)
    fasta_strings = list(fasta_strings)
    f = open(outdir + 'sequence.txt', 'w')
    genome = fasta_strings[0]
    for x in fasta_strings:
        f.write(x)
    f.close()
    encode = FullEncoder(outdir + r'sequence.txt')
    encode.full_zip()
    bwtmf = buildBWTMF(list(encode.bw_encoder.bwt), genome, 100)

    
    f = open(outdir + 'partialSuffixArray.txt', 'w')
    f.write(''.join(str(bwtmf[0])))
    f.close
    f = open(outdir + 'occurenceArray.txt', 'w')
    f.write(''.join(str(bwtmf[1])))
    f.close
    f = open(outdir + 'countArray.txt', 'w')
    f.write(''.join(str(bwtmf[2])))
    f.close

if __name__ == "__main__":
    main()




import argparse
import fastq as fq
from sys import getsizeof
from dnazip.encoder import FullEncoder
import miniFasta as mf


def sortArr(e):
    return e[1]

def sufArr(text):
    arr = []
    ans = []
    for i in range(len(text)):
        suffix = text[i:]
        pair = (i,suffix)
        arr.append(pair)
    arr.sort(key=sortArr)

    for x in arr:
        ans.append(x[0])
    return ans

def buildPSA(text, k):
    text+='$'
    sa = sufArr(text)
    psa = [sa[x] for x in range(len(sa)) if x%k==0]
    return psa

def buildOccurrence(bwt):
    occ = {'$':'Null','A':'Null','C':'Null','G':'Null','T':'Null'}
    bwt = bwt.copy()
    bwt.sort()
    for x in range(0,len(bwt)):
        if occ[bwt[x]] == 'Null':
            occ[bwt[x]] = x

    return occ

def buildCheckpoint(bwt, k):
    check = {'$':[(0,0)],'A':[(0,0)],'C':[(0,0)],'G':[(0,0)],'T':[(0,0)]}
    c_a, c_, c_t, c_g, c_c = 0, 0, 0, 0, 0
    for x in range(len(bwt)):
        match bwt[x]:
            case 'A':
                c_a += 1
                
            case 'C':
                c_c += 1
                
            case 'G':
                c_g += 1
                
            case 'T':
                c_t += 1
                
            case '$':
                c_ += 1
        if x%k == 0 or x%k == k:

            check['A'].append((c_a, x))
            check['C'].append((c_c, x))
            check['T'].append((c_t, x))
            check['G'].append((c_g, x))
            check['$'].append((c_, x))

    return check

def buildBWTMF(bwt, text, k):
    psa = buildPSA(text, k)
    occ = buildOccurrence(bwt)
    count = buildCheckpoint(bwt, k*4)

    return psa, occ, count


def main():
    parser = argparse.ArgumentParser(
        prog='index',
        description='Index database sequences in the FASTA format.'
    )
    parser.add_argument('fa',  type=str)
    parser.add_argument('-p',  type=str, help='Prefix of the output database [same as db filename]')
    args = parser.parse_args()
    args.fa

    fasta_strings = mf.read(args.fa, seq=True)
    fasta_strings = list(fasta_strings)
    f = open('sequence.txt', 'w')
    genome = fasta_strings[0]
    for x in fasta_strings:
        f.write(x)
    f.close()
    encode = FullEncoder(r'sequence.txt')
    encode.full_zip()
    bwtmf = buildBWTMF(list(encode.bw_encoder.bwt), genome, 100)
    f = open('partialSuffixArray.txt', 'w')
    f.write(''.join(str(bwtmf[0])))
    f.close
    f = open('occurenceArray.txt', 'w')
    f.write(''.join(str(bwtmf[1])))
    f.close
    f = open('countArray.txt', 'w')
    f.write(''.join(str(bwtmf[2])))
    f.close

if __name__ == "__main__":
    main()




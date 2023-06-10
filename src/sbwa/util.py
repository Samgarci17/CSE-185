import argparse
import fastq as fq
from dnazip.encoder import FullEncoder
import miniFasta as mf
import os


def sortArr(e):
    return e[1]

def sufArr(text):
    '''
    Builds a suffix array from text using a naive implementation

    Parameters
    ----------
    text: string
        text to build suffix array from 


    Returns 
    -------
    ans: list
        list containing the indices corresponding to the sorted suffixes of text
    '''
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
    '''
    Builds the list of every k indice from the suffix array

    Parameters
    ----------
    bwt: string
        The bwt of the genomic sequence

    k: int
        The k value that reduces the size of psa by k


    Returns 
    -------
    check: list
        partial suffix array reduced by a size of k from sa
    '''
    text+='$'
    sa = sufArr(text)
    psa = [sa[x] for x in range(len(sa)) if x%k==0]
    return psa

def buildOccurrence(bwt):
    '''
    Builds a dict containting the index corresponding to the first occurence of every letter in the bwt alphabet

    Parameters
    ----------
    bwt: string
        The bwt of the genomic sequence


    Returns 
    -------
    occ: dict
        The dict holding the first occurences
    '''
    occ = {'$':'Null','A':'Null','C':'Null','G':'Null','T':'Null'}
    bwt = bwt.copy()
    bwt.sort()
    for x in range(0,len(bwt)):
        if occ[bwt[x]] == 'Null':
            occ[bwt[x]] = x

    return occ

def buildCheckpoint(bwt, k):
    '''
    Builds the dict containing the amount of characters seen at every 4k index

    Parameters
    ----------
    bwt: string
        The bwt of the genomic sequence

    k: int
        The k value that reduces the size of check by 4k


    Returns 
    -------
    check: dict
        dict containing the amount of characters seen at every 4k index
    '''
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
    '''
    Build the auxillary arrays for alignment from the BWT of a string 

    Parameters
    ----------
    bwt: string
        The bwt of the genomic sequence

    text: string
        The original string that has been transformed

    k: int
        The k value that reduces the size of the psa array by k and count by 4k


    Returns 
    -------
    psa: list
        list of every k indice from the suffix array

    occ: dict 
        dict containting the index corresponding to the first occurence of every letter in the bwt alphabet

    count: dict
        dict containing the amount of characters seen at every 4k index
    '''
    psa = buildPSA(text, k)
    occ = buildOccurrence(bwt)
    count = buildCheckpoint(bwt, k*4)

    return psa, occ, count

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')  # return an open file handle
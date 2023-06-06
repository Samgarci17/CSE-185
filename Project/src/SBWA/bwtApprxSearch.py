import random
global k 
k = 2

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

def buildBWT(text):
    text += '$'
    suffixArr = sufArr(text)
    bwt = [x for x in range(len(text))]
    for i in range(len(text)):
        bwt[i] = text[suffixArr[i]-1]

    return bwt
    
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
    check = {'$':[0],'A':[0],'C':[0],'G':[0],'T':[0]}
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
        if x%k == 0 or k:

            check['A'].append(c_a)
            check['C'].append(c_c)
            check['T'].append(c_t)
            check['G'].append(c_g)
            check['$'].append(c_)

    return check

def getCheckpoint(symbol, stop, bwt, check):
    start = (stop)//k
    count = check[symbol][start]
    for i in range(start,stop):
        if bwt[i] == symbol:
            count += 1
    print(len(bwt),start,stop)
    return count

#FIX GET CHECKPOINT AS IT DOES NOT HAVE THE RIGHT SEARCH INTERVAL WHEN LOOKING THROUGH BWT FOR POTENTIAL ADDITIONS TO THE CURRENT COUNT OF A SYMBOL AT THE INDEX TOP OR BOTTOM, SEARCH INTERVAL SHOULD BE FROM THE INDEX X TO Y IN BWT BUT IS CURRENTLY X IN CHECK ARRAY WHCI IS SMALLER BY %K TO Y IN BWT, SO EITHER SAVE THE CORRESPONGING INDEX WHEN BUILDNG THE ARRAY OR LOOK AT THE PAPER AGAIN AND SEE HOW THEY ACCESS...

'''def seedExt():
    pass

def seed(pattern, d=3):
    seeds = []
    vals = []
    while len(vals) < d:
        pick = random.randrange(1,len(pattern))
        if not vals.count(pick):
            vals.append(pick)
    vals.sort()
    prev = 0
    for x in vals:
        x = x - prev
        split = pattern[:x]
        pattern = pattern[x:]
        seeds.append(split)
        prev += len(split)

    seeds.append(pattern)

    return seeds'''

def getIdx(psa, idx, bwt):
    pass


def exactsearch(bwt, occ, check, pattern,curr):
    top = 0
    bottom = len(bwt)-1
    while top <= bottom:
        if len(pattern) > 0:
            empty = False
            symbol = pattern[-1]
            pattern = pattern[:-1]
            for i in range(top, bottom+1):
                if bwt[i] == symbol:
                    empty = True
            if empty:
                top = occ[symbol] + getCheckpoint(symbol, top, bwt, check)
                bottom = occ[symbol] + getCheckpoint(symbol, bottom+1, bwt, check)-1
                curr += symbol
                print(top,bottom)
            else: #if mismatch
               return 0
               ''' if len(curr) > min_len:
                    if mismatch < 3:
                        mismatch += 1
                        for x in range(top, bottom):
                            idx = search(bwt, occ, check, pattern+bwt[x], min_len, curr, mismatch)
                            if idx > 0:
                                return idx'''  
        else:
            return bottom - top + 1, curr
        
def build(text, pattern):
    testbwt = buildBWT(genome)
    testpsa = buildPSA(genome, k)
    testocc = buildOccurrence(testbwt)
    testcheck = buildCheckpoint(testbwt,k)
    min_l, curr, d = len(query)//5*2, '', 0
    return testbwt, testpsa, testocc, testcheck, min_l, curr, d

def findindex(bwt, psa, idx, check, occ):
    curr = bwt[idx]
    next = occ[curr] + getCheckpoint(curr, idx, bwt, check)


query = 'TAT'
genome = 'GGCTATAGT' 

def main():
    functions = build(genome, query)
    idx = exactsearch(functions[0], functions[2], functions[3], query, functions[5])
    print(idx)


if __name__ == "__main__":
    main()
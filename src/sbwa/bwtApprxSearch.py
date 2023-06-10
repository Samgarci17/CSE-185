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

def getCheckpoint(symbol, stop, bwt, check):
    start = (stop)//k
    pair = check[symbol][start]
    count = pair[0]
    start = pair[1]
    for i in range(start+1, stop):
        if bwt[i] == symbol:
            count += 1
    return count

def exactsearch(bwt, occ, check, pattern, q_string, a_string, mismatch):
    top = 0
    bottom = len(bwt)-1
    while top <= bottom:
        print(top, bottom)
        print(pattern,'original')
        if len(pattern) > 0:
            empty = False
            symbol = pattern[-1]
            pattern = pattern[:-1]
            for i in range(top, bottom+1):
                if bwt[i] == symbol:
                    empty = True
            if empty:
                print(pattern,'match')
                top = occ[symbol] + getCheckpoint(symbol, top, bwt, check)
                bottom = occ[symbol] + getCheckpoint(symbol, bottom+1, bwt, check)-1
                a_string = symbol + a_string
            elif mismatch < 3: 
                for i in range(top, bottom+1):
                    print(pattern,'mismatch')
                    print(pattern+bwt[i],'new search')
                    ans = exactsearch(bwt, occ, check, pattern+bwt[i], q_string, a_string, mismatch)
                    if ans != None:
                        return ans
                #return 0
                    ''' if len(curr) > min_len:
                    if mismatch < 3:
                        mismatch += 1
                        for x in range(top, bottom):
                            idx = search(bwt, occ, check, pattern+bwt[x], min_len, curr, mismatch)
                            if idx > 0:
                                return idx'''  
            else:
                return None
        else:
            return bottom, top, a_string
        
def build(text, pattern):
    testbwt = buildBWT(genome)
    testpsa = buildPSA(genome, k)
    testocc = buildOccurrence(testbwt)
    testcheck = buildCheckpoint(testbwt,k)
    min_l = len(query)//5*2
    return testbwt, testpsa, testocc, testcheck, min_l

def findindex(bwt, psa, top, bottom, check, occ):
    pass


query = 'AGCGGC'
genome = 'GGCTATAGTGGCTATAGT' 

def main():
    functions = build(genome, query)
    idx = exactsearch(functions[0], functions[2], functions[3], query, '', '', 0)    
    alignment = idx[2]
    i = idx[0]
    j = idx[1]



if __name__ == "__main__":
    main()
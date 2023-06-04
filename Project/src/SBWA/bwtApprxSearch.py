import random
k = 3

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
    for x in range(0,len(bwt)):
        if occ[bwt[x]] == 'Null':
            occ[bwt[x]] = x

    return occ

def buildCheckpoint(bwt, k):
    check = {'$':[],'A':[],'C':[],'G':[],'T':[]}
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
        if x%k == 0:

            check['A'].append(c_a)
            check['C'].append(c_c)
            check['T'].append(c_t)
            check['G'].append(c_g)
            check['$'].append(c_)

    return check

def getCheckpoint(symbol, stop, bwt, check):
    start = stop//k 
    count = check[symbol][start]
    for i in range(start+1,stop):
        if bwt[i] == symbol:
            count += 1
    
    return count


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

def search(bwt, psa, occ, check, pattern):
    '''seeds = seed(pattern)
    for seed in seeds:
        for x in range(len(seed),0,-1):
            seed[x]'''
    
    top = 0
    bottom = len(bwt)-1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern[-1]
            pattern = pattern[:len(pattern)]
            if occ[symbol] > top and occ[symbol] < bottom:
                top = occ[symbol] + getCheckpoint(symbol, top, bwt, check)
                bottom = occ[symbol] + getCheckpoint(symbol, bottom+1, bwt, check)-1
            else:
                return 0
        else:
            return bottom - top + 1
        

ans_bwt = 'TTCCTAACG$A'
test_bwt = buildBWT('TACATCACGT')

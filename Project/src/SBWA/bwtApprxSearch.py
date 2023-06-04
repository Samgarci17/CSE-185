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



def getCheckpoint():
    pass

def search():
    pass

ans_bwt = 'TTCCTAACG$A'
test_bwt = buildBWT('TACATCACGT')
print(buildCheckpoint(test_bwt,3))
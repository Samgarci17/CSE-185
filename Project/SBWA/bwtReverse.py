
def sortArr(e):
    return e[0]

def buildMatrix(text):
    bwt = []
    first_col = []
    val = {}
    for c in text:
        val[c] = 0
    for c in text:
        count = val[c]
        count += 1
        duo = (c, count)
        val[c] = count
        bwt.append(duo)
        first_col.append(duo)
        
    first_col.sort(key=sortArr)

    return bwt, first_col

def inverse(text):
    ans = buildMatrix(text)
    last = ans[0]
    first = ans[1]
    inv_string = []

    char = ('$', 1)
    while(len(inv_string) != len(first)):
        for i in range(len(first)):
            if last[i] == char:
                char = first[i]
                inv_string.append(char[0])
                break
    
    return ''.join(inv_string)
                
            
'''prac = 'ard$rcaaaabb'
print(inverse(prac))'''

'''f = 'dataset_865528_11.txt'
text = []
with open(f, 'r') as file:
    for line in file:
        l = line.strip()
        text.append(l)

ans = inverse(text[0])

f = open('out.txt', 'w')
print(ans, file = f)
f.close()'''
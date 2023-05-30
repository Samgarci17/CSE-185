import argparse

def bwt(text):
    text += '$'
    transformation = ''
    arr = [text]
    char = text[len(text)-1]
    for i in range(len(text)-1):
        text = text[:len(text)-1]
        text = char + text
        char = text[len(text)-1]
        arr.append(text)
    arr.sort()
    for x in arr:
        transformation += x[len(x)-1]
    
    return transformation

parser = argparse.ArgumentParser()
parser.add_argument('command', choices=['index', 'mem'])
parser.add_argument('idx',  type=str)
args = parser.parse_args()
cmd = args.command
if cmd == 'index':
    text = ''
    genome = args.idx
    f = open(genome,'r')
    text = f.readline()
    f.close()

    indexFile = bwt(text)
    print(indexFile)

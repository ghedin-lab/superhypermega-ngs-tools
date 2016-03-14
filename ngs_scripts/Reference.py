import sys
import os.path
import os


def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def open_fasta(someref):
    filename = '../FILES/reference/'+someref
    # print filename
    segdict = {}
    with open(filename) as fp:
        for name, seq in read_fasta(fp):
            segdict[name[1:]] = seq
    return segdict

def open_fasta_path(someref):
    filename = someref
    segdict = {}
    with open(filename) as fp:
        for name, seq in read_fasta(fp):
            segdict[name[1:]] = seq
    return segdict

def return_segmentlist(someref):
    filename = '../FILES/reference/'+someref
    seglist = []
    with open(filename) as fp:
        for name, seq in read_fasta(fp):
            seglist.append(name[1:])
    return seglist 

def return_segmentlist_path(someref):
    filename = someref
    seglist = []
    with open(filename) as fp:
        for name, seq in read_fasta(fp):
            seglist.append(name[1:])
    return seglist 
# i = open_fasta('flua_reference.fa')

# for k in i:
#     print k,len(i[k])
#     
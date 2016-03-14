import os,sys
import glob
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ngs_scripts.ReadMetaCSV import getSampleDict
somedict = getSampleDict()
# 
# SEGMENT = 'PB2'
reversedict = {}
for key in somedict:
    reversedict[somedict[key].key] = somedict[key].sample
SEGLIST = ['PB2','PB1','PA','HA','NP','NA','MP','NS']

path = '../FILES/fullvarlist'

def printfun(thesampleid,row):
    ntpos = int(row[2])
    major = row[4]
    majorfreq = float(row[5])
    minor = row[6]
    minorfreq = float(row[7])
    binocheck = row[3]
    coverage = float(row[12])  
    covertype = 'good'
    if int(coverage) <= 200: 
        covertype = 'worst'
    elif int(coverage) <= 1000:
        covertype = 'bad'
    # elif int(coverage) >= 5000:
    #     coverage = 5000
    # printlist = [thesampleid,ntpos,'major',major,majorfreq,thetype]
    # printlist = [str(x) for x in printlist]
    # print>>thefile,','.join(printlist)
    printlist = [thesampleid,SEGMENT,ntpos,coverage,covertype]
    printlist = [str(x) for x in printlist]
    print>>thefile,','.join(printlist)

for SEGMENT in SEGLIST:
    thefile = open(SEGMENT+"_coverage_formatted.csv",'w')
    print>>thefile,'sample,segment,ntpos,coverage,covertype'


    for infile in glob.glob( os.path.join(path+'/', '*'+SEGMENT+'*.csv') ):
        # print infile
        samplename = os.path.basename(infile).split('.')[0]
        samplename = reversedict[samplename]
        print samplename
        with open(infile,'rU') as f:
            alist = [map(str, line.split(',')) for line in f]
        alist = alist[1:]
        # sampleid = alist[0][0]
        # if somedict[sampleid].generation == 'F0':
        # samplename = 
        for row in alist:
            # sampleid = row[0]
            printfun(samplename,row)




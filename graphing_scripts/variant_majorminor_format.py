import os,sys
import glob
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ngs_scripts.ReadMetaCSV import getSampleDict
somedict = getSampleDict()

reversedict = {}
for key in somedict:
    reversedict[somedict[key].key] = somedict[key]
# 
# SEGMENT = 'PB2'
STRAIN = 'FLU'
strain = 'FLU'
# SEGLIST = ['PB2','PB1','PA','HA','NP','NA','MP','NS']
MINORFREQ_CUTOFF = 0.01
SEGLIST = ['HA']

path = '../FILES/fullvarlist/'

def printfun(thesampleid,row,truentlist):
    ntpos = int(row[2])
    major = row[4]
    majorfreq = float(row[5])
    minor = row[6]
    minorfreq = float(row[7])
    binocheck = row[3].upper()
    coverage = float(row[12])  
    covertype = 'good'
    if int(coverage) <= 200: 
        covertype = 'worst'
    elif int(coverage) <= 1000:
        covertype = 'bad'
    elif int(coverage) >= 5000:
        coverage = 5000

    if strain == STRAIN:
        if ntpos in truentlist:
            printlist = [thesampleid,SEGMENT,ntpos,'major',major,coverage,covertype]
            printlist = [str(x) for x in printlist]
            print>>thefile,','.join(printlist)

            if binocheck == 'TRUE' and minorfreq >= MINORFREQ_CUTOFF and coverage >= 1000:

                printlist = [thesampleid,SEGMENT,ntpos,'minor',minor,coverage,covertype]
                printlist = [str(x) for x in printlist]
                print>>thefile,','.join(printlist)
            else:
                printlist = [thesampleid,SEGMENT,ntpos,'minor','',0,covertype]
                printlist = [str(x) for x in printlist]
                print>>thefile,','.join(printlist)



for SEGMENT in SEGLIST:
    unionlist = []

    for infile in glob.glob( os.path.join(path, '*'+SEGMENT+'*.csv') ):
        samplename = os.path.basename(infile).split('.')[0]
        print samplename
        with open(infile,'rU') as f:
            alist = [map(str, line.split(',')) for line in f]
        alist = alist[1:]

        for row in alist:

            ntpos = int(row[2])
            major = row[4]
            majorfreq = float(row[5])
            minor = row[6]
            minorfreq = float(row[7])
            binocheck = row[3].upper()
            coverage = float(row[12])

            if binocheck == 'TRUE' and minorfreq >= MINORFREQ_CUTOFF and strain == STRAIN and coverage >= 1000:
                unionlist.append(ntpos)

unionlist = list(set(unionlist))
    

for SEGMENT in SEGLIST:
    thefile = open(SEGMENT+"_majorminor_"+str(MINORFREQ_CUTOFF)+"_"+STRAIN+".csv",'w')
    print>>thefile,'sample,segment,ntpos,majmin,nt,coverage,covertype'


    for infile in glob.glob( os.path.join(path, '*'+SEGMENT+'*.csv') ):
        samplename = os.path.basename(infile).split('.')[0]
        samplename = reversedict[samplename].sample
        with open(infile,'rU') as f:
            alist = [map(str, line.split(',')) for line in f]
        alist = alist[1:]

        for row in alist:
            printfun(samplename,row,unionlist)



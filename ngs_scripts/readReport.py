import sys,os,glob
import os.path
import numpy as np
from scipy.stats.distributions import binom
import pysam
import operator
import time
import argparse
from natsort import natsort
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ngs_scripts.Reference import *
# from ngs_scripts.ReadMetaCSV import getSampleDict

start_time = time.time()
#A value of 0 will return an N
parser = argparse.ArgumentParser()
parser.add_argument('--refname','-r',type=str,default='flua_reference.fa',help='indicate reference name found inside ../FILES/reference/')
parser.add_argument('--refpath','-R',help='give full path to reference. Needs full path if not local!')
parser.add_argument('--skipqual','-k',action='store_true',default=False,help='skip quality (usually for minion or pacbio)')
parser.add_argument('--infile','-i',help='input single bamfile. Needs full path if not local!')
parser.add_argument('--segment','-s',help='input single segment')
parser.add_argument('--phredq','-q',type=int,default=20,help='phred quality cutoff (default is at 20)')
parser.add_argument('--cutoff','-c',type=float,default=0.01,help='minor variant frequency cutoff (default is at 0.03)')
parser.add_argument('--strain','-T',type=str,default='FLU',help='need strain')
parser.add_argument('--allowdel','-d',action='store_true',default=False,help='allow deletions (default no!)')
parser.add_argument('--verbose','-v',action='store_true',default=False,help='Prints a read report file for every position')
parser.add_argument('--covercutoff','-C',type=int,default=100,help='coverage cutoff for consensus (default is at 100)')
args = parser.parse_args()

def return_aligned_read(cigartup, someread):
    alignedseq = []
    tempidx = 0
    for (i,c) in cigartup:
        if i == 0:
            alignedseq.extend(someread[tempidx:tempidx+c])
            tempidx = tempidx + c
        elif i == 1:
            tempidx = tempidx + c
        elif i == 2:
            pass
        elif i == 3:
            pass
        elif i == 4:
            pass
        else:
            pass
    alignedseq = ''.join(alignedseq)
    # print alignedseq
    return alignedseq


def cigarTranslate(cigartuple):
    newcigarseq = []
    for identifier,length in cigartuple:
        if identifier == 0: #match
            pass
            newcigarseq.extend('M'*length)
        elif identifier == 1: #insertion
            newcigarseq.extend('I'*length)
        elif identifier == 2: #deletion
            pass
        elif identifier == 4: #softclip
            newcigarseq.extend('S'*length)
        elif identifier == 5: #hardclip
            pass
        else:
            print 'strange cigar identifier: '+str(identifier)+ ' == ',cigartuple

    return newcigarseq


def findDeletion(cigartuple): #deletion is found 
    deletioneventlist = []
    counter = 0
    for identifier,length in cigartuple:
        if identifier == 0: #match
            counter = counter + length
        elif identifier == 1: #insertion
            counter = counter + length
        elif identifier == 2: #deletion
            deletioneventlist.append((counter,length))
            counter = counter + length
        elif identifier == 4: #softclip
            counter = counter + length
        elif identifier == 5: #hardclip
            pass #i think i should do nothing with this ...
        else:
            print 'very strange indeed!'

    return deletioneventlist


def analyzeRead(CIGARTUP,CIGARSTR,unfiltidx,unfilt,qual,cigarseq,is_reverse):
    if np.mean(qual) < args.phredq:
        pass
    else:
        if 'D' in CIGARSTR:
            # print CIGARSTR
            # print unfiltidx
            # print unfilt
            deltuples = findDeletion(CIGARTUP)
            if not deltuples: #might be redundant
                pass
            else:
                for event,delLength in deltuples:
                    for i in range(delLength):
                        unfiltidx.insert(event,'GIVEPREVIOUS')
                        unfilt.insert(event,'-')
                        qual.insert(event,30)
                        cigarseq.insert(event,'D')

        # if 'D' in CIGARSTR:
        #     print CIGARSTR
        #     print cigarseq
        #     print 'beep',len(unfiltreadidx),len(unfilt),len(qual),len(cigarseq)
        #     print unfiltidx

        # else:
        previdx = 0
        recent = 'B'
        for counteridx, (c,idx,soment,qual) in enumerate(zip(cigarseq,unfiltidx,unfilt,qual)):

            # print c,idx,soment,qual
            if qual >= args.phredq:
                if c == 'S':
                    recent = 'S'
                elif c == 'M':
                    recent = 'M'
                    previdx = idx

                    # print c,idx,soment,qual
                    # CONSENSUSDICT[str(idx)][soment] = CONSENSUSDICT[str(idx)][soment] + 1
                    # if is_reverse:    
                    #     REVERSE_DICT[str(idx)][soment] = REVERSE_DICT[str(idx)][soment] + 1
                    # else:
                    #     FORWARD_DICT[str(idx)][soment] = FORWARD_DICT[str(idx)][soment] + 1
                    if CONSENSUSDICT[str(idx)].has_key(soment):
                        CONSENSUSDICT[str(idx)][soment] = CONSENSUSDICT[str(idx)][soment] + 1
                    else:
                        CONSENSUSDICT[str(idx)][soment] = 1

                    if is_reverse:
                        if REVERSE_DICT[str(idx)].has_key(soment):
                            REVERSE_DICT[str(idx)][soment] = REVERSE_DICT[str(idx)][soment] + 1
                        else:
                            REVERSE_DICT[str(idx)][soment] = 1
                    else:
                        if FORWARD_DICT[str(idx)].has_key(soment):
                            FORWARD_DICT[str(idx)][soment] = FORWARD_DICT[str(idx)][soment] + 1
                        else:
                            FORWARD_DICT[str(idx)][soment] = 1

                elif c == 'D':
                    recent = 'D'
                    previdx = previdx+1
                    if idx != 'GIVEPREVIOUS':
                        print 'HOLD ON HOLD OANWEOI FANWOEI FJAOWIEJF OAI'
                    # else:
                        # idx = 
                    # CONSENSUSDICT[str(idx)][soment] = CONSENSUSDICT[str(idx)][soment] + 1
                    # if is_reverse:    
                    #     REVERSE_DICT[str(idx)][soment] = REVERSE_DICT[str(idx)][soment] + 1
                    # else:
                    #     FORWARD_DICT[str(idx)][soment] = FORWARD_DICT[str(idx)][soment] + 1
                    if CONSENSUSDICT[str(previdx)].has_key(soment):
                        CONSENSUSDICT[str(previdx)][soment] = CONSENSUSDICT[str(previdx)][soment] + 1
                    else:
                        CONSENSUSDICT[str(previdx)][soment] = 1

                    if is_reverse:
                        if REVERSE_DICT[str(previdx)].has_key(soment):
                            REVERSE_DICT[str(previdx)][soment] = REVERSE_DICT[str(previdx)][soment] + 1
                        else:
                            REVERSE_DICT[str(previdx)][soment] = 1
                    else:
                        if FORWARD_DICT[str(previdx)].has_key(soment):
                            FORWARD_DICT[str(previdx)][soment] = FORWARD_DICT[str(previdx)][soment] + 1
                        else:
                            FORWARD_DICT[str(previdx)][soment] = 1

                elif c == 'I':
                    if recent == 'S' or recent == 'D':
                        recent = 'S'
                    else:
                        recent = 'I'
                        previdx = previdx+1
                        newkey = str(previdx)+'I'
                        # CONSENSUSDICT[str(idx)][soment] = CONSENSUSDICT[str(idx)][soment] + 1
                        # if is_reverse:    
                        #     REVERSE_DICT[str(idx)][soment] = REVERSE_DICT[str(idx)][soment] + 1
                        # else:
                        #     FORWARD_DICT[str(idx)][soment] = FORWARD_DICT[str(idx)][soment] + 1
                        if CONSENSUSDICT.has_key(newkey):
                            if CONSENSUSDICT[newkey].has_key(soment):
                                CONSENSUSDICT[newkey][soment] = CONSENSUSDICT[newkey][soment] + 1
                            else:
                                CONSENSUSDICT[newkey][soment] = 1     
                        else:  
                            CONSENSUSDICT[newkey] = {}
                            if CONSENSUSDICT[newkey].has_key(soment):
                                CONSENSUSDICT[newkey][soment] = CONSENSUSDICT[newkey][soment] + 1
                            else:
                                CONSENSUSDICT[newkey][soment] = 1    


def isGlobalVariant(freqdict):
    #FOR FREQUENCY ONLY
    if args.allowdel:
        pass
    else:
        freqdict['-'] = 0

    total = float(sum(freqdict.values()))
    if total == 0:
        return (False,'X',0.0,'X',0.0)
    else:
        for key in freqdict:
            if key == 'A':
                afreq = freqdict['A']/total
            elif key == 'C':
                cfreq = freqdict['C']/total
            elif key == 'G':
                gfreq = freqdict['G']/total
            elif key == 'T':
                tfreq = freqdict['T']/total
            elif key == '-':
                gapfreq = freqdict['-']/total


        newfreqdict = {'A':afreq,'C':cfreq,'G':gfreq,'T':tfreq,'-':gapfreq}
        varcounter = 0
        for key, value in sorted(newfreqdict.iteritems(), key=lambda (k,v): (v,k), reverse = True):
            if varcounter == 0:
                majornt = key
                majorfreq = value
                varcounter += 1
            elif varcounter == 1:
                minornt = key
                minorfreq = value
                varcounter += 1
        if minorfreq >= args.cutoff:
            # return (True,majornt,majorfreq,minornt,minorfreq)
            return (True,majornt,freqdict[majornt],minornt,freqdict[minornt])
        else:
            return (False,majornt,majorfreq,minornt,minorfreq)


def binomialcheck(majornt,minornt,fordict,revdict):

    if majornt == 'X' or minornt == 'X':
        accept = False
    else:
        forwardMajorCount = fordict[majornt]
        forwardMinorCount = fordict[minornt]

        reverseMajorCount = revdict[majornt]
        reverseMinorCount = revdict[minornt]
        percentVariant = args.cutoff
        ALPHA = 0.05

        pforward = 1 - binom.cdf( forwardMinorCount, (forwardMajorCount + forwardMinorCount), percentVariant)
        preverse = 1 - binom.cdf( reverseMinorCount, (reverseMajorCount + reverseMinorCount), percentVariant)
        if pforward <= ALPHA/2 and preverse <= ALPHA/2:
            accept = True
        else:
            accept = False
    return accept



def returnCodon(sampconsensus,pos,minor): #0-index
    aminoacid = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
    'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
    'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
    'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
    'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
    'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
    'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
    'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
    'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
    'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
    'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
    'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
    'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
    'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
    'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
    'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'}
    # for pos in snvlist:
    pos = int(pos)
    ntpos = pos# - 1
    # minor = snvdict[pos]

    if ntpos % 3 == 0:# first position
        fp = ntpos#,ntpos+1,ntpos+2]
        p2 = ntpos+1
        p3 = ntpos+2

        p1nt = sampconsensus[fp].lower()
        p2nt = sampconsensus[p2].upper()
        p3nt = sampconsensus[p3].upper()

        altcodon = [minor.lower(),p2nt,p3nt]
    elif ntpos % 3 == 1: #second
        p1 = ntpos-1#,ntpos,ntpos+1]
        fp = ntpos
        p3 = ntpos+1

        p1nt = sampconsensus[p1].upper()
        p2nt = sampconsensus[fp].lower()
        p3nt = sampconsensus[p3].upper()

        altcodon = [p1nt,minor.lower(),p3nt]

    elif ntpos % 3 == 2: #third
        # fp = ntpos-2#,ntpos-1,ntpos]
        p1 = ntpos-2
        p2 = ntpos-1
        fp = ntpos

        p1nt = sampconsensus[p1].upper()
        p2nt = sampconsensus[p2].upper()
        p3nt = sampconsensus[fp].lower()
        altcodon = [p1nt,p2nt,minor.lower()]
    # print codon
    aapos = ntpos/3 + 1
    # ref_codon = refseq[fp:fp+3]
    # aa = aminoacid[ref_codon.lower()]
    majorcodon = ''.join([p1nt,p2nt,p3nt])
    try:
        aa = aminoacid[majorcodon.lower()]

        altcodon = ''.join(altcodon)
        alt_aa = aminoacid[altcodon.lower()]

        # print p1nt,p2nt,p3nt
        # print majorcodon
        if aa == alt_aa:
            sameaa = 'syn'
        else:
            sameaa = 'non'
        return aapos,majorcodon,aa,altcodon,alt_aa,sameaa
    except KeyError:
        return aapos,majorcodon,'NaN','NaN','NaN','NaN'
    # print snvdict[pos]

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


if __name__ == '__main__':
    ensure_dir('../FILES/consensus/')
    ensure_dir('../FILES/fullvarlist/')

    STRAIN = 'FLU'
    # STRAIN = args.strain.upper()

    #for future work we'll need to change this! 
    # if STRAIN.upper() == 'H3N2':
    #     REF_FILE = 'flua_cds.fa'
    #     # REF_FILE = 'flua_cds.fa'
    #    # addpath = 'H3N2_BAM/'
    # elif STRAIN.upper() == 'FLUB':
    #     REF_FILE = 'flub_cds.fa'
    #     # REF_FILE = 'flub_reference.fa'
    #    # addpath = 'FLUB_BAM/'
    REF_FILE = 'calref.fa'
    addpath = ''

    refdict = open_fasta(REF_FILE)
    SEGLIST = return_segmentlist(REF_FILE)
    # somedict = getSampleDict()


    samplist = []
    samplebamdict = {}

    if args.infile is None:
        filepath = '../FILES/bamfiles/'+addpath

        for infile in glob.glob( os.path.join(filepath, '*.bam') ):
            # print infile
            PREFIXFILENAME= os.path.basename(infile)

            samplename = PREFIXFILENAME.split('.')[0]
            try:
                samplist.append(samplename)
                samplebamdict[samplename] = pysam.AlignmentFile(infile, "rb" )
            except KeyError:
                print '%s was not found in our metadata!' % (samplename)
    else:
        infile = args.infile #Examining a single input file! 
        PREFIXFILENAME= os.path.basename(infile)

        samplename = PREFIXFILENAME.split('.')[0]
        try:
            samplist.append(samplename)
            samplebamdict[samplename] = pysam.AlignmentFile(infile, "rb" )
        except KeyError:
            print '%s was not found in our metadata!' % (samplename)


    # Default: Do full segment list
    if args.segment is None:
        pass
    else:
        SEGLIST = [args.segment]

    for SEGMENT in SEGLIST:
        print 'examining segment: '+ SEGMENT
        filepath = '../FILES/consensus/'
        if args.infile is None:
            thefile = open(filepath+STRAIN+'.'+SEGMENT+'.'+"consensus.fasta",'w')
        else:
            #for a single case
            PREFIXFILENAME= os.path.basename(infile)
            samplename = PREFIXFILENAME.split('.')[0]
            thefile = open(filepath+samplename+'.'+STRAIN+'.'+SEGMENT+'.'+"consensus.fasta",'w')
        
        seglength = len(refdict[SEGMENT])
        for SAMPLENAME in samplebamdict:
            print 'analyzing ' + SAMPLENAME
            # readreportfile = open(STRAIN+'.'+SAMPLENAME+'.'+SEGMENT+'.'+"readreport.txt",'w')
            # print>>readreportfile,refdict[SEGMENT]

            snplistfile = open('../FILES/fullvarlist/'+SAMPLENAME+'.'+STRAIN+'.'+SEGMENT+'.'+str(args.cutoff)+".snplist.csv",'w')
            print>>snplistfile,'name,segment,ntpos,binocheck,major,majorfreq,minor,minorfreq,A,C,G,T,totalcount,ref_nt,consensus=major?,aa_pos,major_codon,major_aa,minor_codon,minor_aa,nonsyn_syn'

            CONSENSUSDICT = {}
            FORWARD_DICT = {}
            REVERSE_DICT = {}
            #populating our dictionaries|These are global! I don't know if that's a good idea or not.. but it works!
            for idx in range(seglength):
                CONSENSUSDICT[str(idx)] = {}
                FORWARD_DICT[str(idx)] = {}
                REVERSE_DICT[str(idx)] = {}

            consensus = []
            for read in samplebamdict[SAMPLENAME].fetch(SEGMENT):
                cigartup= read.cigartuples
                cigarstr = read.cigarstring
                unfiltreadidx = read.get_reference_positions(full_length=True)
                unfiltread = list(read.query_sequence)
                readqual = read.query_qualities
                cigarseq = cigarTranslate(cigartup)
                analyzeRead(cigartup,cigarstr,unfiltreadidx,unfiltread,readqual,cigarseq,read.is_reverse)

            bigconsensus = []
            keylist = []
            for boop in CONSENSUSDICT:
                keylist.append(boop)

            a = natsort(keylist) #sorting our nucleotide
            coveragechecker = 0


            tempconsensus = []
            for i in a: #move consensus earlier, we're going to need to use it later.
                if 'I' in i: #and sum(CONSENSUSDICT[i].values()) < 200: #Include insertion!?!?!?
                    pass
                else:
                    if sum(CONSENSUSDICT[i].values()) < 200: 
                        coveragechecker+=1

                    # if sum(CONSENSUSDICT[i].values()) < args.covercutoff: #Do we want to filter?!?!?!
                    #     bigconsensus.append('N')
                    #     tempconsensus.append('N')
                    # else:
                    try:
                        rtopval = max(CONSENSUSDICT[i].iteritems(), key=operator.itemgetter(1))[0]
                        bigconsensus.append(rtopval)
                        tempconsensus.append(rtopval)
                    except ValueError:
                        bigconsensus.append('N')
                        tempconsensus.append('N')
            if float(coveragechecker)/seglength >= .40:
                print>>thefile,'>'+SAMPLENAME+' '+SEGMENT+' POORCOVERAGE'
                print>>thefile,''.join(bigconsensus)
            else:
                print>>thefile,'>'+SAMPLENAME+' '+SEGMENT
                print>>thefile,''.join(bigconsensus)               



            for i in a:
                if 'I' in i: #and sum(CONSENSUSDICT[i].values()) < 200: #Include insertion!?!?!?
                    pass
                else:
                    true_i = str(int(i) + 1) #1 based
                    x = CONSENSUSDICT[i]
                    f = FORWARD_DICT[i]
                    r = REVERSE_DICT[i]
                    validlist = 'ACGT-'
                    for keynt in validlist:
                        if x.has_key(keynt):
                            pass
                        else:
                            x[keynt] = 0

                        if f.has_key(keynt):
                            pass
                        else:
                            f[keynt] = 0

                        if r.has_key(keynt):
                            pass
                        else:
                            r[keynt] = 0
      


                    checkvar = isGlobalVariant(x)
                    # if checkvar[0] == True:

                    accepted = binomialcheck(checkvar[1],checkvar[3],f,r)

                    sorted_dict = sorted(x.iteritems(), key=lambda item: -item[1])
                    majornt= sorted_dict[0][0]
                    majorcount = sorted_dict[0][1]
                    minornt = sorted_dict[1][0]
                    minorcount = sorted_dict[1][1]
                    ntTotal = float(sum(x.values()))

                    if ntTotal != 0:
                        majorfreq = majorcount/ntTotal
                        minorfreq = minorcount/ntTotal
                    else:
                        majorfreq = 0.0
                        minorfreq = 0.0
                    refnt = refdict[SEGMENT][int(i)]
                    if refnt.upper() != majornt.upper():
                        samecheck = 'no'
                    else:
                        samecheck = 'yes'
                    # if float(minorfreq)<= args.cutoff:
                    #     returnCodon(tempconsensus,int(i),minornt)
                    # aa_pos,major_codon,major_aa,minor_codon,minor_aa,nonsyn_syn
                    if SEGMENT == 'MP' or SEGMENT == 'NS':
                        aapos = ''
                        majorcodon = ''
                        aa = ''
                        altcodon = ''
                        alt_aa = ''
                        sameaa = ''
                    else:
                        aapos,majorcodon,aa,altcodon,alt_aa,sameaa = returnCodon(tempconsensus,int(i),minornt)

                    if float(minorfreq) <= args.cutoff: 
                        printlist = [SAMPLENAME,SEGMENT,true_i,str(accepted),majornt,str(majorfreq),'',str(minorfreq),str(x['A']),str(x['C']),str(x['G']),str(x['T']),str(ntTotal),refnt,samecheck,str(aapos),majorcodon,aa,'','','']
                    else:
                        printlist = [SAMPLENAME,SEGMENT,true_i,str(accepted),majornt,str(majorfreq),minornt,str(minorfreq),str(x['A']),str(x['C']),str(x['G']),str(x['T']),str(ntTotal),refnt,samecheck,str(aapos),majorcodon,aa,altcodon,alt_aa,sameaa]

                    print>>snplistfile, ','.join(printlist)






       

print("--- %s seconds ---" % (time.time() - start_time))

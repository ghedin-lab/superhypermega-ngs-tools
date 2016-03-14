import sys
import os.path
import os
import csv

class sampleobject:
    #        print sampleid,strain,school,swabDate,symptomDate,familyILI
    def __init__(self, unique, key, sample,resp_tract,day,ferret):
        self.unique = unique
        self.key = key
        self.sample = sample.upper()
        self.resp_tract = resp_tract.upper()
        self.day = day
        self.ferret = ferret
        # self.familyili = familyili
        self.hasvarlist = False
    def addVarList(self,varlist):
        self.varlist = varlist
        self.hasvarlist = True

def getSampleDict():
    # relpath =  os.getcwd()
    filename = '../FILES/parent_fd_metadata.csv'

    # ReadMetaCSV
    sampdict = {}
    with open(filename,'rU') as csvfile:
        metareader = csv.reader(csvfile, delimiter=',')
        # header = metareader[0]
        # print header
        counter = 0
        for row in metareader:
            if counter == 0:
                counter+=1
            else:
                unique = row[0]
                key = row[1]
                sample = row[2]
                resp_tract = row[3]
                day = row[4]
                ferret = row[5].rstrip()
                # sampleid = row[-1].rstrip().zfill(3)
                # strain = row[-2]
                
                sampobj = sampleobject(unique,key,sample,resp_tract,day,ferret)
                sampdict[unique] = sampobj
    return sampdict
if __name__ == '__main__':

    wee = getSampleDict()

    for k in wee:
        print k,wee[k].sample

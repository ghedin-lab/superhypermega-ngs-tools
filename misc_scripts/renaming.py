import os,sys
import glob
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ngs_scripts.ReadMetaCSV import getSampleDict

reversedict = {}
somedict = getSampleDict()

for key in somedict:
    reversedict[somedict[key].key] = key

#for the unmapped files
# path = '../../../fludynamo/mappedfiles/'
# for infile in glob.glob( os.path.join(path, 'unmapped*') ):
#     # print "current is fileo: " + infile
#     filename = os.path.basename(infile)
#     path = os.path.dirname(infile)
#     parts = filename.split('.')
#     # print parts 
#     querykey = parts[2]
#     newkey = reversedict[querykey]

#     printname = [newkey,parts[0],parts[1],'fastq']
#     newpath = path+'/'+'.'.join(printname)
#     os.system('mv '+infile+' '+newpath)


#for the mapped files
# path = '../../../fludynamo/mappedfiles/bowtiemapped/'
# for infile in glob.glob( os.path.join(path, '*bai') ):
#     # print "current is fileo: " + infile
#     filename = os.path.basename(infile)
#     path = os.path.dirname(infile)
#     parts = filename.split('.')
#     # print parts 
#     querykey = parts[0]
#     # newkey = somedict[querykey]
#     newkey = somedict[reversedict[querykey]].sample
#     queryunique = somedict[reversedict[querykey]].unique
#     printname = [queryunique,'flu','miseq',newkey,parts[2],parts[3]]
#     # print printname
#     newpath = path+'/'+'.'.join(printname)
#     # print newpath
#     os.system('mv '+infile+' '+newpath)

## for the fullvarlist
path = '/home/timo/NGS/parent_fd/FILES/fullvarlist/'
for infile in glob.glob( os.path.join(path, '*csv') ):
    # print "current is fileo: " + infile
    filename = os.path.basename(infile)
    path = os.path.dirname(infile)
    parts = filename.split('.')
    # print parts 
    querykey = parts[0]
    # newkey = somedict[querykey]
    newkey = somedict[reversedict[querykey]].sample
    queryunique = somedict[reversedict[querykey]].unique
    printname = [queryunique,'flu','miseq',newkey,parts[2],parts[3],parts[4],parts[5],parts[6]]
    # print printname
    newpath = path+'/'+'.'.join(printname)
    # print newpath
    os.system('mv '+infile+' '+newpath)


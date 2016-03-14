import sys,os,glob
import synapseclient
from synapseclient import Project, Folder, File, Link

syn = synapseclient.Synapse()

PASSWORD = raw_input()
syn.login('ts2742@nyu.edu', PASSWORD)

somefolder = syn.get('syn5684267')
# print somefolder

# test_entity = File('test_deleteme.txt', description='Fancy new data', parent=somefolder)
# test_entity = syn.store(test_entity)
# path = '../../../fludynamo/mappedfiles/'
path = '../../../fludynamo/mappedfiles/bowtiemapped/'
for infile in glob.glob( os.path.join(path, '*bam') ):
    print "current is fileo: " + infile
    test_entity = File(infile, description='parent mapped bowtie2 --local', parent=somefolder)
    test_entity = syn.store(test_entity)
    

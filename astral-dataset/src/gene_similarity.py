__author__ = 'ashu'
import sys
from quartet_aggregate import unique_quartet
def get_quartets(filepath):
    f = open(filepath,'r')
    q_set=set()
    for line in f:
        q_set.add(unique_quartet(line))
    f.close()
    return q_set
def gene_similarity(filedir,prefix,suffix,gene,numgenes):
    qset = get_quartets(filedir+'//'+prefix+str(gene)+suffix)
    f=open(filedir+'//'+prefix+str(gene)+'_similarity.txt','w')
    for i in range(1,numgenes+1):
        if(i==gene):
            f.write(str(len(qset))+'\n')
        else:
            qset_tmp = get_quartets(filedir+'//'+prefix+str(i)+suffix)
            f.write(str(len(qset & qset_tmp))+'\n')
            del qset_tmp
        print i,' Done'
if __name__ == "__main__":
    filedir = sys.argv[1]
    prefix = sys.argv[2]
    suffix = sys.argv[3]
    gene = int(sys.argv[4])
    numgenes = int(sys.argv[5])
    gene_similarity(filedir,prefix,suffix,gene,numgenes)
    
    

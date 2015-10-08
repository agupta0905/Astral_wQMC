__author__ = 'ashu'
import sys
def check_all_taxa(filepath,n):
    f=open(filepath,'r')
    taxa_set=set()
    for line in f:
        q=line.split(':',1)[0]
        siblings=q.split('|',1)
        i=siblings[0].split(',',1)[0]
        j=siblings[0].split(',',1)[1]
        k=siblings[1].split(',',1)[0]
        l=siblings[1].split(',',1)[1]
        taxa_set.add(int(i))
        taxa_set.add(int(j))
        taxa_set.add(int(k))
        taxa_set.add(int(l))
    f.close()
    for x in range(0,n):
        if x not in taxa_set:
            print x,' not present'
if __name__ == "__main__":
    filepath=sys.argv[1]
    num_taxa=int(sys.argv[2])
    check_all_taxa(filepath, num_taxa)
    
    

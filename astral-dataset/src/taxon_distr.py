__author__ = 'ashu'
import sys
import operator
def get_taxon(filepath):
    f=open(filepath,'r')
    taxa_set=set()
    for line in f:
        q=line.split(':',1)[0]
        v=int(line.split(':',1)[1])
        if(v!=0):
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
    return taxa_set
def get_neighbors(simfile,n):
    f=open(simfile,'r')
    l = []
    for line in f:
        l.append(int(line.replace('\n','')))
    l=sorted(range(len(l)), key=lambda k: l[k])
    l=map(lambda x: x+1, l)
    f.close()
    return l[-n:]
def taxon_distr(fdir,g,n):
    taxon_dict={}
    simfile=fdir+'//gene_'+str(g)+'_similarity.txt'
    n_list=get_neighbors(simfile, n)
    for i in n_list:
        print 'gene', i
        taxa_set=get_taxon(fdir+'//gene_'+str(i)+'_quartets.txt')
        for t in taxa_set:
            if (t in taxon_dict):
                taxon_dict[t]+=1
            else:
                taxon_dict[t]=0
    x = taxon_dict
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    print sorted_x
if __name__ == "__main__":
    fdir = sys.argv[1]
    gene=int(sys.argv[2])
    num_neighbors=int(sys.argv[3])
    taxon_distr(fdir,gene,num_neighbors)
    
    

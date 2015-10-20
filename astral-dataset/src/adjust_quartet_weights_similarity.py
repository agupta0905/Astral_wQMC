__author__ = 'ashu'
import sys
from quartet_aggregate import format, unique_quartet
from adjust_quartet_weights import write
def neighbors(file,n,g):
    f=open(file,'r')
    l = []
    for line in f:
        l.append(int(line.replace('\n','')))
    l=sorted(range(len(l)), key=lambda k: l[k])
    l=map(lambda x: x+1, l)
    return filter(lambda x: x!=g, l[-n:])
    f.close()
def update(dict_list,filepath):
    f=open(filepath,'r')
    for line in f:
        q=unique_quartet(line)
        for i in range(len(dict_list)):
            if q in dict_list[i]:
                dict_list[i][q]+=1
            else:
                dict_list[i][q]=1
    f.close()    
def adjust_quartet_weight_similarity(file_dir,gene,numtaxa,n):
    nlist=neighbors(file_dir+'//gene_'+str(gene)+'_similarity.txt', n, gene)
    wlist=[2,10,25]
    q_dict=[{},{},{}]
    for i in range(numtaxa-3):
        for j in range(len(wlist)):
            q_dict[j][format(i, i+1, i+2, i+3)]=0
    f = open(file_dir+'//gene_'+str(gene)+'_quartets.txt','r')
    for line in f:
        q=unique_quartet(line)
        for i in range(len(wlist)):
            q_dict[i][q]=wlist[i]
    f.close()
    for i in nlist:
        print 'neighbor ',i
        update(q_dict, file_dir+'//gene_'+str(i)+'_quartets.txt')
    for i in range(len(wlist)):
        write(q_dict[i],file_dir+'//gene_'+str(gene)+'_neighbor_'+str(n)+'_w_'+str(wlist[i])+'_quartets.txt')
if __name__ == "__main__":
    file_dir=sys.argv[1]
    gene = int(sys.argv[2])
    numtaxa=int(sys.argv[3])
    numneighbor = int(sys.argv[4])
    adjust_quartet_weight_similarity(file_dir,gene,numtaxa,numneighbor)
    
    

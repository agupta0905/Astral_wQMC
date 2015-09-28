__author__ = 'ashu'
import sys
import os
from random import shuffle
def sample_taxa(path, replicate, k, n):
    f = open(path+'//'+replicate+'//'+'all-genes.phylip', 'r')
    out_folder=path+'//'+replicate+'_sampled_'+str(n-k).zfill(2)
    if not os.path.exists(out_folder):
            os.makedirs(out_folder)
    f_out=open(out_folder+'//all-genes.phylip','w')
    taxa_list=range(0,n)    
    for line in f:
        words=line.split(' ',1)
        if(n==int(words[0])):
            f_out.write(str(n-k)+' '+words[1])
            shuffle(taxa_list)
        elif(int(words[0]) in taxa_list[:n-k]):
            f_out.write(line)

if __name__ == "__main__":
    model_path=sys.argv[1]
    replicate=sys.argv[2]
    num_taxa_remove=int(sys.argv[3])
    total_taxa = int(sys.argv[4])
    sample_taxa(model_path,replicate,num_taxa_remove,total_taxa)
    
    

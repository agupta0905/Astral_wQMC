__author__ = 'ashu'
import sys
def formatted(i,j,k,l):
    if(j<i):
        i,j=j,i
    if(l<k):
        k,l=l,k
    if(k<i):
        return str(k)+','+str(l)+'|'+str(i)+','+str(j)
    else:
        return str(i)+','+str(j)+'|'+str(k)+','+str(l)
def write_all_quartets(dt,out_file_path):
    f = open(out_file_path,'w')
    for k in dt.keys():
            f.write(k+':'+str(dt[k])+'\n')
    f.close() 
def quartet_aggregate(model_dir,r,gene,numgenes,t):
    bin=set()
    f_bin=open(model_dir+'/R'+r+'/'+str(gene)+'/orginal_binning_t_'+str(t)+'.txt','r')
    for line in f_bin:
        bin.add(int(line))
    f_bin.close()
    quartet_dict={}
    taxon_set=set()
    for f in range(1,numgenes+1):
        if(f in bin):
            f_in = open(model_dir+'/R'+r+'/'+str(f)+'/quartets_relabeled.txt','r')
            for line in f_in:
                quartet=line.split(':',1)[0]
                v=int(line.split(':',1)[1])
                siblings=quartet.split('|',1)
                i = siblings[0].split(',',1)[0]
                taxon_set.add(i)
                j = siblings[0].split(',',1)[1]
                taxon_set.add(j)
                k = siblings[1].split(',',1)[0]
                taxon_set.add(k)
                l = siblings[1].split(',',1)[1]
                taxon_set.add(l)
                form_q= formatted(i,j,k,l)
                if form_q in quartet_dict:
                    quartet_dict[form_q]+= v
                else:
                    quartet_dict[form_q]=v
            f_in.close()
            print f," Done"
    write_all_quartets(quartet_dict, model_dir+'/R'+r+'/'+str(gene)+'/allorigbin_t_'+str(t)+'_quartets_relabeled.txt')
    print 'Total Taxa',len(taxon_set)
if __name__ == "__main__":
    model_dir=sys.argv[1]
    replicate=sys.argv[2]
    gene=int(sys.argv[3])
    num_genes=int(sys.argv[4])
    threshold=int(sys.argv[5])
    quartet_aggregate(model_dir,replicate,gene,num_genes,threshold)
    
    

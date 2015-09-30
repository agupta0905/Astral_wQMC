__author__ = 'ashu'
import sys
from quartet_aggregate import format
def write(dict,file):
    f=open(file,'w')
    for k in dict.keys():
        f.write(k+':'+str(dict[k])+'\n')
    f.close()
def get_taxa(q):
    siblings = q.split('|',1)
    i,j = siblings[0].split(',',1)[:]
    k,l = siblings[1].split(',',1)[:]
    return [i,j,k,l]
def adjust_quartet_weight(dir,filename,prefix,suffix,g,w):
    f=open(dir+'//'+filename,'r')
    q_dict={}
    q_dict_tmp={}
    for line in f:
        q=line.split(':',1)[0]
        v=int(line.split(':',1)[1].replace('\n',''))
        q_dict[q]=v
    f.close()
    for i in range(1,g+1):
        del q_dict_tmp
        q_dict_tmp=q_dict.copy()
        f=open(dir+'//'+prefix+str(i)+suffix,'r')
        for line in f:
            qlist=get_taxa(line.split(':',1)[0])
            q=format(int(qlist[0]),int(qlist[1]),int(qlist[2]),int(qlist[3]))
            v=int(line.split(':',1)[1].replace('\n',''))*w
            q_dict_tmp[q]=q_dict_tmp[q]+v-1
        f.close()
        write(q_dict_tmp,dir+'//'+prefix+str(i)+'_w_'+str(w)+suffix)  
        print "Gene-",i," Done" 
if __name__ == "__main__":
    file_dir=sys.argv[1]
    filename=sys.argv[2]
    prefix=sys.argv[3]
    suffix=sys.argv[4]
    num_genes=sys.argv[5]
    weight = sys.argv[6]
    adjust_quartet_weight(file_dir,filename,prefix,suffix,int(num_genes),int(weight))
    
    

__author__ = 'ashu'
import sys
def relabel(tdict,qfilepath):
    outfilepath=qfilepath.rsplit('.',1)[0]+'_relabeled'+qfilepath.rsplit('.',1)[1]
    fin=open(qfilepath,'r')
    fout=open(outfilepath,'w')
    for line in fin:
        q=line.split(':',1)[0]
        v=line.split(':',1)[1]
        siblings=q.split('|',1)
        i=tdict[siblings[0].split(',',1)[0]]
        j=tdict[siblings[0].split(',',1)[1]]
        k=tdict[siblings[1].split(',',1)[0]]
        l=tdict[siblings[1].split(',',1)[1]]
        fout.write(i+','+j+'|'+k+','+l+':'+v)
    fin.close();
    fout.close();
def relabeler(mdir,t_dict_path,r,g):
    mapping={}
    f=open(t_dict_path,'r')
    for line in f:
        key=line.split(' ',1)[0]
        value=line.split(' ',1)[1].replace('\n','')
        mapping[key]=value
    f.close()
    relabel(mapping,mdir+'/R'+r+'/allquartets_sampled_36_numgenes_100.txt')
    for i in range(1,g+1):
        for w in [5,10,25,50]:
            relabel(mapping, mdir+'/R'+r+'/'+str(i)+'/quartets_sampled_36_numgenes_100_w_'+str(w)+'.txt')
        print i
if __name__ == "__main__":
    modeldir=sys.argv[1]
    taxa_dict_path=sys.argv[2]
    replicate=sys.argv[3]
    numgenes=int(sys.argv[4])
    relabeler(modeldir, taxa_dict_path,replicate, numgenes)    
    

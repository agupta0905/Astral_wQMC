__author__ = 'ashu'
import sys
import dendropy
def relabel(tdict,tfilepath):
    toutfilepath=tfilepath.rsplit('.',1)[0]+'_relabeled'+'.'+tfilepath.rsplit('.',1)[1]
    tt=dendropy.Tree.get(
        path=tfilepath,
        schema='newick')
    for i in range(0,len(tt.taxon_namespace)):
        tt.taxon_namespace[i].label=tdict[tt.taxon_namespace[i].label]
    tt.write(path=toutfilepath,schema='newick')
    
def relabeler_trees(mdir,t_dict_path,r,g):
    mapping={}
    f=open(t_dict_path,'r')
    for line in f:
        key=line.split(' ',1)[0]
        value=line.split(' ',1)[1].replace('\n','')
        mapping[key]=value
    f.close()
    for i in range(1,g+1):
        relabel(mapping, mdir+'/R'+r+'/'+str(i)+'/true.gt')
        print i
if __name__ == "__main__":
    modeldir=sys.argv[1]
    taxa_dict_path=sys.argv[2]
    replicate=sys.argv[3]
    numgenes=int(sys.argv[4])
    relabeler_trees(modeldir, taxa_dict_path,replicate, numgenes)    
    

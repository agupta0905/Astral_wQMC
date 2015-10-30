__author__ = 'ashu'
import sys
import dendropy
def get_induced_tree(fulltreepath,subtreepath):
    ftree=dendropy.Tree.get(
            path=fulltreepath,
            schema='newick')
    stree=dendropy.Tree.get(
            path=subtreepath,
            schema='newick')
    ftree.retain_taxa_with_labels(
            stree.taxon_namespace.labels())
    outfilepath=fulltreepath.rsplit('.',1)[0]+'_induced.'+fulltreepath.rsplit('.',1)[1]
    ftree.write(
            path=outfilepath,
            schema='newick')
def induced_subtrees(mdir,r,numgenes):
    for g in range(1,numgenes+1):
        print g
        for t in [10,20,30,40]:
            for w in [1,5,10,25,50]:
                get_induced_tree(
                    mdir+'/R'+r+'/'+str(g)+'/wqmc_sampled_36_bin_t_'+str(t)+'_w_'+str(w)+'_relabeled.tree',
                    mdir+'/R'+r+'/'+str(g)+'/raxmlboot.gtrgamma/RAxML_bipartitions.final_relabeled.f200_sampled_36')
if __name__ == "__main__":
    modeldir=sys.argv[1]
    replicate=sys.argv[2]
    numgenes=int(sys.argv[3])
    induced_subtrees(modeldir, replicate, numgenes)    
    

__author__ = 'ashu'
import sys
import dendropy
increment=5
total_taxa=48
def decode_bipartitions(bp,tlist):
    tset0 =set()
    tset1 =set()
    size=len(bp)
    for idx,c in enumerate(bp):
        if(c=='0'):
            tset0.add(tlist[size-1-idx])
        else:
            tset1.add(tlist[size-1-idx])
    return (tset0,tset1)

def get_bipartitions(tree):
    tree.encode_bipartitions()
    bp=[]
    for n in tree.preorder_node_iter():
        if (n.is_internal() and (n.parent_node!=None) and n.label!=None):
           bp.append(decode_bipartitions(str(n.edge.bipartition),tree.taxon_namespace.labels())+(n.label,))
    return (bp,set(tree.taxon_namespace.labels()))
def bp_conflict(rbp,obp,t):
    if((int(rbp[2])>t) and (int(obp[2])>t)):
        x1,y1,x2,y2=rbp[0],rbp[1],obp[0],obp[1]
        if(len(x1 & x2) ==0 or len(x1 & y2)==0 or len(y1 & x2)==0 or len(y1 & y2)==0):
            return False
        else:
            return True
    else:
        return False
def conflict(refbps,othbps,t):
    for rbp in refbps[0]:
        for obp in othbps[0]:
            if(bp_conflict(rbp,obp,t)):
                return True
    return False
def update_bin(mdir,r,refbps,bin_taxa,in_bin,out_bin,t):
    for g in out_bin.copy():
        print "Gene",g
        othbps=get_bipartitions(dendropy.Tree.get(
            path=mdir+'/R'+r+'/'+str(g)+'/raxmlboot.gtrgamma/RAxML_bipartitions.final_relabeled.f200_sampled_36',
            schema='newick'))
        if(not conflict(refbps,othbps,t)):
            in_bin.add(g)
            out_bin.remove(g)
            bin_taxa=bin_taxa | othbps[1]

def get_bin(mdir,r,gene,numgenes,t):
    in_bin=set()
    in_bin.add(gene)
    out_bin=set(range(1,numgenes+1))
    out_bin.remove(gene)
    reftree=dendropy.Tree.get(
        path=mdir+'/R'+r+'/'+str(gene)+'/raxmlboot.gtrgamma/RAxML_bipartitions.final_relabeled.f200_sampled_36',
        schema='newick')
    refbps=get_bipartitions(reftree)
    bin_taxa=refbps[1].copy()
    t-=increment
    while(len(bin_taxa)!=48):
        t+=increment
        update_bin(mdir,r,refbps,bin_taxa,in_bin,out_bin,t)
    print t,in_bin
if __name__ == "__main__":
    modeldir=sys.argv[1]
    replicate=sys.argv[2]
    gene=int(sys.argv[3])
    numgenes=int(sys.argv[4])
    threshold = int(sys.argv[5])
    get_bin(modeldir,replicate,gene,numgenes,threshold)   
    

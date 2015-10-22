__author__ = 'ashu'
import sys
import dendropy
from numpy import mean
def get_bipartition_dict(tree):
    bdict={}
    for n in tree.preorder_node_iter():
        if (n.is_internal() and (n.parent_node!=None)):
            bipartition=str(n.edge.bipartition)
            if bipartition not in bdict:
                if n.label!=None:
                    bdict[bipartition]=float(n.label)
                else:
                    bdict[bipartition]=None
            else:
                print 'Dublicate',bipartition
    return bdict
def avg_bootstrap_retained(rtpath,otpath):
    tns=dendropy.TaxonNamespace()
    rtree=dendropy.Tree.get(
        path=rtpath,
        schema='newick',
        taxon_namespace=tns)
    rtree.encode_bipartitions()
    otree=dendropy.Tree.get(
        path=otpath,
        schema='newick',
        taxon_namespace=tns)
    otree.encode_bipartitions()
    rbdict=get_bipartition_dict(rtree)
    obdict=get_bipartition_dict(otree)
    l=[]
    for b in obdict.keys():
        if((b in rbdict) and rbdict[b]!=None):
            l.append(rbdict[b])
    return mean(l)
if __name__ == "__main__":
    reftreepath=sys.argv[1]
    othertreepath=sys.argv[2]
    print avg_bootstrap_retained(reftreepath,othertreepath)    
    

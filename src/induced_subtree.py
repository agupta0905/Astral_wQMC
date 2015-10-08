__author__ = 'ashu'
import sys
import dendropy
def induced_subtree(fulltreefilepath, subtreefilepath, outtreefilepath):
    fulltree = dendropy.Tree.get(
        path=fulltreefilepath,
        schema='newick')
    subtree = dendropy.Tree.get(
        path=subtreefilepath,
        schema='newick')
    fulltree.retain_taxa_with_labels(subtree.taxon_namespace.labels())
    f = open(outtreefilepath,'w')
    f.write(fulltree.as_string('newick'))
    f.close()
if __name__ == "__main__":
    fulltreefilepath=sys.argv[1]
    subtreefilepath=sys.argv[2]
    outtreefilepath=sys.argv[3]
    induced_subtree(fulltreefilepath,subtreefilepath, outtreefilepath)
    
    

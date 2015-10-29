import subprocess
from numpy import mean,median,std
from avg_bootstrap_retained import avg_bootstrap_retained
cmd='/home/agupta80/phylogenetics/comparetrees/compareTrees.missingBranch'
numgenes=100
rlist=map(lambda x: [], range(numgenes))

def print_resultes(rlist):
    totalval=3*5
    for i in range(totalval):
        l=[],counts=[]
        for g in range(numgenes):
            l.append(rlist[g][i][0])
            counts.append(rlist[g][i][1])
        print str(mean(l))+','+str(mean(counts))

for g in range(1,numgenes+1):
    print g,'Done'
    for m in [0.5,1,2]:
        t1='/home/agupta80/scratch/avian_dataset/avian-'+str(m)+'X-1000-500/R1/'+str(g)+'/raxmlboot.gtrgamma/RAxML_bipartitions.final_relabeled.f200_sampled_36'
        for w in [1, 5, 10, 25, 50]:
            t2='/home/agupta80/scratch/avian_dataset/avian-'+str(m)+'X-1000-500/R1/'+str(g)+'/wqmc_sampled_36_numgenes_100_w_'+str(w)+'_relabeled_induced.tree'
            rlist[g-1].append(avg_bootstrap_retained(t1, t2))
print_resultes(rlist)
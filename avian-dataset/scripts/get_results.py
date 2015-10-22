import subprocess
from numpy import mean,median,std
cmd='/home/agupta80/phylogenetics/comparetrees/compareTrees.missingBranch'
numgenes=100
rlist=map(lambda x: [], range(numgenes))

def print_resultes(rlist):
    totalval=3*5
    for i in range(totalval):
        l=[]
        for g in range(numgenes):
            l.append(rlist[g][i])
        print str(mean(l))+','+str(median(l))+','+str(std(l))

for g in range(1,numgenes+1):
    print g,'Done'
    for m in [0.5,1,2]:
        t1='/home/agupta80/scratch/avian_dataset/avian-'+str(m)+'X-1000-500-true/R1/'+str(g)+'/true_relabeled.gt'
        for w in [5, 10, 25, 50]:
            t2='/home/agupta80/scratch/avian_dataset/avian-'+str(m)+'X-1000-500/R1/'+str(g)+'/wqmc_sampled_36_numgenes_100_w_'+str(w)+'_relabeled.tree'
            p= subprocess.Popen([cmd, t1, t2], stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
            out, err = p.communicate()
            rlist[g-1].append(float(out.split(' ')[2].replace('\n','')))
        t2='/home/agupta80/scratch/avian_dataset/avian-'+str(m)+'X-1000-500/R1/wqmc_sampled_36_numgenes_100.tree'
        p= subprocess.Popen([cmd, t1, t2], stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
        out, err = p.communicate()
        rlist[g-1].append(float(out.split(' ')[2].replace('\n','')))
print_resultes(rlist)
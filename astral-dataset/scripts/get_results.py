import subprocess
cmd='/home/agupta80/phylogenetics/comparetrees/compareTrees.missingBranch'
tree1 = '/home/agupta80/scratch/model.100.2000000.0.000001/01/truegenetree_induced_'
tree2 = '/home/agupta80/scratch/tmp/gene_'
for g in range(1,11):
    oline=str(g)+','
    t1=tree1+str(g-1).zfill(3)
    for w in [2, 10, 100]:
        for sample in ['','_10psample']:
            t2=tree2+str(g)+'_w_'+str(w)+sample+'_wqmc.tree'
            p= subprocess.Popen([cmd, t1, t2], stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
            out, err = p.communicate()
            oline=oline+out.split(' ')[2].remove('\n')+','
            #gene,w2,w2sam,w10,w10sam,w100,w100sam,wqmc_on_full
            #print out," output"
            #print "Gene",g, "Weight",w, 'sample',sample,out.split(' ')[2]
    p= subprocess.Popen([cmd, t1, '/home/agupta80/scratch/tmp/all_quartets.tree'], stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
    out, err = p.communicate()
    oline=oline+out.split(' ')[2].remove('\n')+','
    
    p= subprocess.Popen([cmd, t1, '/home/agupta80/scratch/tmp/all_quartets_10psample.tree'], stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE)
    out, err = p.communicate()
    oline=oline+out.split(' ')[2].remove('\n')
    print oline
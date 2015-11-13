__author__ = 'ashu'
import sys
import os.path
def write_bin(glist,filepath):
    f=open(filepath,'w')
    for i in glist:
        f.write(str(i)+'\n')
    f.close()
def reorganize_bin_def(bindefdir, threshold,numgenes,modeldir, replicate):
    for i in range(0,numgenes):
        if(os.path.isfile(bindefdir+'/bin.'+str(i)+'.txt')):
            f=open(bindefdir+'/bin.'+str(i)+'.txt','r')
            glist=[]
            for line in f:
                glist.append(int(line.replace('\n','')))
            f.close()
            for g in glist:
                write_bin(glist,modeldir+'/R'+replicate+'/'+str(g)+'/orginal_binning_t_'+threshold+'.txt')
        else:
            break; 
if __name__ == "__main__":
    bindefdir=sys.argv[1]
    threshold=sys.argv[2]
    numgenes=int(sys.argv[3])
    modeldir=sys.argv[4]
    replicate=sys.argv[5]
    reorganize_bin_def(bindefdir, threshold,numgenes,modeldir, replicate)   
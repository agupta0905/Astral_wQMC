__author__ = 'ashu'
import sys
import os
from random import shuffle
def split_file(path,name,prefix, extension):
    f=open(path+'//'+name,'r')
    for linenumber,line in enumerate(f):
        f_out=open(path+'//'+prefix+str(linenumber+1)+extension,'w')
        f_out.write(line)
        f_out.close()
    f.close()
     
if __name__ == "__main__":
    file_dir=sys.argv[1]
    filename=sys.argv[2]
    prefix=sys.argv[3]
    extension=sys.argv[4]
    split_file(file_dir,filename,prefix,extension)
    
    

import os
from contextlib import contextmanager

@contextmanager
def BoldTagFunc():
    print '<b>'
    yield
    print '</b>'
        
with BoldTagFunc() as b:
    print "Hello World"
    
    
@contextmanager
def FileOpenerFunc(Filename,mode):
    fh = open(os.path.join('/home/rohith/Python',Filename),mode)
    yield fh
    fh.close()

with FileOpenerFunc('Test.txt','w+') as fh2:
    for i in range(28):
        fh2.write(str(i) + '\n')

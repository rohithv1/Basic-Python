import os
# A simple Context manager
class BoldTag:
    def __init__(self):
        self
    def __enter__(self):
        print '<b>'
    def __exit__(self,x,y,z):
        print '</b>'

with BoldTag() as b:
    print "Hello World"
    
# Context manager for file operation    
class FileOpener:
    def __init__(self,Filename,mode):
        self.FileName = Filename
        self.Mode = mode
    def __enter__(self):
        self.fh = open(os.path.join('/home/rohith/Python',self.FileName),self.Mode)
        return self
    def __exit__(self,exception_type, exception_value, traceback):
        self.fh.close()
        print exception_value
        return self
    def FileWrite(self,text):
        self.fh.write(text) 
    
with FileOpener('Test.txt','r') as fh1:
    for i in range(25):
        print i
        fh1.FileWrite(str(i) + '\n')

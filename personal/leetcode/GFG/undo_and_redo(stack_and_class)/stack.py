class Solution:
    def __init__(self):
        self.doc = []   
        self.tmp=[]# main document stack
        
    def append(self, x):
        # append x into document
        self.doc.append(x)
        #print(self.doc)

    def undo(self):
        # undo last change
        
        u=self.doc.pop()
        self.tmp.append(u)
        #print(self.doc)

    def redo(self):
        # redo changes
        r=self.tmp.pop()
        self.doc.append(r)
        #print(self.doc)

    def read(self):
        # read the document
        return "".join(self.doc)
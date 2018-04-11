class Loc:
    def __init__(self,filename):
        self.lineCount=0
        self.blankLineCount=0
        self.commentLineCount = 0
        self.importLineCount = 0

        file=open(filename)
        lines=file.read().split('\n')
        comm=False
        for line in lines:
            line=line.strip()
            self.lineCount+=1
            if(line.startswith('import')):
                self.importLineCount+=1
            if(line==""):
                self.blankLineCount+=1
            if(line[:1]=='#' or comm==True):
                self.commentLineCount+=1
            if(line[:3]=='\"\"\"'):
                comm=not comm
                self.commentLineCount+=1
                if(len(line)>3 and line[-3:]=='\"\"\"'):
                    comm=not comm


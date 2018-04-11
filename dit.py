import ast

class DITFinder(ast.NodeVisitor):
    def __init__(self):
        self.upperClass=''

    def visit_ClassDef(self,node):
        if(len(node.bases)==1):
            self.upperClass=node.bases[0].id

class Dit:
    def __init__(self,filename,option):
        self.reportStr=''
        tree = ast.parse(open(filename).read())
        upperClassDict={}
        resultDict={}
        for node in ast.walk(tree):
            if isinstance(node,ast.ClassDef):
                resultDict[node.name]=0
                finder=DITFinder()
                finder.visit(node)
                if(option):
                    if(finder.upperClass!=''):
                        upperClassDict[node.name] = finder.upperClass
                else:
                    if (finder.upperClass != '' and finder.upperClass!='object'):
                        upperClassDict[node.name]=finder.upperClass
        for key,value in upperClassDict.items():
            resultDict[key] += 1
            if value in upperClassDict.keys():
                resultDict[key]+=1
        for key,value in resultDict.items():
            self.reportStr+=str(key)+' has DIT of '+str(value)+'\n'
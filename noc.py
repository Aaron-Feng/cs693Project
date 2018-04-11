import ast

class NOCFinder(ast.NodeVisitor):
    def __init__(self):
        self.upperClass=''

    def visit_ClassDef(self,node):
        if(len(node.bases)==1):
            self.upperClass=node.bases[0].id

class Noc:
    def __init__(self,filename):
        self.reportStr=''
        tree = ast.parse(open(filename).read())
        upperClassDict={}
        resultDict={}
        for node in ast.walk(tree):
            if isinstance(node,ast.ClassDef):
                resultDict[node.name]=0
                finder=NOCFinder()
                finder.visit(node)
                if (finder.upperClass != '' and finder.upperClass!='object'):
                    upperClassDict[node.name]=finder.upperClass
        for key,value in upperClassDict.items():
            resultDict[value] += 1
        for key, value in resultDict.items():
            self.reportStr += str(key) + ' has NOC of ' + str(value) + '\n'
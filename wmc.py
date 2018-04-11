import ast
class Wmc:
    def __init__(self,filename,option):
        self.reportStr=''
        tree = ast.parse(open(filename).read())
        resultDict={}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                count=0
                for methods in node.body:
                    if option:
                        if isinstance(methods,ast.FunctionDef):
                            count+=1
                    else:
                        if isinstance(methods,ast.FunctionDef) and methods.name!='__init__':
                            count+=1
                resultDict[node.name]=count
        for key,value in resultDict.items():
            self.reportStr+=str(key)+' has WMC of '+str(value)+'\n'
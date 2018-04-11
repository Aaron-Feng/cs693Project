import ast
import collections

class CouplingFinder(ast.NodeVisitor):
    def __init__(self):
        self._name=[]
    @property
    def name(self):
        return '.'.join(self._name)
    def visit_Name(self,node):
        if(self._name!=[]):
            self._name.insert(0,node.id)

    def visit_Attribute(self, node):
        self._name.insert(0,node.attr)
        self.generic_visit(node)

class Cbo:
    def __init__(self,filename):
        self.resultStr=''
        tree = ast.parse(open(filename).read())
        for node in ast.walk(tree):
            if isinstance(node,ast.ClassDef):
                resultList = []
                keyDict={}
                couplingClass=[]
                for functions in node.body:
                    if isinstance(functions,ast.FunctionDef):
                        for statements in functions.body:
                            finder=CouplingFinder()
                            finder.visit(statements)
                            if (finder.name!=''and functions.name!='__init__'):
                                resultList.append(finder.name)
                            elif(functions.name=='__init__'):
                                tempList=finder.name.split('.')
                                if(len(tempList)==3):
                                    tempList.remove('self')
                                    keyDict[tempList[1]]=tempList[0]
                for attr in resultList:
                    tempList=attr.split('.')
                    if (tempList[0]!='self'):
                        couplingClass.append(tempList[0])
                    if (keyDict != {}):
                        for key,value in keyDict.items():
                            if (key in tempList):
                                couplingClass.append(value)
                result=collections.Counter(couplingClass)
                for i,j in result.items():
                    self.resultStr+=(str(node.name)+' and '+ str(i) +' has CBO:'+str(j)+'\n')
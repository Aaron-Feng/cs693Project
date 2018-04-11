import ast

class AttributeVisitor(ast.NodeVisitor):
    def __init__(self):
        self._name = ''

    @property
    def name(self):
        return (self._name)

    @name.deleter
    def name(self):
        self._name.clear()

    def visit_Attribute(self, node):
        try:
            self._name = node.attr
        except AttributeError:
            pass

class Locm:
    def __init__(self,filename):
        self.result=''
        tree = ast.parse(open(filename).read())
        instanceList=[]
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                attributeList = [node.name]
                for function in node.body:
                    if isinstance(function,ast.FunctionDef) and function.name!='__init__':
                        functionName=set()
                        functionName.add(function.name)
                        for attr in function.body:
                            visitor = AttributeVisitor()
                            visitor.visit(attr)
                            if (visitor.name!=''):
                                functionName.add(visitor.name)
                        attributeList.append(functionName)
                instanceList.append(attributeList)

        for n in instanceList:
            count=len(n)
            if(count>1):
                count-=1
                for i in range(1,len(n)):
                    set1=n[i]
                    for j in range(i+1,len(n)):
                        set2=n[j]
                        if (set1 & set2 !=set()):
                           count-=1
            self.result+=(n[0] + '      LOCM:'+str(count)+'\n')

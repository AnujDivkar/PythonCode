#python cs2.py "C:\Users\PC-server\Documents\PythonCode\testClasses"
import sys
import os
import ast  
import inspect

def importClasses(path,fileList):
    sys.path.append(path)    
    for i in fileList:
        filePath= path +"\\"+i;
        if(os.path.isfile(filePath)):
            fileName = i
            name, ext = os.path.splitext(fileName)
            module = __import__(name)
            globals()[name] = module
            
def printSubClassResult(className):
    subclasses = eval(className).__subclasses__()
    for cls in subclasses:
        classFileName = os.path.basename(inspect.getmodule(cls).__file__)
        print("\t",cls.__name__, "[", classFileName, "]")    

def printClassResult(path,fileList):
    for i in fileList:
            filePath= path +"\\"+i;
            if(os.path.isfile(filePath)):
                fileName = i
                name, ext = os.path.splitext(fileName)
                file = open(filePath, "r")
                code = file.read()
                tree = ast.parse(code)
                classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
                for classObj in classes:
                    print(classObj.name, "[", fileName, "]")
                    className = name + "."+ classObj.name
                    printSubClassResult(className)
                    print("\n")
                    
def processFiles(path):
    
    try:
        fileList = os.listdir(path)
        
        importClasses(path,fileList)
        
        printClassResult(path,fileList)
        
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
    
def main(argv):
   processFiles(argv)
   
main(sys.argv[1])
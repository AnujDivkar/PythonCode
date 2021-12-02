import sys
import os
import ast  
import inspect
def processFiles(path):
    try:
        sys.path.append(path)    
        fileList = os.listdir(path)
        for i in fileList:
            filePath= path +"\\"+i;
            if(os.path.isfile(filePath)):
                fileName = i
                name, ext = os.path.splitext(fileName)
                module = __import__(name)
                globals()[name] = module
        
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
                    className = name +"."+classObj.name
                    subclasses = eval(className).__subclasses__()
                    for cls in subclasses:
                        print("\t",cls.__name__, "[", os.path.basename(inspect.getmodule(cls).__file__), "]")
                    print("\n")

    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
    
def main(argv):
   processFiles(argv)
   
main(sys.argv[1])
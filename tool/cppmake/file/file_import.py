import importlib

def import_file(file): ...



def import_file(file):
    try:
        return importlib.machinery.SourceFileLoader(
            fullname=file.removesuffix(".py").replace('/', '.'), 
            path=file
        ).load_module()            
    except:
        return None

import sys
import os
#Inspector not implemented yet
class Importer():
    def __init__(self):
        pass
    
    def _addPath(self, path = str()):
        try:
            if not sys.path.count(path):
                sys.path.append(os.path.dirname(path)) #if path exist then but for now it works
            else:
                print path + "already exist on sys.path"
                pass
        except:
            raise
        
    def _check(self, obj_name = str()):
        #this is name sensitive, so do not use same names for different objects loaded!

        try:
            
            obj = getattr(self, obj_name)
            return obj
        
        except AttributeError:
            print "AttributeError"# or use traceback
            
        return None

    def _fromLoad(self, obj = str(), module_path = str()):
        try:
            
            module = os.path.basename(module_path)[:-3]
            
            self._addPath(module_path)
            
            exec("from " + module + " import " + obj)
            exec("self." + obj + " = " + obj)
            exec("o = self." + obj)

            return o

        except:
            raise

    def _load(self, module_path = str()):
        try:
            
            module = os.path.basename(module_path)[:-3]
            
            self._addPath(module_path)
            
            exec("import " + module)
            exec("self." + module + " = " + module)
            exec("m = self." + module)

            return m

        except:
            print "[e] Maybe " + module_path + " does not exist"

    def _fromGet(self, obj = str(), module_path = str()):
        pass

    def _get(self, module_path = str()):
        module = os.path.basename(module_path)[:-3]
        obj = self._check(module)

        if not obj:
            obj = self._load(module_path)
        else:
            return obj
            
        return obj
    
    def _reload(self, obj):
        pass#exec("self." + "obj" + " = " + #obj_name)

    def _update(self, module_path = str()):
        pass

    def _fromUpdate(self, module_path = str(), obj = str()):
        pass

if __name__ == "__main__":
    pass

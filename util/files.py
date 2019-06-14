import glob
import os
import sys
import pyclbr


class Files:
    modules = {}

    def __init__(self, path):
        root_path = os.path.dirname(sys.modules["__main__"].__file__)
        self.files = [f for f in glob.glob(root_path + "/" + path + "/**/*.py", recursive=True) if
                      not f.endswith("__init__.py")]
        for f in self.files:
            module = f.replace(root_path, "")[1:].replace("/", ".").replace(".py", "")
            self.modules[module] = list(pyclbr.readmodule(module).keys())

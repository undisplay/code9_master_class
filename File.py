
import io
import os

class FileManager :

    path = ""
    file = None

    def __init__(self,path):
        self.path = path
        self.file = io.open(path,'w')

    def delete(self):
        os.remove(self.path)

    def erase(self):
        self.file.truncate()

    def read(self):
        return self.file.read()

    def add(self,str):
        self.file.write(str)


f = FileManager("./test.txt")

f.delete()
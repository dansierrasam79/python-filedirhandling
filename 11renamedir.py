#rename a directory 
class RenameSingleDirectory: 
    def __init__(self, dpath, dName1, dName2): 
        self.directorypath = dpath 
        self.directoryName1 = dName1 
        self.directoryName2 = dName2 
    def renameOneDirectory(self): 
        file1Command = self.directorypath + self.directoryName1
        file2Command = self.directorypath + self.directoryName2
        os.rename(file1Command,file2Command) 
        print("Directory has been renamed") 
# Driver code 
if __name__ == "__main__": 
    import os 
    filepath = input("Please enter the directory path: ") 
    fileName = input("Please enter the current directory name: ")
    fileName2 = input("Please enter the new directory name: ")
    outputObject = RenameSingleDirectory(filepath,fileName, fileName2)
    outputObject.renameOneDirectory()

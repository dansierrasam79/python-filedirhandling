# rename a file 
class RenameSingleFile: 
    def __init__(self, fpath, fName1, fName2): 
        self.filepath = fpath 
        self.fileName1 = fName1 
        self.fileName2 = fName2 
    def renameOneFile(self): 
        file1Command = self.filepath + self.fileName1 
        file2Command = self.filepath + self.fileName2 
        os.rename(file1Command,file2Command)
        print("File has been renamed")
# Driver code
if __name__ == "__main__": 
    import os 
    filepath = input("Please enter the filepath: ") 
    fileName1 = input("Please enter the current file name with extension: ")
    fileName2 = input("Please enter the new file name with extension: ")
    outputObject = RenameSingleFile(filepath,fileName1, fileName2)
    outputObject.renameOneFile()

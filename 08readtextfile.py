# Read a text file 
class readSingleFile: 
    def __init__(self, fpath): 
        self.filepath = fpath 
    def readFile(self): 
        fName = open(self.filepath, "r") 
        fullText = fName.read() 
        print(fullText) 
# Driver code 
if __name__ == "__main__": 
    filepath = input("Enter the directory where the file is located: ") 
    filename = input("Enter the file name to be read: ") 
    finalfilepath = filepath + filename 
    outputObject = readSingleFile(finalfilepath)
    outputObject.readFile()

# find a file and directory in a given path 
class findFileInGivenDirectory: 
    def __init__(self, fName, dName): 
        self.fileName = fName 
        self.directoryName = dName 
    def findFile(self): 
        if self.fileName in os.listdir(self.directoryName): 
            print(self.fileName, "is located in the directory") 
        else: 
            print(self.fileName, "is NOT located in the directory") 
# Driver code 
if __name__ == "__main__":
    import os 
    directorypath = input("Enter a directory path: ") 
    filename = input("Enter a file with extension or directory name: ")
    outputObject = findFileInGivenDirectory(filename,directorypath)
    outputObject.findFile() 

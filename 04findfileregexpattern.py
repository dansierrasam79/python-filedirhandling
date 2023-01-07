# find files matching Regex pattern 
class findFileswithPattern: 
    def __init__(self, fname, fpath): 
        self.filename = fname 
        self.filepath = fpath 
    def findFilePatternMatching(self): 
        result = [] 
        for root, dirs, files in os.walk(self.filepath): 
            for name in dirs + files: 
                if fnmatch.fnmatch(name,self.filename): 
                    result.append(os.path.join(root, name)) 
        return result 
#Driver code 
if __name__ == "__main__": 
    import os, fnmatch 
    filepath = input("enter the file path: ") 
    filename = input("Enter the file name with specific Regex pattern characters: ")
    outputObject = findFileswithPattern(filename, filepath) 
    finalList = outputObject.findFilePatternMatching() 
    for path in finalList: 
        print(path) 

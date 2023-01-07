# Move several files 
class MoveManyFiles: 
    def __init__(self, sourceDir, destDir, fName): 
        self.sourceDir = sourceDir
        self.destDir = destDir
        self.fName = fName
    def MoveSeveralFiles(self): 
        shutil.move(os.path.join(self.sourceDir,self.fName), self.destDir) 
if __name__ == "__main__": 
    import os, shutil
    sourceFolder = input("Enter the absolute path of the source folder: ")
    destinationFolder = input("Enter the absolute path of the destination folder: ")
    fileNames = ["MissionMessage.odt"] 
    for file in fileNames: 
        outputObject = MoveManyFiles(sourceFolder,destinationFolder,file)
        outputObject.MoveSeveralFiles()
    for file in fileNames:
        if file in os.listdir(destinationFolder): 
            print("Success. ", file, "has been moved.")

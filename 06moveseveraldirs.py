# Move several directories 
class MoveManyDirectories: 
    def __init__(self, sourceDir, destDir, fName): 
        self.sourceDir = sourceDir
        self.destDir = destDir
        self.fName = fName
    def MoveSeveralDirectories(self): 
        shutil.move(os.path.join(self.sourceDir,self.fName), self.destDir) 
if __name__ == "__main__": 
    import os, shutil
    sourceFolder = input("Enter the absolute path of the source folder: ")
    destinationFolder = input("Enter the absolute path of the destination folder: ")
    folderNames = ["test", "test2"] 
    for folder in folderNames: 
        outputObject = MoveManyDirectories(sourceFolder,destinationFolder,folder)
        outputObject.MoveSeveralDirectories()
    for folder in folderNames:
        if folder in os.listdir(destinationFolder): 
            print("Success. ", folder, "has been moved.") 

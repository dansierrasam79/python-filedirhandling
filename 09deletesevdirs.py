# Remove several directories 
class DeleteManyDirectories: 
    def __init__(self, dpath, dName): 
        self.directorypath = dpath 
        self.directoryName = dName 
    def deleteSeveralDirectories(self): 
        deleteCommand = self.directorypath + self.directoryName
        os.rmdir(deleteCommand) 
# Driver code 
if __name__ == "__main__": 
    import os 
    directorypath = input("Please enter the directory path: ")
    directorynames = ["test", "test2"] 
    for directoryname in directorynames: 
        outputObject = DeleteManyDirectories(directorypath,directoryname)
        outputObject.deleteSeveralDirectories() 
    for directoryName in directorynames: 
        if directoryName not in os.listdir(directorypath): 
            print("Success.", directoryName, " has been deleted") 
        else: 
            print("Failure.", directoryName, " has NOT been deleted") 

# delete many files in said folder 
class DeleteManyFiles: 
    def __init__(self, fpath): 
        self.finalfilepath = fpath 
    def deleteSeveralFiles(self): 
        os.remove(self.finalfilepath) 
if __name__ == "__main__": 
    import os 
    filepath = input("Enter the folder where files are located: ")
    deleteFiles = ["daniel.txt"] 
    userInput = input("Do you want to delete the files (Y/N)?: ")
    for fileName in deleteFiles: 
        removeFilepath = filepath + fileName 
        outputObject = DeleteManyFiles(removeFilepath)
        outputObject.deleteSeveralFiles() 
    for fileName in deleteFiles: 
        if fileName not in os.listdir(filepath): 
            print("Success.", fileName, "is Deleted.") 
        else: 
            print("Error.", fileName, "is NOT Deleted.") 

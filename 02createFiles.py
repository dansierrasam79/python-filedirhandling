#Create many files 
class createManyFiles: 
    def __init__(self, fpath): 
        self.filepath = fpath 
    def createSeveralFiles(self): 
        newEmptyFile = open(self.filepath, "w") 
        newEmptyFile.close() 
if __name__ == "__main__": 
    import os 
    filesList = ["test1.txt", "test1.xlsx", "test1.docx","test1.py"] 
    # directorypath = /home/danielchakraborty/Desktop/
    directorypath = input("Please enter the directory path in which you want to create the files: ")
    for fileName in filesList: 
        filepath = directorypath + fileName 
        outputObject = createManyFiles(filepath) 
        outputObject.createSeveralFiles() 
    for fileName in filesList: 
        if fileName in os.listdir(directorypath): 
            print("Success. File Created.") 
        else: 
            print("Error. File NOT Created.") 

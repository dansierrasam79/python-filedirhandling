# Create directories 
class createManyDirectories: 
    def __init__(self,dpath): 
        self.directorypath = dpath 
    def createSeveralDirectories(self): 
        os.mkdir(self.directorypath) 
if __name__ == "__main__": 
    import os 
    directorynames = ["test1", "test2", "test3", "test4"]
    # directorypath = /home/danielchakraborty/Desktop/
    directorypath = input("Please enter directory path to create new directory: ")
    for directoryname in directorynames: 
        finaldirectorypath = directorypath + directoryname 
        outputObject = createManyDirectories(finaldirectorypath) 
        outputObject.createSeveralDirectories() 
    for directoryname in directorynames:
        if directoryname in os.listdir(directorypath): 
            print("File created in directory") 
        else: 
            print("File not created in directory") 

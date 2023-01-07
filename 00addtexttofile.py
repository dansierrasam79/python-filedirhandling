# Add text to file 
class AddTextToFile: 
    def __init__(self,fpath): 
        self.finalfilepath = fpath 
    def AddTextFile(self): 
        textFile = open(self.finalfilepath, "a")
        textFile.write("Hello world") 
        textFile.write("\n") 
        textFile.write("Hello world again!") 
        textFile.close() 
# Driver code 
if __name__ == "__main__":
    # filepath: /home/danielchakraborty/Desktop/
    filepath = input("Enter the file path to open the file: ") 
    # filename: daniel.txt
    filename = input("Enter the file name: ") 
    finalfilepath = filepath + filename 
    outputObject = AddTextToFile(finalfilepath) 
    outputObject.AddTextFile() 

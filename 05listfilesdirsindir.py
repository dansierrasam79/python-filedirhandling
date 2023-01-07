# List all files and directories in a directory 
class ListFilesDirectories: 
    def __init__(self, dpath): 
        self.directorypath = dpath 
    def ListAllFilesDirectories(self): 
        import os 
        directories = [] 
        files = [] 
        for item in os.listdir(self.directorypath): 
            if "." in item: 
                files.append(item)
            else: 
                directories.append(item) 
        print("Files:") 
        if len(files) == 0: 
            print("No Files") 
        else: 
            for items in files: 
                print(items) 
        print()
        print("Directories:") 
        if len(directories) == 0: 
            print("No directories") 
        else: 
            for items in directories: 
                print(items)
if __name__ == "__main__": 
    directorypath = input("Enter the directory to generate list of contents: ")
    outputObject = ListFilesDirectories(directorypath) 
    outputObject.ListAllFilesDirectories()

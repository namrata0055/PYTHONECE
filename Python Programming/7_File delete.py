import os

class FileRead:
    def main():
        p=input("Enter file to be deleted: ")
        a=os.remove(p)
        print("File Deleted Successfully")
FileRead.main()
class FileRead:
    def main():
        a=open((str(input("Enter file name: "))),"w")
        a.write(str(input("Enter the content of file: ")))
        print("Done")
        a.close()
FileRead.main()
        
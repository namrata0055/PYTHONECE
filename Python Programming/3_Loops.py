class Numbers:
    def even():
        a=int(input("Enter start:"))
        b=int(input("Enter end: "))
        for x in range(a,b+1):
            if x%2==0:
                print(x, end=" ")

    def odd():
        x=int(input("Enter start: "))
        y=int(input("Enter end: "))
        for z in range(x,y+1):
            if z%2!=0:
                print(z, end=" ")

    print("\t\t.....EVEN.....")   
Numbers.even()
print("\n")
print("\t\t.....ODD.....")
Numbers.odd()
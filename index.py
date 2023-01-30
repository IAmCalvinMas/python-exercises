x = int(input("Number: "))

def isToZero(num):
    match num:
        case x is 0:
            print("greater")
        case x == 0:
            print("Equal")
        case x < 0:
            print("less")

isToZero(x)

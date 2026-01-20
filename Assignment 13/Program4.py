# 4. Write a program which accepts one number and prints binary equivalent

def binary(No):

    lst = []
    
    while No > 0 :
        lst.append(No%2)
        No = No//2

    return lst

def main():
    No = int(input("Enter the Number :"))
    
    res = binary(No)
    print("Binary equivalant of ",No," is :", *res[::-1], sep="")

if __name__ == "__main__":
    main()
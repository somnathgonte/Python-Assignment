# 5.Write a program which accepts one number and prints all odd numbers till that number

def OddNumber(No):
    lst = []
    for i in range(1,No+1):
        if i%2 != 0 :
            lst.append(i)
        
    return lst

def main():
    No = int(input("Enter Number :"))
    res = OddNumber(No)

    print("Even Number upto",No,"is :" ,res )

if __name__ == "__main__":
    main()
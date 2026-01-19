# 2. Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12

def factor(No):
    
    lst = []
    for i in range(1, No+1):
        if No%i==0 :
            lst.append(i)

    return lst

def main():
    No = int(input("Enter Number :"))
    res = factor(No)

    print("Factor of",No, "is", res)

if __name__ == "__main__":
    main()
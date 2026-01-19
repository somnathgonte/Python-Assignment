# 2. Write a program which contains one function ChkGreater() 
# that accepts two numbers and prints the greater number.
# Input : 10 20
# Output : 20 is greater

def ChkGreter(No1, No2):
    if No1>No2 :
        return No1
    else :
        return No2
    
    # return No1 if No1 > No2 else No2

def main():
    res = ChkGreter(100,20)
    print(res, "is greater")

if __name__ == "__main__":
    main()
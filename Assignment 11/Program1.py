# 1. Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def PrimeNumber(No):
    i = 0
    if No<=1  :
        return "Not Prime Number"
    
    if No==2 :
        return "Prime Number"
    
    for i in range(2,No+1):
        if No%i == 0 :
            break

    if i==No :
        return "Prime Number"
    else :
        return "Not Prime Number"

def main():
    No = int(input("Enter Number :"))
    res = PrimeNumber(No)

    print(No,"is",res )

if __name__ == "__main__":
    main()
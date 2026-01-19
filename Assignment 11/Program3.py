# 3. Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def SumOfDigit(No):
   
    sum = 0

    #while No > 0:
    #    sum = sum + (No%10) 
    #    No = No//10

    #return sum

    for i in range(len(str(No))):
        sum = sum+(No%10)
        No = No//10
    
    return sum

def main():
    No = int(input("Enter Number :"))
    res = SumOfDigit(No)
    print("Total sum of",No,"digit is",res)

   

if __name__ == "__main__":
    main()


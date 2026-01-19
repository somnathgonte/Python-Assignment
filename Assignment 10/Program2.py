# 2. Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15

def SumOfNumber(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + i
    
    return sum

def main():
    No = int(input("Enter Number :"))
    res = SumOfNumber(No)

    print("Sum of 1 to",No,"is :",res )

if __name__ == "__main__":
    main()
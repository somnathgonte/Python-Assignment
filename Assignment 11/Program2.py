# 2.Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def DigitCount(No):
    count = 0

    while No > 0:
        No = No//10
        count = count+1

    return count

def main():
    No = int(input("Enter Number :"))
    res = DigitCount(No)
    print("Total digit in",No,"is",res)

   

if __name__ == "__main__":
    main()


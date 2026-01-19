# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def ReverseNumber(No):
   
    rev = 0

    #while No > 0:
    #    rev = rev*10 + (No%10) 
    #    No = No//10

    for i in range(1, 100):   # fixed range, break manually
        if No == 0:
            break
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10

    return rev

def main():
    No = int(input("Enter Number :"))
    res = ReverseNumber(No)
    print("Reverse of",No,"is",res)

if __name__ == "__main__":
    main()


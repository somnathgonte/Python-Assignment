# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5

def DivideBy(No):
    if No%3 == 0 and No % 5 == 0 :
        return True
    else :
        return False

def main():
    No = int(input("Enter Number :"))
    res = DivideBy(No)

    if res == True :
        print(No, "is divisible by 3 and 5")
    else :
        print(No, "is not divisible 3 and 5")

if __name__ == "__main__":
    main()
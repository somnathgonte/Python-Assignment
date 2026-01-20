# 10. Write a lambda function which accepts three numbers and returns largest number.

def main():

    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))
    No3 = int(input("Enter Third Number :"))

    max = lambda No1, No2, No3 : No1 if (No1 > No2 and No1 > No3) else No2 if (No2 > No3) else No3

    
    print("Max Number is :",max(No1, No2, No3))

if __name__ == "__main__":
    main()
 
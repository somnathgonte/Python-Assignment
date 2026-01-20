# 8. Write a lambda function which accepts two numbers and returns addition.

def main():

    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    add = lambda No1, No2 : No1 + No2
    
    print("Addition is :",add(No1, No2))

if __name__ == "__main__":
    main()
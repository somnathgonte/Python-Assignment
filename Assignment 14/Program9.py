# 9. Write a lambda function which accepts two numbers and returns multiplication.

def main():

    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    multi = lambda No1, No2 : No1 * No2
    
    print("Multiplication is :",multi(No1, No2))

if __name__ == "__main__":
    main()
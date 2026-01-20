# 1. Write a lambda function which accepts one number and returns square of that number.

def main():

    No = int(input("Enter Number :"))
    square = lambda No : No*No

    print("Square of ",No," is :",square(No))

if __name__ == "__main__":
    main()
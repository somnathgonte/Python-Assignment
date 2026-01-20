# 2. Write a lambda function which accepts one number and returns cube of that number.

def main():

    No = int(input("Enter Number :"))
    cube = lambda No : No**3

    print("Cube of ",No," is :",cube(No))

if __name__ == "__main__":
    main()
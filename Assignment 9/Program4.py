# 4. Write a program which accepts one number and prints cube of that number.
# Input: 5
# Output: 625

def Cube(No):
    return No**3

def main():
    No = int(input("Enter Number :"))
    res = Cube(No)
    print("Cube of",No,"is :", res)

if __name__ == "__main__":
    main()
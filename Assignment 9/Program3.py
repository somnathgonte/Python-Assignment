# 3. Write a program which accepts one number and prints square of that number.
# Input: 5
# Output: 25

def SqrNumber(No):
    return No**2

def main():
    res = SqrNumber(5)
    print("Square of",5,"is :", res)

if __name__ == "__main__":
    main()
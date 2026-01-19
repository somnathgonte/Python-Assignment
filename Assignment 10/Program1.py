# 1. Write a program which accepts one number and prints multiplication table of that number.
# Input: 4
# Output:4 8 12 16 20 24 28 32 36 40

def multi(No):
    multiplication = 1
    for i in range(1, 11):
        yield No * i

def main():
    No = int(input("Enter Number :"))
    print(list(multi(No)))

if __name__ == "__main__":
    main()
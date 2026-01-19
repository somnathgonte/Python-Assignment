# 3. Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120.

def FactorialOfNumber(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    
    return fact

def main():
    No = int(input("Enter Number :"))
    res = FactorialOfNumber(No)

    print("Factorial of",No,"is :",res )

if __name__ == "__main__":
    main()
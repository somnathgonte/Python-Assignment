# 3. Write a program which accepts two numbers and prints 
# addition, subtraction, multiplication and division.

def addition(No1, No2):
    return No1+No2

def subtraction(No1, No2):
    return No1-No2

def multiplication(No1, No2):
    return No1*No2

def division(No1, No2):
    return No1/No2

def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    add = addition(No1,No2)
    sub = subtraction(No1,No2)
    div = division(No1,No2)
    multi = multiplication(No1,No2)

    print("Addition of", No1,"and", No2 ,"is :", add)
    print("Substraction of", No1,"and", No2 ,"is :", sub)
    print("Division of", No1,"and", No2 ,"is :", div)
    print("Multiplication of", No1,"and", No2 ,"is :", multi)

if __name__ == "__main__":
    main()
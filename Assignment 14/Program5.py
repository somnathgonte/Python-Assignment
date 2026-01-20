# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.

def main():

    No = int(input("Enter Number :"))
    
    chkEven = lambda No :No%2==0 
    
    print(chkEven(No))

if __name__ == "__main__":
    main()
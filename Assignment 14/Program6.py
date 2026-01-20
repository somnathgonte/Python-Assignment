# 5. Write a lambda function which accepts one number and returns True if number is odd otherwise False.

def main():

    No = int(input("Enter Number :"))
    
    chkOdd = lambda No :No%2!=0 
    
    print(chkOdd(No))

if __name__ == "__main__":
    main()
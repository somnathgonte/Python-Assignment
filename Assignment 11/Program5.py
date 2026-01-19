# 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def IsPalindrome(No):
   
    rev = 0
    No1 = No

    #while No > 0:
    #    rev = rev*10 + (No%10) 
    #    No = No//10

    for i in range(1, 100):   # fixed range, break manually
        if No == 0:
            break
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10
    
    if rev == No1:
        return "Palindrome Number"
    else :
        return "Not a Palindrome Number" 

def main():
    No = int(input("Enter Number :"))
    res = IsPalindrome(No)
    print(No,"is",res)

if __name__ == "__main__":
    main()


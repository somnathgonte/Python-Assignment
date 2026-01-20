# 3. Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def isPerfect(No):

    sum = 0

    for i in range(1, No):
        if No%i==0 :
            sum = sum+i

    if No == sum :
        return "Perfect Number"
    else :
        return "Not a Perfect Number"

def main():
    No = int(input("Enter the Number :"))
    
    res = isPerfect(No)

    print(No,"is", res)

if __name__ == "__main__":
    main()
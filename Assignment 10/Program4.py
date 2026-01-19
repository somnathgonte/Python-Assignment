# 4. Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10

def EvenNumber(No):
    lst = []
    for i in range(1,No+1):
        if i%2==0 :
            lst.append(i)
        
    return lst

def main():
    No = int(input("Enter Number :"))
    res = EvenNumber(No)

    print("Even Number upto",No,"is :" ,res )

if __name__ == "__main__":
    main()
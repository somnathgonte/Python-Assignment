# 5. Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 54321

def demo(No):

    lst = []

    for i in range(No, 0, -1):
        lst.append(i)
    
    return lst

def main():
    No = int(input("Enter Number :"))
    
    res = demo(No)

    print(*res, sep=" ")

if __name__ == "__main__":
    main()
# 4. Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 12345

def demo(No):

    lst = []

    for i in range(1,No+1):
        lst.append(i)
    
    return lst


def main():
    No = int(input("Enter Number :"))
    
    res = demo(No)

    print(*res, sep=" ")

if __name__ == "__main__":
    main()
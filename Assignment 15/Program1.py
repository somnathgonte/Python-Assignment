# 1. Write a lambda function using map() 
# which accepts a list of numbers and returns a list of squares of each number.

def main():

    lst = []

    size = int(input("Enter the length of list :"))

    for i in range(size):
        lst.append(int(input("Enter the element : ")))

    square = list(map(lambda no : no**2, lst))
    
    print("Square of given list is :",square)

if __name__ == "__main__":
    main()
 
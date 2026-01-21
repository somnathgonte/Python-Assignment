# 4. Write a lambda function using reduce() 
# which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

def main():

    lst = []

    size = int(input("Enter the length of list :"))

    for i in range(size):
        lst.append(int(input("Enter the element : ")))

    addition = reduce(lambda no1, no2 : no1 + no2, lst)
    
    print("List of Even Number :",addition)

if __name__ == "__main__":
    main()
 
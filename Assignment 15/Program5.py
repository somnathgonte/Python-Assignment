# 5. Write a lambda function using reduce() 
# which accepts a list of numbers and returns the maximum element.

from functools import reduce

def main():

    lst = []

    size = int(input("Enter the length of list :"))

    for i in range(size):
        lst.append(int(input("Enter the element : ")))

    max = reduce(lambda no1, no2 : no1 if no1>no2 else no2, lst)
    
    print("Maximum element :",max)

if __name__ == "__main__":
    main()
 
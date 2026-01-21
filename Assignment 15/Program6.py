# 6. Write a lambda function using reduce() 
# which accepts a list of numbers and returns the minimum element.

from functools import reduce

def main():

    lst = []

    size = int(input("Enter the length of list :"))

    for i in range(size):
        lst.append(int(input("Enter the element : ")))

    min = reduce(lambda no1, no2 : no1 if no1 < no2 else no2, lst)
    
    print("Minumun element :",min)

if __name__ == "__main__":
    main()
 
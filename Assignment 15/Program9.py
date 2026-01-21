# 9. Write a lambda function using reduce() 
# which accepts a list of numbers and returns the product of all elements.

from functools import reduce

def main():

    no = []
    
    size = int(input("Enter the length of list :"))

    for i in range(size):
        no.append(int(input("Enter Name : ")))

    product = reduce(lambda no1, no2 : no1*no2  , no)

    print("Product of all elements :",product)
    
if __name__ == "__main__":
    main()
 
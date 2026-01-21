# 2. Write a lambda function using filter() 
# which accepts a list of numbers and returns a list of even numbers.

def main():

    lst = []

    size = int(input("Enter the length of list :"))

    for i in range(size):
        lst.append(int(input("Enter the element : ")))

    evens = list(filter(lambda no : no%2==0, lst))
    
    print("List of Even Number :", evens)

if __name__ == "__main__":
    main()
 
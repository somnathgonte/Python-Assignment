# 8. Write a lambda function using filter() 
# which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5


def main():

    no = []
    
    size = int(input("Enter the length of list :"))

    for i in range(size):
        no.append(int(input("Enter Name : ")))

    divide = list(filter(lambda no1 : no1%3==0 and no1%5==0  , no))

    print("List of numbers divisible by both 3 and 5 :",divide)
    
if __name__ == "__main__":
    main()
 
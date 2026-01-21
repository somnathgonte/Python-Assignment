# 10.Write a lambda function using filter() 
# which accepts a list of numbers and returns the count of even numbers

def main():

    no = []
    
    size = int(input("Enter the length of list :"))

    for i in range(size):
        no.append(int(input("Enter Name : ")))

    count = list(filter(lambda no1 : no1%2==0 , no))

    print("Count of even numbers :",len(count))
    
if __name__ == "__main__":
    main()
 
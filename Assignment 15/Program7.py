# 7. Write a lambda function using filter() 
# which accepts a list of strings and returns a list of strings having length greater than 5.


def main():

    names = []
    
    size = int(input("Enter the length of list :"))

    for i in range(size):
        names.append(input("Enter Name : "))

    greter = list(filter(lambda no1 : len(no1)>5, names))

    print("List of Strings having length greter than 5 :",greter)
    
if __name__ == "__main__":
    main()
 
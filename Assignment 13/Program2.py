# 2. Write a program which accepts radius of circle and prints area of circle.

def AreaOfCircle(radius):

    return 3.14*radius**2

def main():
    radius = int(input("Enter Radius of Circle :"))
    
    res = AreaOfCircle(radius)

    print("Area of Circle is :", res)

if __name__ == "__main__":
    main()
# 1. Write a program which accepts length and width of rectangle and prints area.

def Area(length, width):

    return length*width

def main():
    lght = int(input("Enter Length of Rectangle :"))
    wdht = int(input("Enter Width of Rectangle :"))
    res = Area(lght, wdht)

    print("Area of Rectangle is :", res)

if __name__ == "__main__":
    main()
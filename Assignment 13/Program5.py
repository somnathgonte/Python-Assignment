#5. Write a program which accepts marks and displays grade.
# Condition Example:
# > 75 Distinction
# ≥ 60 First Class
# ≥ 50 Second Class
# < 50 → Fail


def display(No):

    if No > 75 :
        return "Distinction"
    elif No >= 60 :
        return "First Class"
    elif No >= 50 :
        return "Second Class"
    elif No < 50 :
        return "Fail"

def main():
    No = int(input("Enter Marks :"))
    
    res = display(No)
    print(res)

if __name__ == "__main__":
    main()
# 1. Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

def ChkVowels(ch):
    
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' \
       or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
        return "Vowel"
    else:
        return "Consonant"

def main():
    char = input("Enter English chracter :")
    res = ChkVowels(char)

    print(char, "is", res)

if __name__ == "__main__":
    main()
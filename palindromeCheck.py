import sys

def main():
    quit = True
    while quit == True:
        word = input("Enter Word: ").lower()
        if word == "q":
            sys.exit()
        print(isPalindrome(word))


def isPalindrome(s):
    if len(s) < 2:
        return True
    elif s[0] == s[len(s) - 1]:
        return isPalindrome(s[1:-1])
    else:
        return False;

main()

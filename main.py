

userinput = input("Enter a word which might be a palindrome: ").lower()
palindrome = userinput[::-1]

def check():
    if userinput == palindrome:
        print(userinput +" word is a palindrome!")
    else:
        print(userinput +" isn't a palindrome")

check()

# QUESTION ---PALINDROME CHECKER
while True:
    text = input("Enter the text here to check plaindrome or(press q to stop)").lower()
    if text == 'q':
        print("TATA_BYEBYE_GOODBYE_GAYA")
        break
    if text == text[::-1]:
        print(f"{text} is a palindrome")

    else: 
        print("Its not a palindrom number ")
def palind(s):
    rev = s[::-1]
    if s == rev:  
        print("It is palindrome")
    else:
        print("It is not palindrome")

s = input().strip()  

if s:
    palind(s)
else:
    print("Input is empty. Please enter a valid string.")

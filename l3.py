def count(s):
    alphabets=digits=0
    for char in s:
        if('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            alphabets += 1
        elif '0' <= char <= '9':
            digits += 1
    print("Number of Alphabets=", alphabets)        
    print("Number of Digits=", digits)
string=input("Enter a string")
count(string)

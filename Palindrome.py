s=input("Enter string=")
s1=""
for i in range(len(s)-1,-1,-1):
    s1+=s[i]
if s==s1:
    print("Given string {0} is palindrome".format(s))
else:
    print("Given string {0} is not palindrome".format(s))

    

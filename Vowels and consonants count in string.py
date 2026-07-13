s=input("Enter string==")
v="aeiouAEIOU"
vc,cc=0,0
for i in s:
    if i in v:
        vc+=1
    else:
        cc+=1
print("vowels count in the given string={0}".format(vc))
print("constants count in the given string={0}".format(cc))


s=input("Enter string")
d={}
s1=set(s)
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
duplicate_elements=""
for i in s1:
    if d[i]>1:
        duplicate_elements+=i
print("duplciate elements in given string =={0}".format(duplicate_elements))

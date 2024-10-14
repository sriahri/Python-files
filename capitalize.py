def solve(s):
    l=list(s)
    x=''
    for i in range(len(l)):
        if l[0].isalpha():
            l[0]=l[0].upper()
        if l[i]==' ':
            l[i+1]=l[i+1].upper()
        else:
            pass
    for i in l:
        x+=i
    return x
s=input()
t=solve(s)
print(t)

def decry(t):
    if(len(t)<3):
        return ''.join(reversed(t))
    else:
        t=t[3:-3]
        a=t[-1]
        t=t.replace(a,"",-1)
        t=a+t
        return t

txt=input("enter the encrypted msg:")
m=[]
for i in txt.split():
    r=decry(i)
    m.append(r)
msg=' '.join(m)
print("The decrpted msg is ",msg)
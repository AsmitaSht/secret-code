import random
import string

def encry(txt):
    if(len(txt)<3):
        txt=''.join(reversed(txt))
        return txt
    else:
        a=txt[0]
        t=txt.replace(a,"",1)
        t=t+a
        for i in range(3):
            r_char=random.choice(string.ascii_letters)
            p_char=random.choice(string.ascii_letters)
            t=r_char+t+p_char
        txt=t
        return txt

txt=input("Enter the message:")
m=[]
for i in txt.split():
    r=encry(i)
    m.append(r)
msg=' '.join(m)
print("The encrpted msg is ",msg)




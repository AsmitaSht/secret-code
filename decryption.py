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

'''another'''
# st=input("Enter msg:")
# words=st.split(" ")
# coding=True
# if(coding):
#     n=[]
#     for word in words:
#         if(len(word)>=3):
#             st=word[3:-3]
#             st=st[-1]+st[:-1]
#             n.append(st)

#         else:
#             n.append(word[::-1]) #reverse
# print(" ".join(n))
'''another'''

coding=input("1 for coding \n0 for decoding\n")
st=input("Enter msg:")
words=st.split(" ")
coding=True if coding=="1" else False
if(coding):
    n=[]
    for word in words:
        if(len(word)>=3):
            r1="asd"
            r2="bcd"
            st=r1+word[1:]+word[0]+r2
            n.append(st)

        else:
            n.append(word[::-1]) #reverse
    print(" ".join(n))
else:
    n=[]
    for word in words:
        if(len(word)>=3):
            st=word[3:-3]
            st=st[-1]+st[:-1]
            n.append(st)

        else:
            n.append(word[::-1]) #reverse
    print(" ".join(n))
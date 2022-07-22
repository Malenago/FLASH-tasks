
count=0

for N in range(2000,20000+1):
    N2=bin(N)[2:]

    N2='1'+N2+'1'

    if len(N2)%2==0:
        N2=N2[:len(N2)//2]+'0'+N2[len(N2)//2:]
    else:
        N2=N2[:-1]
        N2=N2[:len(N2)//2]+'1'+N2[len(N2)//2:]

    R=int(N2,2)

    if len(str(R))==6 and N2.count('1')==4:
        count+=1


print(count)
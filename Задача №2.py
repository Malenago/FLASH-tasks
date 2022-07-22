
#решение №1
start='89180*1927*'
start=start.split('*')

for nu1 in range(10):
    for nu2 in range(10):
        N=int(start[0]+str(nu1)+start[1]+str(nu2))

        N2=bin(N)[2:]
        if N%2==0:
            N2+=bin(N2.count('1'))[2:]
        else:
            N2='1'+N2+'00'

        R=int(N2,2)
        if R%41==0 and R%2==0:
            print(N)



#решение №2
for nu1 in range(10):
    for nu2 in range(10):
        N=int('89180'+str(nu1)+'1927'+str(nu2))

        N2=bin(N)[2:]
        if N%2==0:
            N2+=bin(N2.count('1'))[2:]
        else:
            N2='1'+N2+'00'

        R=int(N2,2)
        if R%41==0 and R%2==0:
            print(N)
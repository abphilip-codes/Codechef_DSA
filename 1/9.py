# https://www.codechef.com/LRNDSA01/problems/MULTHREE

for T in range(int(input())):
    k,d0,d1 = map(int,input().split())
    A = (2*(d0+d1))%10 + (4*(d0+d1))%10 + (8*(d0+d1))%10 + (6*(d0+d1))%10
    soln = d0+d1+((d0+d1)%10)+(A*((k-3)//4))
    for i in range(1,((k-3)%4)+1):
        soln = soln + ((2**i)*(d0+d1))%10
    if(soln%3==0): print("YES")
    else: print("NO")
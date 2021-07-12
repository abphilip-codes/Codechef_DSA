# https://www.codechef.com/LRNDSA01/problems/CONFLIP

for T in range(int(input())):
    for G in range(int(input())):
        I,N,Q = map(int,input().split())
        if(N%2==0): head = N/2
        else:
            if(I==1): head = N//2
            if(I==2): head = (N//2)+1
        if(Q==1): print(int(head))
        else: print(int(N-head))
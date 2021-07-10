# https://www.codechef.com/LRNDSA01/problems/CARVANS

for T in range(int(input())):
    ans = 1
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(1,N):
        if(A[i]<=A[i-1]): ans+=1 
        else: A[i]=A[i-1]
    print(ans)
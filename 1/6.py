# https://www.codechef.com/LRNDSA01/problems/FCTRL

for T in range(int(input())):
    ans = 0
    a = int(input())
    while(a>=5):
        a=a//5
        ans=ans+a
    print(ans)
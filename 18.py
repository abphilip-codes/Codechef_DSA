# https://www.codechef.com/LRNDSA01/problems/LAPIN

for T in range(int(input())):
    l = list(input())
    if(sorted(l[0:len(l)//2])==sorted(l[(len(l)+1)//2:len(l)])): print("YES")
    else: print("NO")
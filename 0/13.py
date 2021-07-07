# https://www.codechef.com/CCSTART2/problems/ANGTRICH

a = list(map(int,input().split(" ")))
if(sum(a)==180 and min(a)>0): print("YES")
else: print("NO")
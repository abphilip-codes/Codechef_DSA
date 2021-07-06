# https://www.codechef.com/CCSTART2/problems/TRIVALCH

l = sorted(list(map(int,input().split(" "))))
print((l[2]<=sum(l[:2])) and "YES" or "NO")
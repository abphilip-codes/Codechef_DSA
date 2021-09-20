# https://www.codechef.com/CCSTART2/problems/SUMEVOD

n = int(input())
print(sum(list(range(1,n*2+1,2))),end=" ")
print(sum(list(range(2,n*2+1,2))))
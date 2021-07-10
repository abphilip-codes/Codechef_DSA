# https://www.codechef.com/LRNDSA01/problems/ZCO14003

a = []
m = 0
for T in range(int(input())): a.append(int(input()))
a.sort(reverse=True)
for T in range(len(a)):
    if(m<=(a[T]*(T+1))): m=a[T]*(T+1)
print(m)
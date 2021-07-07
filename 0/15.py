# https://www.codechef.com/CCSTART2/problems/SQALPAT

n = int(input())
l = [x for x in range(1,n*5+1)]
for i in range(0,n):
    if((i+1)%2!=0): print(*l[i*5:(i+1)*5])
    else: print(*l[(i+1)*5-1:i*5-1:-1])

# n = int(input())
# j=1
# for i in range(1,n+1):
#     str1=str2=""
#     if(i%2!=0): 
#         while(j<=i*5):  
#             str1 = str1+str(j)+" "
#             j+=1 
#         print(str1.strip())
#     else:
#         while(j<=i*5):
#             str2 = str(j)+" "+str2
#             j+=1
#         print(str2.strip())
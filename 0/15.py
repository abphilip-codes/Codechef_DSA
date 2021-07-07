# https://www.codechef.com/CCSTART2/problems/SQALPAT

n = int(input())
j=1
for i in range(1,n+1):
    str1=str2=""
    if(i%2!=0): 
        while(j<=i*5):  
            str1 = str1+str(j)+" "
            j+=1 
        print(str1.strip())
    else:
        while(j<=i*5):
            str2 = str(j)+" "+str2
            j+=1
        print(str2.strip())
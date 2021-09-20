# https://www.codechef.com/CCSTART2/problems/DIFACTRS

s,x,y = "",0,int(input())
for z in range(1,y+1):
    if(y%z==0): 
        s+=str(z)+" "
        x+=1
print(x,"\n",s,sep="")
# https://www.codechef.com/CCSTART2/problems/ISBOTH

a = int(input())
if(a%11==0 and a%5==0): print("BOTH")
elif(a%11!=0 and a%5!=0): print("NONE")
else: print("ONE")
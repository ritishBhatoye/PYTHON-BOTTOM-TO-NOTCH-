a=int(input("ENTER A FIVE DIGIT NUMBER "))
sum=0
alt=0
y=0
while a>0:
    sum=sum+a%10
    a=a//10
print("SUM IS ",sum)
n=sum
while n>0:
    if(a%10>alt):
        alt=n%10
        n=n//10
    else:
        n//10
grt=n
print("GREATEST DIGIT IS ",grt)
def fac(x):
    if x==1 or x==0:
        return 1
    else:
        return x*fac(x-1)

print("FACTORIAL OF GREATEST DIGIT IS ",fac(grt))
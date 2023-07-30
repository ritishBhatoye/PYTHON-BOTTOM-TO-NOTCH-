a=int(input())
y=0

while a>0:
    if(a%10>y):
        y=a%10
        a=a//10
    else:
        a=a//10
print(y)
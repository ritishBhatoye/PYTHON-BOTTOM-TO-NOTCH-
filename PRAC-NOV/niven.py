n=int(input("Enter a  number to check whether it is niven ot not "))
sum=0
temp=n
while temp>0:
    sum=sum+temp%10
    temp=temp//10


if(temp%sum==0):
    print("YES,it is NIVEN")
else:
    print("NO,it is not NIVEN")    
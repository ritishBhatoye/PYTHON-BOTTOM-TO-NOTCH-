import string


s=""
for i in (1,16):
    if i%3==0:
        s[i]+="Fizz"
    if i%5==0:
        s[i]+="Buzz"
    if(i%3 and i%5):
        s[i]+="FizzBuzz"
    else:
        s[i]+=i


print(s)
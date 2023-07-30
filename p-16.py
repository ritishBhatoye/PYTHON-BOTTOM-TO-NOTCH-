ritish_n = int(input("Enter the five digit number: "))
ritish_s = 0
ritish_r = 0
ritish_f=1
while ritish_n!=0:
    ritish_r= ritish_n%10
    ritish_s=ritish_s+ritish_r
    ritish_n=int(ritish_n/10)
print("Sum of Digits = ",ritish_s)
ritish_n2 = ritish_s
ritish_gr = ritish_s%10;
while ritish_n2!=0:
    ritish_r2 = ritish_n2%10
    if ritish_gr<ritish_r2:
        ritish_gr=ritish_r2
    ritish_n2 = int(ritish_n2/10)
print("greatest digit = ",ritish_gr)
for i in range(1,ritish_gr+1):
    ritish_f = ritish_f*i
print("Factorial is = ",ritish_f)

import random
n = int(input(" ENTER THE NUMBER OF SLIPS: "))
rn = n*9 
l = [];
counter = 0
j = 0
s = 0
while(counter < rn):
  r = random.randint(1,100)

  l.append(r) 
  counter += 1
print(l)
a = int((rn/3))

while(j < a):
   count =0
   print(" SLIP", s+1) 
   s += 1
   while(count < 3): 
    k = j * 3
    x = slice(k, k + 3) 
    print(l[x])
    count += 1
    j += 1
   print("")

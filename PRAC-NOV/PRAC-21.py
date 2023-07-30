contents = input("Enter the contents for the input file: ")
f1 = open("f1.txt","w")
f1.writelines(contents)
print("Your contents are written to the file : f1.txt")
print("Now we are going to copy in another file f2.txt")
with open('f1.txt', 'r') as f1, open('f2.txt', 'w') as f2:
    
    for line in f1:
        f2.write(line)

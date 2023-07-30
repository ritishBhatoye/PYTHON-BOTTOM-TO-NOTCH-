# f=open("r.txt","w")
# f.write("HI RITISH IS ABOUT TO LEAVE YOU")
# if f:
#     print("File is opened")
#     print(f.read())
# f=open("p.txt","r") 
# #stores all the data of the file into the variable content 
# for i in f:
#     print(i)
#  # prints the type of the data stored in the file 

#   #prints the content of the file 

# #closes the opened file 
# f.close()
fr=open("r.txt","rt")
content=fr.readline()
print(content)
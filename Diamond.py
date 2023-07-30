
n=int(input("Enter the size: "))
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(end=" ")
    for k  in range(1,i+1):
        print(i,end=" ")
    print("\r")
for i in range(1,n+1):
    for j in range(1,i):
        print(end=" ")
    for k in range(0,(n-i)+1):
        print((n+1)-i,end=" ")
    print("\r")

# num=int(input("enter the number of rows"))

# for m in range(1, num+1):
#     for n in range(num, m, -1):
#         # Print the space character.
#         print(end=' ')
#     # Loop from 1 to first loop iterator value using another Nested For loop.
#     for n in range(1, m+1):
#        # Print the first loop iterator value.
#         print(m, end=' ')
#     # Print the Newline character after the end of the inner loop.
#     print()
# for m in range(1, num+1):
#     for n in range(1, m+1):
#         # Print the space character.
#         print(end=' ')
#     # Loop from 1 to first loop iterator value using another Nested For loop.
#     for n in range(num, m, -1):
#        # Print the first loop iterator value.
#         print(m, end=' ')
#     # Print the Newline character after the end of the inner loop.
#     print()    


# # n=int(input("enter the number of rows"))

# # for i in range(n):

# #     for j in range(1,int((n/2))-i+3):

# #         print(sep=" ",end=" ")

# #     for k in range(1,i+2):

# #         print(i, end=" ")

        

# #     print()

# # for i in range(n):

# #     for j in range(1,5-(int((n/2))-i+3)+2):

# #         print(sep=" ",end=" ")

# #     for k in range(1,5-i):

# #         print(k, end=" ")

# #     print()

# # # n=5
# # # for i in range(n-1):
# # #     for j in range(i,n):
# # #         print('',end='')
# # #     for j in range(i):
# # #         print('*',end='')
# # #     for j in range(i+1):
# # #         print('*',end='')
# # #     print()
# # # for j in range(n):
# # #     for j in range(i+1):
# # #         print('',end='')
# # #     for j in range(i,n-1):
# # #         print('*',end='')
# # #     for j in range(i,n):
# # #         print('*',end='')
# # #     print()  
   
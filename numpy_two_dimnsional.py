from numpy import *
arr=array([[10,20,30,40],[50,60,70,80]])

"""1.Printing 2D array"""

'''Without index'''
# for r in arr:
#     for c in r:
#         print(c)
#     print()    

'''With index- for loop'''  
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j])
#     print()    

'''With index- While loop'''   
# i=0
# while(i< len(arr)):
#     j=0
#     while (j<len(arr[i])):
#         print(arr[i][j])   
#         j=j+1
#     i=i+1
#     print()    

'''2.Initialize and print 2D zeros/Ones Array'''

'''zeros'''
# arr=zeros((3,2),dtype=int)
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#        print(arr[i][j])
#     print()    
'''Ones'''
# arr1=ones((3,4),dtype=int)
# for i in range(len(arr1)):
#     for j in range(len(arr1[i])):
#        print(arr1[i][j])
#     print()       

'''3.Reshape and flatten use'''
# arr=array([1,2,3,4,5,6,7,8,9,10,11,12])
# arr1=reshape(arr,(4,3))
# arr2=reshape(arr,(2,3,2))

# print(arr)
# print(arr1)
# print(arr2)

# arr3=array([[1,2,3,4],[5,6,7,8]])
# arr4=reshape(arr3,8)
# print(arr4)

'''Flatten--This method used to convert 2D or 3D array into 1D array '''
# arr5=arr3.flatten()
# print(arr5)

'''4.Input from user in numpy two dimentional array'''

# m=int(input("Enter the number of rows ="))
# n=int(input("Enter the number of columns ="))
# arr1=zeros((m,n),dtype=int)
# print(arr1)

# for i in range(len(arr1)):
#     for j in range(len(arr1[i])):
#         arr1[i][j]=int(input(f"Insert Element arr1[{i}][{j}] ="))

# for i in range(len(arr1)):
#     for j in range (len(arr1[i])):
#         print (arr1[i][j])         

# print(arr1)

+

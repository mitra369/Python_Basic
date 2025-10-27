from numpy import *
'''1.Add two array'''

# arr1=array([10,20,30,40])
# arr=arr1-5
# print(arr)


# arr2=array([10,15,20,25])

# arr3=arr1+arr2
# for i in range(len(arr3)):
#     print(arr3[i])

'''2.Comparison between two array'''
# arr1=array([10,20,30,40]) 
# arr2=array([10,15,20,25])

# print(arr1==arr2)
# print(arr1>=arr2)
# print(any(arr1==arr2))
# print(all(arr1==arr2))
  
'''3.Where function'''
# arr1=array([10,20,30,40]) 
# arr2=array([10,15,50,25])
# result=where(arr1>arr2,arr1,arr2)
# print(result)

"""4.Nonzero"""

# arr=([10,20,30,0,0,10,68])
# result=nonzero(arr)
# print(result)

"""5.VIEW METHOD--If one change then another will be changed"""
# arr1=array([10,20,30,40,50])
# arr2=arr1.view()

# arr1[1]=100
# arr2[3]=100
# print(arr1)
# print(arr2)
# print(id(arr1)) 
# print(id(arr2))

"""6.Copy Method--Independent"""

# arr1=array([10,20,30,40,50])

# arr2=arr1.copy()
# arr1[1]=100
# arr2[3]=100
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

"""7.Input new value in zeros array"""
# number=int(input("How many numbers do you want too enter= "))
# arr=zeros(number,dtype=int)
'''For loop'''
# for i in range(len(arr)):
#     arr[i]=int(input("Enter element= "))

# for i in range(len(arr)):
#     print(arr[i])

"""While loop"""     
# i=0
# while(i<number):
#     arr[i]=int(input("Enter element= "))
#     i=i+1

# j=0
# while(j<number):
#     print(arr[j])
#     j=j+1


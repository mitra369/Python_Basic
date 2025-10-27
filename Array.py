'''1.Array initialize'''
# from array import *
# student_id=array('i',[210112,210113,210114])
# print(student_id[2])

'''2.Access array using for loop'''
# from array import*

"""Without accessing index"""
# stu_id= array('i',[11,21,31,41,51,61,71,81,91])
# for i  in stu_id:
#     print(i)
#     i=i+1
    
'''Accessing index'''
# length= len(stu_id)
# for i in range(length):
#     print(i, "=", stu_id[i])



"""3.Accessing array using while loop"""  

# from array import*
# stu_id=array('i',[11,21,31,41,51,61])
# length= len(stu_id)

# i=0
# while(i<length):
#     print(i, '=' , stu_id[i])
#     i=i+1

'''4.Append -- Used to add an element at the end of the array'''

# from array import*
# stu_id=array('i',[11,21,31,41,51,61])
# stu_id.append(71)
# length1=len(stu_id)
# i=0
# while(i<length1):
#     print(stu_id[i])
#     i=i+1

"""5.Getting User"""    

# from array import*
# stu_id=array('i',[])
# n=int(input("How many ID's do you want to enter= "))

# for i in range(n):
#     stu_id.append(int(input("Enter ID= ")))
    

# length= len(stu_id) 
# for i in range(length):
#     print(stu_id[i])


"""6.Insert method-- Insert in a selected position"""    
    
# from array import*
# stu_id=array('i',[11,21,31,41,51,61])

# for i in range(len(stu_id)):
#     print(stu_id[i])

# stu_id.insert(2,100)
# stu_id.insert(3,500)

# print("New Array= ")
# for i in range(len(stu_id)):
#     print(stu_id[i])

"""7.POP method"""

# from array import*
# stu_id=array('i',[11,21,31,41,51,61])

# for i in range(len(stu_id)):
#     print(stu_id[i])


# stu_id.insert(2,100)
# stu_id.insert(3,500)
"""POP last index"""
# stu_id.pop()
# stu_id.pop()

"""POP any position"""
# stu_id.pop(1)
# stu_id.pop(3)


# print("New Array= ")
# for i in range(len(stu_id)):
#     print(stu_id[i])

"""This two process(Insert and POP) happpen one by one.
 After doing one task it generate a new array and do the later part . 
 Like inserting or poping two values after the first insert it will
 generate a new array with new idexing and do the second insert"""


"""8.
Remove method
Index method
Reverse methd
All of these three works with the value not index number
"""

# from array import*
# stu_id=array('i',[11,21,31,41,51,61])

# print(stu_id.index(51))
# for i in range(len(stu_id)):
#     print(stu_id[i])
 
# print('New array=  ') 
# stu_id.remove(31)
# for i in range(len(stu_id)):
#     print(stu_id[i])

# print("After reversing= ")
# stu_id.reverse()
# for i in range(len(stu_id)):
#     print(stu_id[i])

"""9.Extend method"""
# from array import*
# stu_id1=array('i',[10,20,30])
# stu_id2=array('i',[40,50,60,70])
# for i in range(len(stu_id1)):
#     print(stu_id1[i])

# stu_id1.extend(stu_id2)

# print("After array extend=  ")

# for i in range(len(stu_id1)):
#     print(stu_id1[i])

'''10. Slice-Array'''
# from array import*
# stu_id=array('i',[11,21,31,41,51,61,71,81,91])

# for i in range(len(stu_id)):
#     print(stu_id[i])

# print("After slicing= ")
# for i in stu_id[1:4]:
#     print(i)
# print('****')
# for i in stu_id[-7:-2]:
#     print(i)
# print('*****')
# for i in stu_id[-7:-2:2]:
#     print(i)    
    
'''Slice-String'''
# name="antumitra" 
# print(name[1:4])
 
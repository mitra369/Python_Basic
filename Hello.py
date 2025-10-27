""" 1.Printing Anything"""
# print("Hello World")  

""" 2.List  """
# Data=[10,20,30,40,'ANTU']
# print(Data)
# print(type(Data))    
# print(Data[1])
# Data[2]=100
# print(Data[2])
# print(Data)

""" 3.Tupple  """
# Data1=(10,20,30,40,'ANTU')
# print(Data1)
# print(Data1[3])

"""We can't assign a new value in tupple"""
# Data1[1]=50
# print(type(Data1))

"""  4.Set   """
# --Doesnt accept duplicate eliments and eliments maynot appear in the same order as they entered. 
# Data2={30,40,39,'End'}
# print(Data2)
# print(type(Data2))

"""  5. Range  """
# rg=range(10)
# print(rg[9])
# rgb=range(10,50,2)
# print(rgb[1])

"""  6. Mappping """
# Map represents a group of elements in the form of key value pairs.
# Mapping={50:'Antu',100:"AntuPro"}
# print(Mapping)
# print(Mapping[50])
# Mapping1={'Antu':50, 'AntuPro':100}
# print(Mapping1)
# print(Mapping1['AntuPro'])
# print(type(Mapping))

"""  7.Slicing """
# name="Antu Mitra"
# print(name)
# print(type(name))
# print(name[3:6])
# print(name[:6])
# ''' In negative first number means the last n elements and second number tell us when to stop '''
# print(name[-6:-1])
# print (name[1:9:2])

''' 8.Use of ** and Giving the floor value'''

# num1=3
# num2=8
# num3=-3
''' power'''
# print(num1**num2)
'''floor value'''
# print(num2//num1)
# print(num1//num2)
# print(num3//num2)

"""
9.1--1's compliment
 9.2--Left shift
 9.3--Right shift
 9.4--Binary AND
 9.5--Binary OR
 9.6--X-OR

 """
# a=10
# b=15
# print("1,s Complement=", ~a)
# print("Left shift=", a<<2)
# print("Right shift=", a>>2)
# print("Binary AND=", a&b)
# print("Binary OR= ",a|b)
# print("X-OR=",a^b)

""" 10.Indentity Operator(is)"""
# p=10
# q='10'
# print(p is q) 
# print(p is not q)

""" 11.Membership Operator(in)"""
# name= 'Antu Mitra'
# print('Mit' in name)
# print('mit'  not in name)

""" 12.DataType Covert"""
# number='10'
# print(int(number))

# mylist=[10,20,30,40,50]
# print(tuple(mylist))
# print(set(mylist))

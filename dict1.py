# limit=int(input("enter the number of element"))
# list1=[]
# for i in range(limit):
#     data=int(input("enter ur element"))
#     list1.append(data)   
# print(list1)

# limit=int(input("enter the number of elemets"))
# dict1={}
# for i in range(limit):
#     key1=input("enter ur key")
#     value=input("enter ur value")
#     dict1[key1]=value
# print(dict1)

limit=int(input("enter the limit"))
dict1={}
for i in range (limit):
    # key1=(i)
    # value=(i*i)
    # dict1[key1]=value
    dict1[i]=i*i
print(dict1)
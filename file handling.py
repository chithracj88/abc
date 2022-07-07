# f_obj=open("trial.txt",'w')
# f_obj.write("hello")
# f_obj.close()

# f_obj=open("trial.txt",'a')
# f_obj.write("python")
# f_obj.close()

# f_obj=open("trial.txt",'r')
# data=f_obj.read()
# print(data)
# f_obj.close()

# f_obj=open("trial2.py","r")
# data1=f_obj.read()
# f_obj1=open("test2.py","w")
# f_obj1.write(data1)
# f_obj.close()
# f_obj1.close()


# f_obj=open("trial.txt",'w')
# print(f_obj.tell())
# f_obj.write("hello")
# print(f_obj.tell())
# f_obj.seek(3)
# f_obj.write("python")
# f_obj.close()

# with open("trial.txt1",'w') as f_obj:
#     f_obj.write("hello chithra")

# f_obj=open("trial.txt2","w")
# f_obj.write("hello")
# f_obj.seek(3)
# f_obj.write("python")


# import csv
# with open("trial.csv","w",newline='') as f_obj :
#     csvwriter=csv.writer(f_obj,delimiter='\t')

#     header=["name","age","address"]
#     csvwriter.writerow(header)

#     data=['anu',"20","house"],["tom","30","town"]
#     csvwriter.writerows(data)

# import csv
# with open("trial.csv","r") as f_obj :
#     csvreader=csv.reader(f_obj,delimiter='\t')

#     for row in csvreader:
#         print(row)


# zip and unzip
# import shutil
# shutil.make_archive('zipfile',format='zip',root_dir='trial')


# import shutil
# shutil.unpack_archive('zipfile.zip','unzipped')


# EXCETIONAL HANDELLING
# int("hello")

# Exceptional Handelling

# try:
#     a=int(input("enter the data"))
#     b=int(input("enter the data"))
#     print(a/b)

# except Exception:
#     print("Error occured")
# try:
#     a=int(input("enter the data"))
#     b=int(input("enter the data"))
#     print(a/b)

# except ZeroDivisionError:
#     print("No zero in dinominator")

# except ValueError:
#     print("enter intiger value")

# to get the same command promt erroe
try:
    a=int(input("enter the data"))
    b=int(input("enter the data"))
    print(a/b)

except ZeroDivisionError as Z:
    print(Z)

except ValueError as v:
    print(v)

else:
    print("successful")
finally:
    print("the end")
    
# posneg = lambda a: "positive" if a > 0 else "negatitve or zero"
# num = int(input("enter a number"))
# print(posneg(num))

# evenodd = lambda a: "even" if a % 2 == 0 else "odd"
# num = int(input("enter a number"))
# print(evenodd(num))

# largest = lambda a,b: a if a>b else b 
# num = int(input("enter a number"))
# num2 = int(input("enter the second number"))
# print(largest(num,num2))

# largest = lambda a,b,c: a if a>b and a > c else (b if b >c else c)
# num1 = int(input("enter first num"))
# num2 = int(input("enter second number"))
# num3 = int(input("enter the third number"))
# print(largest(num1,num2,num3))

# vote = lambda a: "eligible to vote" if a > 18 else "not eligible for vote"
# age = int(input("enter your age"))
# print(vote(age))

# divisible = lambda a: "Divisible by 5" if a % 5 == 0 else "Not divisible by 5"
# numb = int(input("enter a number"))
# print(divisible(numb))

# check = lambda a: ("Divisible by both 3 and 5" if a % 3 == 0 and a % 5 == 0 else "Only divisible by 3" if a % 3 == 0 else "Only divisible by 5" if a % 5 == 0 else "Not divisible by both 3 and 5")
# num = int(input("Enter a number: "))
# print(check(num))

# try:
#     num1 = int(input("enter a number"))
#     num2 = int(input("enter second number"))
#     result = num1 / num2 
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by Zero")    

# try:
#     mark = int(input("enter your mark"))
#     print(mark)
# except ValueError:
#     print("please enter a integer")

# try:
#     file = open("example.txt","r")
#     print(file.read())
# except FileNotFoundError:
#     print("file not found")

# try: 
#     list1 = [12,56,88]
#     index = int(input("enter a index"))
#     print(list1[index])
# except IndexError:
#     print("No such index")

# try:
#     dict1 = {"name" : "Thahsi","age" : 15,"mark": 50}
#     key = input("enter a key: ")
#     print(dict1[key])
# except KeyError:
#     print("enter a valid key")

# try:
#     import mytype
# except ImportError:
#     print("import error")

# with open("address.txt","w") as f:
#     f.write("Name : Swetha\n")
#     f.write("Adress :Sasi vihar kozhikode\n")

# with open("example.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("address.txt","a") as f:
#     f.write("pincode : 673021.\n")

# import csv
# with open("students.csv","w") as file :
#     writer = csv.writer(file)
#     writer.writerow([1,"swetha",21])
#     writer.writerow([2,"nandana",20])

# import csv
# with open("students.csv","r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# import json 
# student ={ 
#     "rollno" : 1,
#     "name" : "swetha",
#     "age" : 21,
#     "marks" : 50,
# }

# with open("student.json","w") as file:
#     json.dump(student,file,indent = 4)
# print("JSON file created successfully")

# import json

# with open("student.json","r") as file:
#     student = json.load(file)
#     print(student)

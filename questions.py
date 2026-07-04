           #questions
n = float(input("Enter  total purchase amount"))
if n >= 5000:
    discount = n * 20 / 100
    print("final payable amount : ",n - discount)
elif  n >= 2000 and n < 5000:
    discount = n * 10 / 100
    print("final payable amount : ",n - discount)
else:
    print("No discount")
print("final payable amount : ", n)



num = int(input("Enter a number :"))
if num % 10 == 0:
    print("not valid")
elif num % 3 == 0:
    print("valid")
else:
    print("not valid")

s = input("enter the first  string : ")
a = input("enter the second string : ")
if len(s) == len(a) and  sorted(s) == sorted(a):
    print("strings are anagrams ")
else:
    print("not anagram")

username = "swetha"
password = 29102004
user = input("Enter the username : ")
passw = int(input("enter the password : "))
if username == user and password == passw :
    print("Login successfull")
else :
    print("invalid")

num = int(input("Enter a number : "))
if  num % 3 == 0 and num % 5 == 0:
    print("fizz buzz")
elif num % 3 == 0:
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print("error")

num = int(input("enter a no : "))
if num % 2 == 0:
    if num % 4 == 0 :
        print("number is divisible by 2 and 4")
    else:
        print("divisible by 2 but not by divisible by 4")
else:
    print("invalid")



name = input("enter your name : ")
age = int(input("enter your age : "))
exam = float(input("enter your exam percentage : "))
income = int(input(" enter your family annual income :"))
scholarship = input("Are you already receiving another scholarship (yes/no) : ")
if age >= 17 and age <= 25 and income < 800000 and scholarship == "no" :
    if exam >= 85:
        print("Full scholarship")
    elif exam >= 70 and exam <= 84.99:
        print("Partial scholarship")
    else:
        print("Not eligible")
else:
    print("not eligible")


sslc = input("have you passed sslc? (yes/no) ")
if sslc == "yes" :
    plustwo = input("have you completed plustwo? (yes/no) ")
    if plustwo == "yes" :
        percentage = float(input("enter your plustwo percentage :"))
        if percentage > 75:
            print("eligible for engineering admission ")
        else:
            print("eligible for general degree")
    else:
        print("complete twlefth to proceed")
else:
    print("not eligible for admission")



age = int(input("enter your age:"))
income = float(input("enter your monthly income:"))
credit = int(input("enter your  credit score:"))
loan  = int(input("enter your loan amount:"))
if age < 21:
    print("loan denied: age must be 21")
elif income <25000:
    print("loan denied: income too low")
elif loan > income * 20:         
        print("Loan Denied: Loan amount too high compared to income")
else:
    if credit < 650:
        print("Loan Conditionally Approved with 15% interest")
    elif credit <= 750:
        print("Loan Approved with 10% interest")
    else:
        print("Loan Approved with 7% interest")


amt = int(input("enter the amount to withdraw"))
if amt <= 0:
    print("invalid amount")
elif amt % 100 != 0:
    print("amount must be in multiples of 100")
elif amt > 20000:
    print("maximum withdrawal limit is 20000")
else:
    print("Transaction successful")

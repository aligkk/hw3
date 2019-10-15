age=int(input("enter age"))
if age>19:
    print("adult")
elif 10<age<=19:
    print("adolescent")
elif 0<age<1:
    print("infant")
else:
    print("children")
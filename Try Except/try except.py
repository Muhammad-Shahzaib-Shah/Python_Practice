try:
    a = int(input("enter any number: "))
    b = int(input("enter any number: "))
    c = a-b
    print(c)
except Exception as e:
    print(e)

else:
    print("Nothing Went Wrong")
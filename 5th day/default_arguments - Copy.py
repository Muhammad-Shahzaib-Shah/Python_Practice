#Default Arguments 
def GoodDay(name , ending= "Thank You"):
    print("Good Day, " + name , end=" ")
    print(ending)
    return name
#Function Call
a = GoodDay("Shahzaib" , "Thanks")
print(a)
GoodDay("Huzaifa")

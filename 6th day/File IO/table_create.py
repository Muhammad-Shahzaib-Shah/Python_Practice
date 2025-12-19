def table(n):
    tables = ""
    for i in range(1,11):
        tables += f"{n} X {i} = {n*i} \n"  
        with open(f"table/table{n}.txt" , "w") as f: 
            f.write(tables)
    
    
for i in range(2,101):
    table(i)
print("Tables Created")
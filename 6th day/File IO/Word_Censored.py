def cens(string):
    words = ["bad" , "ugly" , "stupid" , "idiot" , "fool" ,"hate" , "spam" , "dummy" , "nonsense", "trash"]
    with open(string , "r") as f:
        content = f.read()
        for word in words:
                content = content.replace(word , "#"*len(word) )
                content = content.replace(word.upper() , "#"*len(word) )       
                content = content.replace(word.capitalize() , "#"*len(word) )       
                
        with open(string , "w") as f:
            f.write(content)
cens("Word_Censored.txt")
print("Word Censored")
                
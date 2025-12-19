import random
def hiscore():
    score = random.randint(1,200)
    print(score)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore =="":
            hiscore=0
        
        if hiscore !="":
            int(hiscore)
        
    if int(score)>int(hiscore):
        with open("hiscore.txt" , "w") as f:
            f.write(str(score))
    return score
hiscore()
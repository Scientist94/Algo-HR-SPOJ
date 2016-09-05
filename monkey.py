import random

def generate(strlen):
    alphabet="abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
        
    return res


def score(goalstring, teststring):    
    numSame = 0
    for i in range(len(goalstring)):
        if goalstring[i] == teststring[i]:
            numSame += 1
        return numSame/len(goalstring)

        ###function : return value to contain matched character , diff func to store returned chars in list[]
        ###lsit to be returned for further comp 

def main():
    goalstring = "methinks it is like a weasel"
    count = 0
    newstring = generate(28)
    best = 0
    newscore = score(goalstring, newstring)
    while newscore < 1:
        count += 1
        if newscore >= best: 
            best = newscore
            print (newscore, newstring)
                  

        if count%1000 == 0:
            print("Best score after 1000retries", best)

        newstring = generate(28)
        newscore = score(goalstring, newstring)

main()

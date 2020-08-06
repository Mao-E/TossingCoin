import random

print("Tossing a coin...")
coin=["Heads","Tails"]
countheads=0
counttails=0
for i in range(3):
    c=coin[random.randrange(2)]
    print("Round {0}: {1}".format(i+1,c))
    if c==coin[0]:
        countheads+=1
    else:
        counttails+=1

print("Heads: {0}, Tails: {1}".format(countheads,counttails))
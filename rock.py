import random
while True:
    choice=int(input("Choose \n0: Rock.\n1: Paper.\n2: Scissors.\n"))
    list =[["Draw","Loose","Win"],
        ["Win","Draw","Loose"],
        ["Loose","Win","Draw"]]
    num=[0,1,2]
    computerChoice=random.choice(num)
    print("Computer choice was: ",computerChoice)
    print("For this round You ",list[choice][computerChoice])
    cont=input("Press any other key to continue or 'E' to Exit!" )
    if(cont=="E" or cont=="e"):
        break
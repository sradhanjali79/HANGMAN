import random
def hangman():
    words=["hangman","project","login","laptop"]
    choose=random.choice(words)
    # print(choose)
    turns=10
    guessing=""
    letter='abcdefghijklmnopqrstuvwxyz'
    while len(choose)>0:
        word=""
        for i in choose:
            if i in guessing:
                word=word+i
            else:
                word=word+"_"
        if word==choose:
            print(word)
            print("you won....")
            break
        print("guess the word")
        guess=input("enter any character...")
        if guess in letter:
            guessing=guessing+guess
        else:
            print("enter valid character")
            g=input("enter....")
        if guess not in choose:
            turns-=1
            if turns==9:
                print("9 turns left...")
                print("----------")
            if turns==8:
                print("8 turns left")
                print("----------")
                print("     o     ")
            if turns==7:
                print("7 turns left")
                print("----------")
                print("     o     ")
                print("     |     ")
            if turns==6:
                print("6 turns left")
                print("----------")
                print("     o     ")
                print("     |     ")
                print("    /     ")
            if turns==5:
                print("5 turns left")
                print("----------")
                print("     o     ")
                print("     |     ")
                print("    / \    ")
            if turns==4:
                print("5 turns left")
                print("----------")
                print("    \o     ")
                print("     |     ")
                print("    / \    ")
            if turns==3:
                print("3 turns left")
                print("----------")
                print("    \o/     ")
                print("     |     ")
                print("    / \    ")
            if turns==3:
                print("3 turns left")
                print("----------")
                print("    \o/    ")
                print("     |     ")
                print("    / \    ")
            if turns==2:
                print("2 turns left")
                print("----------")
                print("    \o/ |   ")
                print("     |     ")
                print("    / \    ")
            if turns==1:
                print("only 1 turns left......hangman on his last breath")
                print("----------")
                print("    \o/_|   ")
                print("     |     ")
                print("    / \    ")
            if turns==0:
                print("you loose")
                print("good man is died")
                print("----------")
                print("     o_|   ")
                print("    /|\     ")
                print("    / \    ")
                break
user=input("enter your name...")
print("welcome",user,".....")
print("           ")
print("try to guess the word in less than 10 attempts")
hangman()

            







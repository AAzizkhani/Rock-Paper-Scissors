import random
import time

#START!_____________________________

START=input("press enter to start: ")
print("_______________________________")

#welcoming_________________________

time.sleep(0.5)
print("rock...")
time.sleep(0.5)
print("paper...")
time.sleep(0.5)
print("scissors...")

print("_______________________________")

time.sleep(0.5)
player_name=input("welcom! \n plaese write your name: ")


print("_______________________________")

while player_name=="" or player_name==" " or player_name=="  " :
    time.sleep(0.5)
    print("it is empty!")
    print("_______________________________")
    time.sleep(0.5)
    player_name=input("plaese write your name: ")


time.sleep(0.5)
print(f"good {player_name}")



#players score____________________

player1_score=0
player2_score=0
wininig_score=5

#the logic of game________________

while player1_score < wininig_score and player2_score < wininig_score:
        #the compter move_________________

    rand_num=random.randint(0,2)
    comp_move="rock"
    if rand_num==0:
        comp_move="rock"
    elif rand_num==1:
        comp_move="paper"    
    elif rand_num==2:
        comp_move="scissors"
        
    print("_______________________________")
    time.sleep(0.5)
    print(f"{player_name} : {player1_score}| me : {player2_score}")
    print("_______________________________")
    time.sleep(0.5)
    print("rock...")
    time.sleep(0.5)
    print("paper...")
    time.sleep(0.5)
    print("scissors...")
    time.sleep(0.5)
    player1=input(f"make your move {player_name} : ").lower()
    
    while player1 == "" or player1 == " " or player1 == "  ":
        print("_______________________________")
        time.sleep(0.5)
        print ("it is empty!")
        print("_______________________________")
        time.sleep(0.5)
        print("rock...")
        time.sleep(0.5)
        print("paper...")
        time.sleep(0.5)
        print("scissors...")
        time.sleep(0.5)
        player1=input(f"make your move {player_name}: ").lower()
        
    print("_______________________________")
    time.sleep(0.5)
    print("rock...")
    time.sleep(0.5)
    print("paper...")
    time.sleep(0.5)
    print("scissors...")
    print(f"i am player2 i move : {comp_move} ")
    player2=comp_move

    if (player1[0]=="Q" or player1[0]=="q") or (player1[0]=="E" or player1[0]=="e"):
        print("_______________________________")
        time.sleep(0.5)
        print(f"oh! {player_name} you end the game!\n so goodbye! ")
        time.sleep(0.5)
        break

    if player1==player2:
        print("_______________________________")
        time.sleep(0.5)
        print("it is a tie!")
    elif player1=="rock":
        if player2=="paper":
            print("_______________________________")
            time.sleep(0.5)
            print("haha! i win!")
            player2_score+=1
        elif player2=="scissors":
            print("_______________________________")
            time.sleep(0.5)
            print(f"wow! {player_name} win!")
            player1_score+=1
    elif player1=="paper":
        if player2=="scissors":
            print("_______________________________")
            time.sleep(0.5)
            print("haha! i win!")
            player2_score+=1
        elif player2=="rock":
            print("_______________________________")
            time.sleep(0.5)
            print(f"wow! {player_name} win!")
            player1_score+=1
    elif player1=="scissors":
        if player2=="rock":
            print("_______________________________")
            time.sleep(0.5)
            print("haha! i win!")
            player2_score+=1
        elif player2=="paper":
            print("_______________________________")
            time.sleep(0.5)
            print(f"wow! {player_name} win!")
            player1_score+=1 
    else:
        print("_______________________________")
        time.sleep(0.5)
        print(f"something went wrong in your move!\n check it again {player_name}!")

print("_______________________________")
time.sleep(0.5)
print(f"final score:{player_name} : {player1_score}| me : {player2_score}")
print("_______________________________")
time.sleep(0.5)
print(f"good end!\n see you then {player_name} ")

# ask play again____________________

ask_play_again=input("hey you can play again if you want to!(yes or no): ")
while ask_play_again=="" or ask_play_again==" " or ask_play_again=="  ":
    print("_______________________________")
    time.sleep(0.5)
    print("it is empty")
    print("_______________________________")
    time.sleep(0.5)
    ask_play_again=input("i say! you can play again if you want to!(yes or no): ")
    
while ask_play_again!="no" and ask_play_again!="yes":
    time.sleep(0.5)
    print ("just yes or no human!")
    print("_______________________________")
    time.sleep(0.5)    
    ask_play_again=input("play again if you want to!(yes or no): ")
    while ask_play_again=="" or ask_play_again==" " or ask_play_again=="  ":
        print("_______________________________")
        time.sleep(0.5)
        print("it is empty")
        print("_______________________________")
        time.sleep(0.5)
        ask_play_again=input("comeon idiot human! i say! you can play again if you want to!(yes or no): ")
    
    
#nooooooooor________________
if ask_play_again=="no":
    print("_______________________________")
    time.sleep(0.5)
    print("ok!")
    print("_______________________________")
    time.sleep(0.5)
    END=input("press enter to end: ")
    exit(0)

#play again____________________

while ask_play_again=="yes":
    print("_______________________________")
    time.sleep(0.5)
    print(f"good {player_name}")


#players score____________________

    player1_score=0
    player2_score=0
    wininig_score=5

#the logic of game________________

    while player1_score < wininig_score and player2_score < wininig_score:
    #the compter move_________________

        rand_num=random.randint(0,2)
        comp_move="rock"
        if rand_num==0:
            comp_move="rock"
        elif rand_num==1:
            comp_move="paper"    
        elif rand_num==2:
            comp_move="scissors"

        print("_______________________________")
        time.sleep(0.5)
        print(f"{player_name} : {player1_score}| me : {player2_score}")
        print("_______________________________")
        time.sleep(0.5)
        print("rock...")
        time.sleep(0.5)
        print("paper...")
        time.sleep(0.5)
        print("scissors...")
        time.sleep(0.5)
        player1=input(f"make your move {player_name}: ").lower()
        
        while player1 == "" or player1 == " " or player1 == "  ":
            print("_______________________________")
            time.sleep(0.5)
            print ("it is empty!")
            print("_______________________________")
            time.sleep(0.5)
            print("rock...")
            time.sleep(0.5)
            print("paper...")
            time.sleep(0.5)
            print("scissors...")
            time.sleep(0.5)
            player1=input(f"make your move {player_name}: ").lower()
            
        print("_______________________________")
        time.sleep(0.5)
        print("rock...")
        time.sleep(0.5)
        print("paper...")
        time.sleep(0.5)
        print("scissors...")
        time.sleep(0.5)
        print(f"i am player2 i move: {comp_move} ")
        player2=comp_move

        if (player1[0]=="Q" or player1[0]=="q") or (player1[0]=="E" or player1[0]=="e"):
           print("_______________________________")
           time.sleep(0.5)
           print(f"oh! {player_name} you end the game!\n so goodbye! ")
           time.sleep(0.5)
           break

        if player1==player2:
           print("_______________________________")
           time.sleep(0.5)
           print("it is a tie!")
        elif player1=="rock":
           if player2=="paper":
               print("_______________________________")
               time.sleep(0.5)
               print("haha! i win!")
               player2_score+=1
           elif player2=="scissors":
               print("_______________________________")
               time.sleep(0.5)
               print(f"wow! {player_name} win!")
               player1_score+=1
        elif player1=="paper":
           if player2=="scissors":
               print("_______________________________")
               time.sleep(0.5)
               print("haha! i win!")
               player2_score+=1
           elif player2=="rock":
               print("_______________________________")
               time.sleep(0.5)
               print(f"wow! {player_name} win!")
               player1_score+=1
        elif player1=="scissors":
           if player2=="rock":
               print("_______________________________")
               time.sleep(0.5)
               print("haha! i win!")
               player2_score+=1
           elif player2=="paper":
               print("_______________________________")
               time.sleep(0.5)
               print(f"wow! {player_name} win!")
               player1_score+=1 
        else:
           print("_______________________________")
           time.sleep(0.5)
           print(f"something went wrong in your move!\n check it again {player_name}!")
    print("_______________________________")
    time.sleep(0.5)
    print(f"final score:{player_name} : {player1_score}| me : {player2_score}")
    print("_______________________________")
    time.sleep(0.5)
    print(f"good end!\n see you then {player_name} ")

    ask_play_again=input("hey you can play again if you want to!(yes or no): ")
    while ask_play_again=="":
       time.sleep(0.5)
       print("it is empty")
       time.sleep(0.5)
       ask_play_again=input("i say! you can play again if you want to!(yes or no): ")

#END!_________________
print("_______________________________")
time.sleep(0.5)
END=input("press enter to end: ")




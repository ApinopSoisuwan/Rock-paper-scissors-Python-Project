def RPS_Rule ():
    #Com
    def Bot():
        import random
        bot = random.choice(["Rock","Paper","Scissors"])
        return bot
    #Player
    def Player():
        player = {1:"Rock",2:"Paper",3:"Scissors"}
        player_choice = input("Select Rock = 1, Paper = 2 , Scissors = 3 \nSelect: ")
        coin_play = 0
        while coin_play <= 1:
            if int(player_choice) >= 4 :
                print("Error:Try again")
                return Player()
            elif int(player_choice) <= 3 :
                coin_play += 1
                return player[int(player_choice)]

    # Rule
    Coin_rule = 0
    while Coin_rule <= 1 :
        if Player() == Bot():
            print("Draw Try Again")
            return RPS_Rule()
        #Player Win
        elif Player() == "Paper" and Bot() == "Rock" or \
                Player() == "Rock" and Bot() == "Scissors" \
                or Player() == "Scissors" and Bot() == "Paper":
            print("Player Win \nPlayer Again Press 1 , Exit Press 0")
        #Bot Win
        elif Bot() == "Paper" and Player() == "Rock" or \
                Bot() == "Rock" and Player() == "Scissors" \
                or Bot() == "Scissors" and Player() == "Paper":
            print("Bot Win \nPlayer Again Press 1 , Exit Press 0")


print(RPS_Rule())







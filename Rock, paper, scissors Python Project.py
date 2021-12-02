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

    player = Player()
    bot = Bot()

    # Rule
    Coin_rule = 0
    while Coin_rule < 1 :
        if player == bot:
            print("\nDraw Try Again")
            return RPS_Rule()
        #Player Win
        elif player == "Paper" and bot == "Rock" or \
                player == "Rock" and bot == "Scissors" \
                or player == "Scissors" and bot == "Paper":
            Coin_rule += 1
            print("Player: "+ player + "\n" +"Com:    " + bot +"\nPlayer Win \nPlay Again Press 1 , Exit Press 0")
        #Bot Win
        elif bot == "Paper" and player == "Rock" or \
                bot == "Rock" and player == "Scissors" \
                or bot == "Scissors" and player == "Paper":
            Coin_rule += 1
            print("Player: "+ player + "\n" +"Com:    " + bot +"\nBot Win \nPlay Again Press 1 , Exit Press 0")


print(RPS_Rule())







def RPS_Rule ():
    #Com
    def Bot():
        import random
        bot = random.choice(["Rock","Paper","Scissors"])
        return bot

    #Player
    def Player():
        player = {1:"Rock",2:"Paper",3:"Scissors"}
        player_choice = input("\nSelect Rock = 1, Paper = 2 , Scissors = 3 \nSelect: ")
        coin_play = 0
        try:
            while coin_play <= 1:
                if int(player_choice) >= 4 or int(player_choice) <= 0:
                    print("Error:Try again")
                    return Player()
                elif int(player_choice) <= 3 :
                    coin_play += 1
                    return player[int(player_choice)]
        except:
                print("Error:Try again")
                return Player()

    def play_again (n):
        coin_press = 0
        error_massage = "\nError: Play Again Press 1 , Exit Press 0\nPress: "
        try:
            while coin_press <= 1:
                if n == 1:
                    coin_press += 1
                    return(RPS_Rule())
                elif n == 0:
                    coin_press +=1
                    return("\nEXIT: ___Thank you___")
                else:
                    return play_again(int(input(error_massage)))
        except:
                print("Error:Try again")
                return play_again (n)

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
            print("\nPlayer: "+ player + "\n" +"Com:    " + bot \
                  +"\n\nPlayer Win\nPlayer Win\nPlayer Win \n\nPlay Again Press 1 , Exit Press 0")
        #Bot Win
        elif bot == "Paper" and player == "Rock" or \
                bot == "Rock" and player == "Scissors" \
                or bot == "Scissors" and player == "Paper":
            Coin_rule += 1
            print("\nPlayer: "+ player + "\n" +"Com:    " + bot \
                  +"\n\nBot Win\nBot Win\nBot Win \n\nPlay Again Press 1 , Exit Press 0")
    return play_again((input("\nPress: ")))
print(RPS_Rule())







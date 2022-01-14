from random import randint

game_active = True
game_playing = True

while game_active:
    print("Let's play Rock Paper Scissors!")
    name = input("What's your name? ")
    while game_playing:
        tie = 0
        win = 0
        lose = 0
        print(f"{name.title()}! Input your command!")
        option = input("Rules, play, or quit: ")
        game_on = True
        if option.lower() == "rules":
            print("The game is played where players deliver hand signals that will represent the elements of the game; rock, paper and scissors.\nThe outcome of the game is determined by 3 simple rules:\nRock wins against scissors.\nScissors win against paper.\nPaper wins against rock.")
        elif option.lower() == "play":
            while game_on:
                user_answer = input("Choose your weapon. Rock/Paper/Scissors: ")
                comp_int = randint(1,3)
                if comp_int == 1:
                    computer = "rock"
                elif comp_int == 2:
                    computer = "paper"
                else:
                    computer = "scissors"
                if user_answer == computer:
                    print(f"{computer.title()}!\nTie!")
                    tie += 1
                elif (user_answer.lower() == "rock" and computer == "scissors") or (user_answer.lower() == "paper" and computer == "rock") or (user_answer.lower() == "scissors" and computer == "paper"):
                    print(f"{computer.title()}!\nYou win!")
                    win += 1
                else:
                    print(f"{computer.title()}!\nYou lose...")
                    lose += 1
                print(f"Score:\nWin: {win} - Lose: {lose} - Draw: {tie}")
                play_again = True
                while play_again:
                    choice = input("Play again? Y/N ")
                    if choice.lower() == "y":
                        play_again = False
                    elif choice.lower() == "n":
                        game_on = False
                        play_again = False
                    else:
                        print("That's not an option!")
        elif option.lower() == "quit":
            game_playing = False
            game_active = False
        else:
            print("That's not an option!")
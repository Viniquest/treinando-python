import random

def get_choices():
    player_choice = input("Escolha sua jogada (pedra, papel, tesoura): ")
    options = ["pedra", "papel", "tesoura"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"Você escolheu {player}, o computador escolheu {computer}")
    if player == computer:
        return "Temos um empate!"
    elif player == "pedra": 
        if computer == "tesoura":
            return "Pedra amassa tesoura! Você ganhou!"
        else:
            return "Papel cobre pedra! Você perdeu :/"
    elif player == "tesoura": 
        if computer == "papel":
            return "Tesoura corta papel! Você ganhou!"
        else:
            return "Pedra amassa tesoura! Você perdeu :/"
    elif player == "papel": 
        if computer == "pedra":
            return "Papel cobre pedra! Você ganhou!"
        else:
            return "Tesoura corta papel! Você perdeu :/"
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
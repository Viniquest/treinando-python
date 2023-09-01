import random

class Carta:
    def __init__(self, ranque, naipe):
        self.ranque = ranque
        self.naipe = naipe
    def __str__(self):
        return f"{self.ranque['ranque']} de {self.naipe}"

class Deck:
    def __init__(self):
        self.cartas = []
        naipes = ["Espadas", "Paus", "Copas", "Ouros"]
        ranques = [
                    {"ranque": "3", "valor": 3},
                    {"ranque": "4", "valor": 4},
                    {"ranque": "5", "valor": 5},
                    {"ranque": "6", "valor": 6},
                    {"ranque": "7", "valor": 7},
                    {"ranque": "8", "valor": 8},
                    {"ranque": "9", "valor": 9},
                    {"ranque": "10", "valor": 10},
                    {"ranque": "J", "valor": 10},
                    {"ranque": "Q", "valor": 10},
                    {"ranque": "K", "valor": 10},
                ]
        for ranque in ranques:
            for naipe in naipes:
                self.cartas.append(Carta(ranque, naipe))

    def shuffle(self):
        if len(self.cartas) > 1:
            random.shuffle(self.cartas)

    def deal(self, number):
        cartas_dadas = []
        for x in range(number):
            if len(self.cartas) > 0:
                carta = self.cartas.pop()
                cartas_dadas.append(carta)
        return cartas_dadas

class Mao:
    def __init__(self, dealer=False):
        self.cartas = []
        self.valor = 0
        self.dealer = dealer
    
    def add_carta(self, lista_carta):
        self.cartas.extend(lista_carta)
    
    def calculo_valor(self):
        self.valor = 0
        possui_ás = False

        for carta in self.cartas:
            valor_da_carta = int(carta.ranque["valor"])
            self.valor += valor_da_carta
            if carta.ranque["ranque"] == "A":
                possui_ás = True

        if possui_ás and self.valor > 21:
            self.valor -= 10

    def pegar_valor(self):
        self.calculo_valor()
        return self.valor
    
    def is_blackjack(self):
        return self.pegar_valor() == 21
    
    def display(self, mostar_cartas_do_dealer=False):
        print(f'''{"Mão do Dealer" if self.dealer else "Sua mão"} :''')
        for index, carta in enumerate(self.cartas):
            if index == 0 and self.dealer and not mostar_cartas_do_dealer and not self.is_blackjack():
                print("escondido")
            else:
                print(carta)
        
        if not self.dealer:
            print("Valor:", self.pegar_valor())
        print()

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <=0:
            try:
                games_to_play = int(input("Quantos jogos você quer jogar? "))
            except:
                print("Você precisa escolher um número.")

        while game_number < games_to_play:
            game_number +=1

            deck = Deck()
            deck.shuffle()

            mao_do_jogador = Mao()
            mao_do_dealer = Mao(dealer = True)

            for i in range(2):
                mao_do_jogador.add_carta(deck.deal(1))
                mao_do_dealer.add_carta(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Jogo {game_number} de {games_to_play}")
            print("*" * 30)
            mao_do_jogador.display()
            mao_do_dealer.display()

            if self.check_vencedor(mao_do_jogador, mao_do_dealer):
                continue

            choice = ""
            while mao_do_jogador.pegar_valor() < 21 and choice not in ["p", "parar"]:
                choice = input("Por favor, escolha se quer 'Mais' ou 'Parar': ").lower()
                print()
                while choice not in ["m", "p", "mais", "parar"]:
                    choice = input("Por favor, escolha se quer 'Mais' ou 'Parar' (ou M/P): ").lower()
                    print()
                if choice in ["mais", "m"]:
                    mao_do_jogador.add_carta(deck.deal(1))
                    mao_do_jogador.display()
            
            if self.check_vencedor(mao_do_jogador, mao_do_dealer):
                continue

            valor_jogador = mao_do_jogador.pegar_valor()
            valor_dealer = mao_do_dealer.pegar_valor()

            while valor_dealer < 17:
                mao_do_dealer.add_carta(deck.deal(1))
                valor_dealer = mao_do_dealer.pegar_valor()
            
            mao_do_dealer.display(mostar_cartas_do_dealer=True)

            if self.check_vencedor(mao_do_jogador, mao_do_dealer):
                continue

            print("Resultados Finais")
            print("Sua mão:", valor_jogador)
            print("Mão do dealer:", valor_dealer)

            self.check_vencedor(mao_do_jogador, mao_do_dealer, True)

        print("\n Obrigado por jogar!")

    def check_vencedor(sel, mao_do_jogador, mao_do_dealer, fim_de_jogo=False):
        if not fim_de_jogo:
            if mao_do_jogador.pegar_valor() > 21:
                print("Você estourou. O dealer venceu!")
                return True
            elif mao_do_dealer.pegar_valor() > 21:
                print("O Dealer estourou. Você venceu!")
                return True
            elif mao_do_dealer.is_blackjack() and mao_do_jogador.is_blackjack():
                print("Ambos tem um blackjack! Empate!")
                return True
            elif mao_do_jogador.is_blackjack():
                print("Você tem um blackjack! Você Venceu!")
                return True
            elif mao_do_dealer.is_blackjack():
                print("O dealer tem um blackjack! O dealer venceu!")
                return True
        else:
            if mao_do_jogador.pegar_valor() > mao_do_dealer.pegar_valor():
                print("Você Venceu!")
            elif mao_do_jogador.pegar_valor() == mao_do_dealer.pegar_valor():
                print("Empate!")
            else:
                print("Dealer venceu!")
        return False
        
g = Game()
g.play()
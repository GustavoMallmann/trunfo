from configsTrunfo import tipos, bonusAtributo, tamanhoDeck
from carta import Carta


class Jogo:

    def __init__(self):
        self.iniciativa = 0
        self.decks = [[Carta() for _ in range(tamanhoDeck)] for _ in range(2)]

    def rodada(self):
        carta_p0 = self.decks[0][0]
        carta_p1 = self.decks[1][0]
        print("\nSua carta:")
        self.mostrar_carta(carta_p0)
        if self.iniciativa == 0:
            atributo = input(f"Jogador {self.iniciativa}, escolha um atributo: ")
        else:
            atributo = tipos[carta_p1.stats.index(max(carta_p1.stats))]
            print(f"\nO oponente escolheu o atributo: {atributo}")
        p_0 = carta_p0.stats[tipos.index(atributo)]
        p_1 = carta_p1.stats[tipos.index(atributo)]
        print("\nCarta do seu oponente:")
        self.mostrar_carta(carta_p1)

        if atributo == carta_p1.type and atributo != carta_p0.type and self.iniciativa == 0:
            p_1 += bonusAtributo
            print(f"A carta do seu oponente é do tipo escolhido e receberá um bônus\n{atributo}: {p_1}")

        if atributo == carta_p0.type and atributo != carta_p1.type and self.iniciativa == 1:
            p_0 += 5
            print(f"A sua carta é do tipo escolhido e receberá um bônus\n{atributo}: {p_0}")
        if p_0 > p_1:
            winner = 0
        elif p_1 > p_0:
            winner = 1
        else:
            winner = 2
        if winner != 2:
            print(f"O jogador {winner} vence o combate")
        else:
            print("Ninguem ganhou o combate")
        self.repasse_cartas(winner)
        print("\n")
        if not self.deck_vazio():
            self.rodada()
        return winner

    def mostrar_carta(self, carta):

        for i, j in zip(tipos, carta.stats):
            print(f"{i}: {j}")
        print(f"{carta.type}\n")
        return

    def repasse_cartas(self, winner):
        if winner != 2:
            self.decks[winner].append(self.decks[winner - 1].pop(0))
            self.decks[winner].append(self.decks[winner].pop(0))
        else:
            self.decks[1].append(self.decks[1].pop(0))
            self.decks[0].append(self.decks[0].pop(0))
        if winner != 2:
            self.iniciativa = winner
        return

    def deck_vazio(self):
        if not self.decks[0]:
            return 10
        elif not self.decks[1]:
            return 11
        else:
            return 0

    def start(self):
        return self.rodada()

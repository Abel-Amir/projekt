import random
import compare_cards

class Black_Jack:
    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.player = [random.choice(self.cards), random.choice(self.cards)]
        self.computer = [random.choice(self.cards), random.choice(self.cards)]
        self.die_or_win = [0, 1000, 0]
        self.cash = [1000]

    def game_card(self):
        print("choise option")
        print("1. Draw cards")
        print("2. Draw cards only to computer")
        print("3. Draw cards only to player")
        print("4. Russian Roulette")
        print("5. Pass round")
        print(f"Your cards : {sum(self.player)}")
        choose = int(input("Your choice :"))
        print(f"your cash : {sum(self.cash)}")
        while True:
            compare_1 = compare_cards.Compare(player_list=self.player,
                                              computer_list=self.computer)
            if choose == 1:
                self.player.append(random.choice(self.cards))
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choose == 2:
                self.computer.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choose == 3:
                self.player.append(random.choice(self.cards))
                if compare_1.compare_results():
                    break
            elif choose == 4:
                self.computer.append(random.choice(self.die_or_win))
                self.player.append(random.choice(self.die_or_win))
                if compare_1.compare_results():
                    break
            elif choose == 5:
                pass
carding = Black_Jack()
carding.game_card()
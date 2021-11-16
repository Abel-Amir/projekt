class Compare:
    def __init__(self, player_list, computer_list):
        self.player_list = player_list
        self.computer_list = computer_list
        self.cash = []
    def compare_results(self):
        if sum(self.player_list) > 21 and sum(self.computer_list) < 21:
            print(f"Our cards : {sum(self.player_list)} Computer Wins ! Computer : {sum(self.computer_list)}")
            print(f"Our cash -1000$")
            return True
        elif sum(self.player_list) < 21 and sum(self.computer_list) > 21:
            print(f"Our cards : {sum(self.player_list)} You wins! Computer : {sum(self.computer_list)}")
            print(self.cash.append(1000), f"our cash : {sum(self.cash)}$!")
            return True
        elif sum(self.player_list) > 21 and sum(self.computer_list) > 21:
            print(f"Our cards : {sum(self.player_list)} Draw! No winner! Computer : {sum(self.computer_list)}")
            print(f"our cash returned ! {sum(self.cash)}$")
            return True

class player:
    def __init__(self ,name ,hiden_word ,list_wrong_gussess ,list_right_gussess ,letter ,score ,start):
        self.name = name
        self.hiden_word = hiden_word
        self.list_wrong_gussess = list_wrong_gussess
        self.list_right_gussess = list_right_gussess
        self.letter = letter
        self.score = score
        self.start =start

    def change_hiden_word(self):
        import random
        words = ["red", "blue", "green", "yellow", "black", "white"]
        word = random.choice(words)
        self.hiden_word = word

    def change_letter(self):
        letter = input("gosses a letter")
        self.letter = letter

    def print_hidden_word(self):
        print_hidden_word = ""
        for i in range(len(self.hiden_word)):
            flag = 0
            for y in self.list_right_gussess:
                if y == self.hiden_word[i]:
                    print_hidden_word += y
                    flag = 1
            if flag == 0:
                print_hidden_word += "*"
        return print_hidden_word

    def main_check_letter(self):
        if self.start == 1:
            player.change_hiden_word(self)
            self.start = 0

        if self.start == 0:
            print(player.print_hidden_word(self))
            player.change_letter(self)

        if self.letter in self.list_wrong_gussess:
            print("you did wrong in this letter")
            print(player.print_hidden_word(self))

        elif self.letter in self.list_right_gussess:
            print("you did right in this letter")
            print(player.print_hidden_word(self))

        elif self.letter not in self.hiden_word:
            print("you are wrong")
            self.list_wrong_gussess += self.letter
            print(player.print_hidden_word(self))

        elif self.letter in self.hiden_word:
            print("good")
            self.list_right_gussess += self.letter
            self.score += 1
            print(player.print_hidden_word(self))

        check_win = player.print_hidden_word(self)
        if "*" not in check_win:
            print(self.score, self.name)
            self.start = 1
            self.list_wrong_gussess = ""
            self.list_right_gussess = ""


player1 = player("", "", "", "", "", 0, 1)
player2 = player("", "", "", "", "", 0, 1)

while player1.score != 10 and player2.score != 10:
  
    player.main_check_letter(player1)
    print("\n")

  
    player.main_check_letter(player2)
    print("\n")

print(player1.name, player1.score, player2.name, player2.score)
if player1.score > player2.score:
    print(player1.name, "you winnn")
elif player1.score < player2.score:
    print(player2.name, "you winnn")


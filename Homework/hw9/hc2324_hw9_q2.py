import random as r

class Die:
    def __init__(self, faces = 6):
        self.number_of_faces = faces
        self.curr_face_value = 0
    def __repr__(self):
        return self.curr_face_value
    def roll(self):
        self.curr_face_value = r.randint(1, self.number_of_faces)

class PigGamePlayer:
    def __init__(self, name):
        self.name = name
        self.die = Die()
        self.score = 0
    def play_turn(self):
        self.die.roll()
        self.score += int(self.die.__repr__())

class PigGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = PigGamePlayer(player1_name)
        self.player2 = PigGamePlayer(player2_name)
    def play(self):
        winner = False
        player = self.player1
        while winner == False:
            turn_score = 0
            seen_h = False
            print("\n" + player.name + "'s turn:")
            while  seen_h == False:
                player.play_turn()
                print("You rolled", int(player.die.__repr__()))
                curr_score = int(player.die.__repr__())
                if curr_score == 1:
                    seen_h = True
                    print("You scored " + str(turn_score) + " points this turn. Your total score is " + str(player.score))
                    if player.score >= 100:
                        print("\n" + player.name + " won!")
                        winner = True
                    if player == self.player1:
                        player = self.player2
                    else:
                        player = self.player1
                else:
                    turn_score += curr_score
                    print("Your score for this turn is: ", turn_score)
                    again = input("Roll again? (type 'r' for roll, or 'h' for hold): ")
                    if again == 'h':
                        seen_h = True
                        print("You scored "+ str(turn_score) + " points this turn. Your total score is "+ str(player.score))
                        if player.score>=100:
                            print("\n"+player.name+" won!")
                            winner = True
                        if player==self.player1:
                            player = self.player2
                        else:
                            player = self.player1

def main():
    name1 = input("Player #1, enter your name: ")
    name2 = input("Player #2, enter your name: ")
    game1 = PigGame(name1, name2)
    game1.play()

main()
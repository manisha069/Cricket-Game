import random

class UserBats:
    def __init__(self):
        self.score = 0
    
    def game(self):
        print("Enter '''QUIT''' to quit the game else enter number between 1-10")
        while True:
            mar=input()
            if mar == "QUIT":
                print("you have quit the game")
                break
            elif mar.isdigit():
                mark= int(mar)
                if mark > 10 or mark < 1:
                    print("INVALID INPUT, GAME CLOSED")
                    return 0
                else:
                    comp= random.randint(1, 10)
                    print("you chose : ", mark)
                    print("computer chose : ", comp)
                    if comp == mark:
                        print("USER OUT")
                        return self.score
                    self.score += mark
                    print("Your score : ", self.score)
                    print()
            else:
                print("INVALID INPUT, GAME CLOSED")
                return 0




class CompBats:
    def __init__(self):
        self.new_score = 0
    
    def game2(self, score):
        print("Enter '''QUIT''' to quit the game ")
        while True:
            mar=input()
            if mar == "QUIT":
                print("you have quit the game")
                break
            elif mar.isdigit():
                mark= int(mar)
                if mark > 10 or mark < 1:
                    print("INVALID INPUT, GAME CLOSED")
                    return 0
                else:
                    comp= random.randint(1, 10)
                    print("you chose : ", mark)
                    print("computer chose : ", comp)
                    if comp == mark:
                        print("COMPUTER OUT")
                        return self.new_score
                    self.new_score += comp
                    print("Computer's score : ", self.new_score)
                    if self.new_score > score:
                        print("COMPUTER WINS")
            else:
                print("INVALID INPUT, GAME CLOSED")
                return 0




# if __name__ == "__main__":
print("WELCOME! LETS PLAY!")
print()
print("Rules:\n 1. Player Bats first \n 2. Input a random number between 1-10\n 3. Batter will be considered OUT when both the batter and bowler have the same number")
print()

print("GET READY!")
x=UserBats()
m=x.game()
if m!=0:
    print("COMPUTER'S turn to bat")
    b=CompBats()
    n=b.game2(m)
    if m> n:
        print("USER WINS!!")
    else:
        print("COMPUTER WINS!!")
        
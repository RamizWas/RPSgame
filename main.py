import random


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = random.choice(self.moves)
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        return self.moves[(self.moves.index(self.my_move) + 1) % 3]


class HumanPlayer(Player):
    def move(self):
        while True:
            move_human = input("Choose rock, paper, or scissors: ").lower()
            if move_human in self.moves:
                return move_human
            elif move_human == 'exit':
                exit()


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def determine_winner(self, move1, move2):
        if ((move1 == 'rock' and move2 == 'scissors') or
                (move1 == 'scissors' and move2 == 'paper') or
                (move1 == 'paper' and move2 == 'rock')):
            self.score_player1 += 1
            return 'Player 1 wins!'
        elif move1 == move2:
            return 'It\'s a tie!'
        else:
            self.score_player2 += 1
            return 'Player 2 wins!'

    def play_round(self, round_num):
        move1 = self.player1.move()
        move2 = self.player2.move()

        result = self.determine_winner(move1, move2)

        print(f"\nRound {round_num}:\n")
        print(f"Player 1 chose: {move1}\nPlayer 2 chose: {move2}\n{result}")

        # Update and display the scores
        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)
        print(f"Scores: Player 1 ({self.score_player1}),"
              f" Player 2 ({self.score_player2})")

    def play_game(self):
        print("Rock, Paper, Scissors Game!\n")

        num_rounds = int(input("How many rounds do you want to play? "))

        for round_num in range(1, num_rounds + 1):
            self.play_round(round_num)

        print("\nGame Over!")
        print(f"Final Scores: Player 1 ({self.score_player1}),"
              f" Player 2 ({self.score_player2})")
        if self.score_player1 > self.score_player2:
            print("Player 1 wins the game!")
        elif self.score_player2 > self.score_player1:
            print("Player 2 wins the game!")
        else:
            print("The game ends in a tie!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([RandomPlayer(),
                                              ReflectPlayer(), CyclePlayer()]))
    game.play_game()

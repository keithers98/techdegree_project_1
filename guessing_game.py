import random
print("""
    ------------------------------------
    Welcome To The Number Guessing Game!
    ------------------------------------
                                        """)

def start_game():
    guess_count = 0
    def question():
        return int(input("Pick a number between 1 and 10  "))
    def raise_count(a_count):
        return a_count + 1
    a_guess = question()
    guess_count = raise_count(guess_count)
    random_num = random.randint(1,10)

    while a_guess != random_num:

        if  a_guess > 10:
            print("Oops! Try Again.")
            guess_count = raise_count(guess_count)
            a_guess = question()
            continue
        if a_guess < random_num:
            print("It's higher!")
            guess_count = raise_count(guess_count)
            a_guess = question()
        elif a_guess > random_num:
            print("It's lower!")
            guess_count = raise_count(guess_count)
            a_guess = question()
        else:
            break
    return guess_count

player_score = start_game()

high_score = 0

round_count = 1

def looser():
        print("You got it! It took you {} tries".format(player_score))
def winner():
        if round_count = 1:
            looser()
        else:
            print("You beat the HIGHSCORE! It took you {} round.".format(round_count))

def referee(score_in_question, high_score):
    if score_in_question > high_score:
        high_score = player_score
        return winner()
    elif score_in_question < high_score:
        return looser()


next_round = "y"
while next_round.lower() != "n":
    referee(player_score, high_score)
    next_round = input("Would you like to play again?  (Y)es or (N)o   ")
    if next_round.lower() != "n":
        round_count = round_count + 1
        print("The HIGHSCORE is {}, good luck!".format(high_score))
        start_game()
    else:
        break
else:
    print("GAMEOVER")

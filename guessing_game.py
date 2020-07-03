import random
import time
print("""
    -~~$$---##~~~++---##~~~$$---##~~~++-
    Welcome To The Number Guessing Game!
    -~~$$---##~~~++---##~~~$$---##~~~++-
                                        """)
def looser():
    print("You got it! It took you {} tries.".format(player_score))
def winner():
    if round_count <= 1 :
        looser()
        #print('looser helper')
    else:
        print("You beat the HIGHSCORE! It took you {} tries.".format(player_score))

def referee(score_in_question, score_to_beat):

    if score_in_question < score_to_beat:
        score_to_beat = score_in_question
        winner()
        #print("winner helper")
        return score_to_beat
    elif score_in_question > score_to_beat:
        looser()
        #print("looser helper")
        return score_to_beat
    else:
        return score_to_beatS

def start_game(current_score, count):
    if count != 1:
        print("The HIGHSCORE is {}, good luck!".format(current_score))

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

#high_score = 10
round_count = 1
player_score = 10
#there is a bug where if the highscore is 10 and the player score is 10 the highscore is then set to "NONE"
while True:
    high_score = player_score
    player_score = start_game(high_score, round_count)
    player_score = referee(player_score, high_score)
    next_round = input("Would you like to play again?  (Y)es or (N)o   ")
    if next_round.lower() != "n":
        round_count = round_count + 1
        continue

    else:
        end_message_list = ["Your HIGHSCORE is {}".format(high_score), "You played {} rounds!".format(round_count), "Please enter a quarter into your computer.","Waiting...", "Waiting...", "Just kidding!", "Thank you for playing."]
        for message in end_message_list:
            print(message)
            time.sleep(1)
        break

print("$$$$$$$$     GAMEOVER     $$$$$$$$")

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
    else:
        print("You beat the HIGHSCORE! It took you {} tries.".format(player_score))

def referee(score_in_question, score_to_beat):

    if score_in_question < score_to_beat:
        score_to_beat = score_in_question
        winner()
        return score_to_beat
    else:
        looser()
        return score_to_beat

def start_game(current_score, count):
    if count != 1:
        print("The HIGHSCORE is {}, good luck!".format(current_score))

    def question():
        return input("Pick a number between 1 and 10  ")

    def raise_count(a_count):
        return a_count + 1

    guess_count = 0
    random_num = random.randint(1,10)

    while True:
        a_guess = question()
        a_valid_response = [1,2,3,4,5,6,7,8,9,10]
        guess_count = raise_count(guess_count)
        try:
            a_guess = int(a_guess)
            if a_guess != random_num:
                if a_guess > 10 :
                    print("Oops, invalid response. That number was too large.")
                    continue
                elif a_guess < 0:
                    print("Oops, invalid response. That number was negative.")
                    continue
                elif a_guess < random_num:
                    print("It's higher!")
                    continue
                elif a_guess > random_num:
                    print("It's lower!")
                    continue
                else:
                    break
        except TypeError as ohno:
            #print("Uh-oh, {}".format(ohno))
            print("Uh-oh, something went wrong. Let's try again.")
        except ValueError as uho:
            print("Uh-oh, that wasn't a number. Lets try again.")
        else:
            break
    return guess_count

round_count = 1
player_score = 10
high_score = player_score

while True:
    player_score = start_game(high_score, round_count)
    high_score = referee(player_score, high_score)
    next_round = input('Enter "n" to quit, or type anything else to play again!')
    if next_round.lower() != "n":
        round_count = round_count + 1
        continue
    else:
        end_message_list = ["Your HIGHSCORE is {}!".format(high_score), "You played {} rounds!".format(round_count), "Please enter a quarter into your computer.","Waiting...", "Waiting...", "Just kidding!", "Thank you for playing."]
        for message in end_message_list:
            print(message)
            time.sleep(1)
        break

print("$#$#$#$#$    GAMEOVER    $#$#$#$#$")

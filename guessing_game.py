import random
print("""
    ------------------------------------
    Welcome To The Number Guessing Game! 
    ------------------------------------ 
                                        """)
#one_more_round = "y"

#while one_more_round.lower() != "n":

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
highscore = start_game()

print("You got it! It took you {} tries".format(highscore))
next_round = input("Would you like to play again?  (Y)es or (N)o   ")

if next_round.lower() != "n":
    print("The HIGHSCORE is {}, good luck!".format(highscore))
    start_game()
else:
    print("GAMEOVER")

    
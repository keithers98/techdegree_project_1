import random

def start_game():
    print("""
------------------------------------
Welcome To The Number Guessing Game! 
------------------------------------ 
                                    """)
    
    def question():
        return int(input("Pick a number between 1 and 10  "))
    a_guess = question()
    guess_count = 1
    random_num = random.randint(1,10)
    
    while a_guess != random_num:
        if a_guess < random_num: 
            print("It's higher!") 
            a_guess = question()
        elif a_guess > random_num:
            print("It's lower!")
            a_guess = question()
            continue
        else:
            print("You got it! It took you {} tries".format)
            break
    
start_game()
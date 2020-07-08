# Tech Degree Project
 My first Techdegree Project

 I only used information we learned in the videos. The only thing we didn't learn was the random method I used, and I did have to check the help(random) documentation to find a method that allowed me to pull a random number. I did this because even though we didn't learn about random specifically, we were informed how to use the help() function.

Otherwise I didn't use google, stack overflow, or anything else other than some peer response on review-my-project. I feel as if my while and if loops get a little messy, and I was having trouble with error handling because I created the entire program then went back to do the handling. It seemed like I approached the error handling wrong, do people incorporate error handling during or after they create a script?

"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""



    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()

>>>>>>>>>help(random)<<<<<<<<<<<<<

randint(self, a, b)                                                                                                                                                                   
     |      Return random integer in range [a, b], including both end points.  
randomGenerator = random.randint(1,10)                                                                                                                                                    
                                                                                                                                                                                   **************************************************************************  
 __getstate__(self)                                                                                                                                                                    
 Issue 17489: Since __reduce__ was defined to fix #759889 this is no longer called;
 we leave it here because it has been here since random was rewritten back in 2001 and why risk breaking something.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<     Interesting..


     |  __init__(self, x=None)                                                                                                                                                                
     |      Initialize an instance.                                                                                                                                                           
     |                                                                                                                                                                                        
     |      Optional argument x controls seeding, as for Random.seed().                                                                                                                       
     |                                                                                                                                                                                        
     |  __reduce__(self)                                                                                                                                                                      
     |      helper for pickle                                                                                                                                                                 
     |                                                                                                                                                                                        
     |  __setstate__(self, state)                                                                                                                                                             
***************************************************************************

#
# Python: 3.10.2
#
# Author: Jeff A
#
# Purpose: Nice and Mean game
#

def start(nice=0 ,mean=0 ,name=""):
    # get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it is not a new game, thank the player
        for playing again and continue with the game.
    """
    # meaning, if we do not aleady have this user's name,
    # then they ae a new player and we need to get their name
    if name != "":
        print("\nThank you fo playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name 



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation, will you be nice \nor mean? (N/M) \n>>>: ")
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger slaps you across \nthe face and storms off..")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()



def show_score(nice,mean,name):
    print ("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))



def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the vaiables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the varriables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    # Substitue the {} wildcards with you vaiable values
    print("\nNice Job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)


def lose(nice,mean,name):
    # Substitue the {} wildcards with you vaiable values
    print("\nAhh too bad, game over! \n{} your face is red from all the slappings.".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again> (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSorry to see you go!")
            quit()
        else:
            print("\nEnter ( Y ) forr 'YES' ( N ) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)




if __name__ == "__main__":
    start()

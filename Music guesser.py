import random
score = 0
print("Welcome to my quiz. The task is to name 10 of Juice Wrld's songs. You get two wrong answers, and if you pass that margin you lose. Good luck!")
    
def login(): #defines the function
    file = open("musicpass.txt", "r")
    password = file.read()
    userguess = input("Enter password for access: ")
    if password == userguess:
        print("Access Granted!")
        game(song)
        ransong()
    else:
        print("Access Denied!")
        login()

def ransong():
    with open("musicsongs.txt", "r") as file:
        content= file.read()
        words = content.splitlines()
  
    # print random string
    #print(random.choice(words))
    return words


def game(song):
    songlist = song
    guess=0
    score=0
    while guess != 2:
        usguess1 = input("Enter your choice here: ")
        if usguess1 in songlist:
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect, one more guess allowed")
            guess = guess + 1
    else:
        print("Incorrect, game over")
        print("Your score is:",score)
        print("Incorrect, no more guesses left.")
    while score != 10:
        print("Well done, you win!")



def main():
    login()
song=ransong()
main()

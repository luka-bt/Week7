# high low program thinks of a number 0 to 100 player has to guess the number and
# program responds with higher or lower has ten chances to create the number
import random
randomnum = int(random.randrange(0, 100))
a = 0
tries=0
if tries == 6:
    print("your out of guesses, the number was", a)
while a != randomnum and tries < 10:
    tries= tries + 1
    a = int(input("take a guess: "))

    if a == randomnum:
            print("correct")
    if a != randomnum:
        if (a > randomnum):
            print("try lower guess again: ")
        if (a < randomnum):
            print("try higher guess again: ")

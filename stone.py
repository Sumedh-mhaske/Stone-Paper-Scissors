import random

pl_wins = 0
comp_wins = 0
draw = 0
i = 1

while i <= 5:
    print()
    print("1 - Stone")
    print("2 - Paper")
    print("3 - Scissor")

    comp = random.randint(1,3)
    pl = int(input("Player select your option : ") )
    

    print("Computer Selects : ", comp)

    if pl == 1 and comp == 3:
        print("You wins...")
        pl_wins += 1
    elif comp == 1 and pl == 3:
        print("Computer wins...")
        comp_wins += 1
    elif pl > comp:
        print("You wins...")
        pl_wins += 1
    elif comp > pl:
        print("Computer wins...")
        comp_wins += 1
    elif pl == comp:
        print("Match draw...")
        draw += 1
    
    def show_result():
        print()
        print("Your wins: ", pl_wins)
        print("Computer wins: ", comp_wins)
        print("Match draws: ", draw)

    if pl_wins == 3:
        show_result()
        print("You wins the best of 5...")
        break
    elif comp_wins == 3:
        show_result()
        print("Computer wins the best of 5...")
        break

    i == 1


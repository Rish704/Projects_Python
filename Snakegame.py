def snake_Game():
    import random


    def game(comp, you):
        if comp == you:
            return None
        elif comp == 's':
            if you == 'w':
                return False
            elif you == 'g':
                return True
            elif comp == 'w':
            if you == 'g':
                return False
            elif you == 's':
                return True
        elif comp == 'g':
            if you == 's':
                return False
            elif you == 'w':
                return True


    print("Welcome to the Snake, Water and Gun game")
    tie, win, lose = 0, 0, 0
    n = int(input("Enter the number of rounds you want to play: "))
    for i in range(n):
        you = input("choose your entity Snake(s), Water(w) or Gun(g): ")
        randNo = random.randint(1, 3)
        if randNo == 1:
            comp = 's'
        elif randNo == 2:
            comp = 'w'
        elif randNo == 3:
            comp = 'g'
        a = game(comp, you)

        print("You chose", you)
        print("Computer chose", comp)
        if a == None:
            print("Tie")
            tir += 1
        elif a:
            print("You win")
            win += 1
        else:
            print("You lose")
            lose += 1
    if win>lose:
        print("You won the game")
        again = input("Press a to play again: ")
        if again == "a":
            snake_Game()
    elif win == lose:
        print("The game is draw.")
        again = input("Press a to play again: ")
        if again == "a":
            snake_Game()
    else:
        print("You lose the game")
        again = input("Press a to play again: ")
        if again == "a":
            snake_Game()
snake_Game()

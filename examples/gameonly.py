from src.game import Game

def main():
    
    if int(input("Do you want to add a seed? (0 for no, 1 for yes)\n")):
        seed = int(input("Please write the seed down as an integer. Best to make it more than 5 Digits.\n"))
        fixed_seed = True
    else:
        seed = 0
        fixed_seed = False
    
    game = Game(seed=seed, fixed_seed=fixed_seed)
    game.start()   

if __name__ == '__main__':
    main()
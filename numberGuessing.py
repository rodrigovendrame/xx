import random

attempts_list = []

def show_score(): 
    if not attempts_list:
        print('There is no high score yet')

    else: 
        print(f'The current high score is:' f'{min(attempts_list)}attempts')

def start_game():
    attempts = 0
    random_num = random.randint(1, 10)
    print('Let`s play a game!')
    player_name = input('What is your name?')
    lets_play = input( f'Hello, {player_name}, would you like to play'
                      f'the Guessing Game? (Enter: Yes/No):')
    
    if lets_play.lower() != 'yes': 
        print('That`s what i`m talking about!')
        exit()

    else: 
        show_score()

    while lets_play.lower() == 'yes':
        try: 
            guess = int(input('Pick a number between 1 and 10:'))
            if guess < 1 or guess > 10:
                raise ValueError('Are you dumb? I told you to choose between 1 and 10 you dumbass!')
            
            attempts += 1
            attempts_list.append(attempts)

            if guess == random_num:
                print('Finally someone worth of my attention!')
                print(f'It only took you {attempts} attempts!')
                lets_play = input('Wanna play again? (Enter: Yes/No):')
                
                if  lets_play.lower() != 'yes':
                    print('Coward!')
                    break

                else:
                    attempts = 0
                    random_num = random.randint(1, 10)
                    show_score()
                    continue

            else: 
                if guess > random_num:
                    print('It`s lower!')
                elif guess < random_num:
                    print('It`s higher!')

        except ValueError as err:
            print('Not a valid value. Try again dumbass. ')
            print(err)

if __name__ == '__main__':
    start_game()
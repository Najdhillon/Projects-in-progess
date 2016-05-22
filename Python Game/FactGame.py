# Game where you answer trivia question true or False
from pip._vendor.distlib.compat import raw_input

global score
score = 0

def begin_game():
    print('Here are the rules:')
    print ('Everyone starts with zero')
    print('Answer all questions with either true or false')
    print('Most important rule, have fun!')
    print()

def begin():
    print('Welcome! Ready to test what is fact or not?')
    name = raw_input("What is your name:")
    print('Welcome,' +name+' !')
    
    start = raw_input('Are you ready play? (yes or no)')
    if start == 'yes':
        print('Let get started!')
        begin_game()
    elif start == 'no':
        print('Thanks for stopping by!')
        
    print()
        
def game():
    score = 0
    print('Question 1: Honey is the only food that does not spoil')
    question = raw_input('Is it true or false?')
    if question == 'true':
        new_score = score + 10
        score = new_score
        print(score)
    else:
        new_score = score - 10
        score = new_score
        print('Oh soooo close')
        print(score)
        
    print('Question 2: An ostrich\'s eye is bigger than it\'s brain')
    question = raw_input('Is it true or false?')
    if question == 'true':
        new_score = score + 10
        score = new_score
        print(score)
    else:
        new_score = score - 10
        score = new_score
        print('Oh soooo close')
        print(score)
        
    print('Question 3: Hummingbirds are the only animals that cannot fly backwards')
    question = raw_input('Is it true or false?')
    if question == 'true':
        new_score = score - 10
        score = new_score
        print('Wrong, but amazing right?')
        print(score)
    else:
        new_score = score + 10
        score = new_score
        print(score)
        
    print('Question 4: The lighter was invented ten years before the match was')
    question = raw_input('Is it true or false?')
    if question == 'true':
        new_score = score + 10
        score = new_score
        print(score)
    else:
        new_score = score - 10
        score = new_score
        print('Oh soooo close')
        print(score)
    
    print('Question 5: It is possible to tickle yourself')
    question = raw_input('Is it true or false?')
    if question == 'true':
        new_score = score - 10
        score = new_score
        print('Wrong')
        print(score)
    else:
        new_score = score + 10
        score = new_score
        print(score)
        
    print()    
    print('Congratulation, you are done!')
    print('Here is your total score:')
    print(score)
    
    print()
    game_again = raw_input('Do you want to play again? (yes,no)')
    if game_again == 'yes':
        game()
    else:
        print('Thanks for playing. Have a nice day')
        
def main():
    begin()
    begin_game()
    game()

main()
import picture
import random
class Hangman:
    def __init__(self,word_list):
        self.word_list=word_list
        self.reset_word()

    def reset_word(self):
        self.word_original=random.choice(self.word_list)
        self.word=self.word_original.lower()
        self.hidden_word=['_']* len(self.word)
        self.max_attempts=6
        self.guessed_letters=set()
        
    def guess_letter(self,letter):
        letter=letter.lower()
        if letter in self.guessed_letters:
            print('This letter has already been guessed.\nTry another letter')
            return
        if letter in self.word:
            self.guessed_letters.add(letter)
            for i,char in enumerate(self.word):
                if char == letter:
                    self.hidden_word[i]=letter
            print('Correct Guess',' '.join(self.hidden_word),sep='\n')
        else:
            self.max_attempts-=1
            print('Incorrect Guess')
            if self.max_attempts>0:
                print(f'You still have {self.max_attempts} chances to guess the word')
                
    def play(self):
        print('Lets play Hangman Game'.center(80,'*'),'GOOD LUCK!',80*'_',sep='\n')
        while True:
            self.reset_word()
            print(f'The word is {len(self.word)} letters long')
            picture.pic(0)
            print('You will be given 6 chances to guess the word')
            invalid_guess=0
            while self.max_attempts>0 and '_' in self.hidden_word and invalid_guess<3:
                try:
                    user_input=input('Guess the letter: ').strip()
                    if user_input.isalpha() and len(user_input)==1:
                        self.guess_letter(user_input)
                        invalid_guess=0
                    else:
                        invalid_guess+=1
                        print('Your input is invalid.\nTry again with a valid input')
                        continue
                    picture.pic(6-self.max_attempts)
                except KeyboardInterrupt:
                    print('Game Interrupted! Exiting...')
                    return
                except EOFError:
                    print('Input stream closed. Exiting the game...')
                    return
                except Exception as e:
                    print(f'An unexpected error occured: {e}')
            print("Game Over")
            if '_' not in self.hidden_word:
                print('You won the game!')
            else:
                print('You lose the game!')
            print(f'The correct word was: {self.word_original}')
            print("*"*80)
            while True:
                try:
                    play_again=input("Do you want to play again? (yes/no)").strip().lower()
                    valid_inputs=['yes','y','no','n']
                    if play_again not in valid_inputs:
                        print('Invalid input.Please enter yes or no')
                    elif play_again in valid_inputs[:2]:
                        break
                    else:
                        print("Thank you for playing hangman.")
                        return
                except KeyboardInterrupt:
                    print('Game Interrupted! Exiting...')
                    return
                except EOFError:
                    print('Input stream closed. Exiting the game...')
                    return
                except Exception as e:
                    print(f'An unexpected error occured {e}')
                    
            
if __name__=='__main__':
    word_list=['Apple','Banana','CustardApple','DragonFruit']
    game=Hangman(word_list)
    game.play()

import re
import random
import sys

a = '''  
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/              '''
print()
print(a)

HANGMANPICS = [
    '''

    
 =========''', '''

        +
        |
        |
        |
        |
        |
 =========''', '''

      --+
        |
        |
        |
        |
        |
 =========''''''

    +---+
        |
        |
        |
        |
        |
 =========''',
    '''

    +---+
    |   |
        |
        |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
 =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']

stri = '''
Babylonian
babysitter
backbiting
background
backpacker
backslider
backsplash
backstroke
bacteritic
baggageman

Bainbridge
balderdash
Balderrama
Ballentine
ballistics
ballplayer
balneology
balustrade
Bangladesh
banishment
bankruptcy
baptistery
Baranowski
barbershop

barnburner
Barrentine
Barrientes
Barrientez
Barrientos
Barrington

baseballer
basketball

Batchelder
bathometer
batrachian
battlement
battleship
Baumgarten
beatboxing
Beauchemin
Beauregard
bedchamber
beekeeping
beforehand
behavioral
believable
bellwether
belongings

benefactor
beneficent
benevolent
Bennington
benzofuran
Bernadetta
Bernadette
Bernardini
Bernardino
Berthiaume
besprinkle
Bessarabia
Betancourt
Betelgeuse
betweenane
Bevilacqua
bewitching
bichloride

Billington
bilocation
bimetallic
binariness
binoculars
biogenesis
biographer
biological
biometrics
biophysics
bipedalism
Birchfield
Birmingham
birthplace
bischofite
bishoprick
bismuthine
bisulphide
bizarrerie
blackberry
blackboard
blackfella
blackguard
Blackledge
Blackshear
Blackshire
blacksmith
Blackstock
Blackstone
Blanchette
blancmange
Blasingame
blogophile
bloodhound
bloodstain
Bloodworth ceilometer
celebrated
cellophane
cemeterial
censorship
centimeter
centimetre
centralise
centralism
centralize
Chadbourne
chalcedony
chalkstone
challenger
Chamberlin
chancellor
Chancellor
chanciness
chandelier
changeable
changeless
charioteer
Charleston
Charmander
Chautauqua
chauvinism
cheapskate
cheatsheet
Cheboksary
checkpoint
cheeseball
chemocline
chequebook
Chichester

childlover
childproof
chimerical
chimpanzee
chinchilla
chirognomy
chiromancy
Chittenden
chlorinity
chlorosity
chlorvinyl
Christabel
Christiana
Christiano
Christmasy
chromicize
chromocyte
chromosome
Chronister
chronogram
chronology
chuckwagon
chumbucket
chupacabra
churchgoer
Churchwell
churchyard
ciguatoxin
Cincinnati
Cinderella
circularly'''


def get_the_word(stri):
    '''
    retuns random word
    '''
    words = stri
    reg = re.compile('[^a-zA-Z ]')
    words = list(set(reg.sub(' ', stri).lower().split()))
    for word in words:
        if len(word) < 10:
            words.remove(word)
    word_ind = random.randint(0, len(words) - 1)
    return words[word_ind]


def display_board(HANGMANPICS, missed_letters, correct_letters, secret_word):
    print(HANGMANPICS[len(missed_letters)])
    print()

    print('Used wrong letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '*' * len(secret_word)
    # changing * for  letters
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
    # showing the guessed word with spaces between the letters
    for letter in blanks:
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # returns the letter which enters player
    # checks the letter is not other symbol
    while True:
        guess = input('Enter the letter\n')
        guess = guess.lower()
        if len(guess) != 1:
            print('Your letter is wrong!')
        elif guess in already_guessed:
            print('You already used this letter. Try another one')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter english alphabet letter')
        else:
            return guess


missed_letters = ''
correct_letters = ''
secret_word = get_the_word(stri)
game_is_done = False

while True:
    display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
    # calculate the amount of letters which are entered
    print('You have', str(10 - len(missed_letters)), 'guesses')
    guess = get_guess(missed_letters + correct_letters)
    if guess in secret_word:
        print("You guessed the letter!")
        correct_letters = correct_letters + guess

        # check the wining condition
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('Great!Congratulations!!! It was a word "', secret_word, '"! You are winner!')
            game_is_done = True
    else:
        print("You didn't guess the letter!")
        missed_letters = missed_letters + guess
        # check the losing condition
        if len(missed_letters) == len(HANGMANPICS)-1:
            display_board(HANGMANPICS, missed_letters, correct_letters, secret_word)
            print('You have no tries!\nafter', str(len(missed_letters)), 'mistakes', str(len(correct_letters)),
                  'guessed letters. the word is:', secret_word + '"')
            game_is_done = True


    if game_is_done:
        print("Game Over")
        break



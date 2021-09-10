import random

frases = ['Learn as if you will live forever live like you will die tomorrow', 'When you give joy to other people you get more joy in return', 'The initial and the most difficult risk that we need to take is to become honest',
'It is better to fail in originality than to succeed in imitation', 'The optimist sees opportunity in every difficulty', 'Education is the most powerful weapon which you can use to change the world',
'Alone we can do so little but together we can do so much', 'Just one small positive thought in the morning can change your whole day',
'It is never too late to be what you might have been', "Don't let someone else's opinion of you become your reality"]

palabras = []

oracion = []

guesses = []

cont = 0

for oraciones in frases:

    oracion = oraciones.split()

    for palabra in oracion:
        palabras.append(palabra)

secret_answer = random.choice(frases)

respuesta = secret_answer.split()

random.shuffle(palabras)

print('WELCOME TO THE GUESSING GAME!!!!!!')

while True:

    print(f' \n {palabras}')

    guess = input(
        f' \n PLEASE ENTER A WORD SO YOU CAN GUESS THE PHRASE . THE PHRASE HAS {len(respuesta)} WORDS. ENTER "S" TO EXIT:')

    if guess == "s" or guess == "S":
        print('\n THANKS FOR PLAYING. GOOD BYE :D')
        input('PRESS ENTER TO QUIT')
        break

    for num in range(len(palabras)):

        if guess == palabras[num] and guess not in respuesta:

            palabras.pop(num)

            break

        else:

            continue

    if guess == respuesta[cont]:

        guesses.append(guess)

        cont += 1

        print('\n CONGRATULATIONS! YOU FOUND THE CORRECT WORD')
        print(f' \n CORRECT GUESSES UNTIL NOW ARE: {guesses}')

    else:

        print('\n ALMOST... BUT NOT QUITE. PLEASE CHOOSE A DIFFERENT WORD')

        print(f' \n YOU HAVE {len(respuesta) - len(guesses)} WORDS TO UNCOVER')
        print(f' \n CORRECT GUESSES UNTIL NOW ARE: {guesses}')

        continue

    if guesses == respuesta:
        print('\n CONGRATULATIONS!!!!! YOU WON')

        print(f' \n THE SECRET PHRASE WAS: {secret_answer}')

        print('\n THANKS FOR PLAYING')

        input('PRESS ENTER TO QUIT' )

        break


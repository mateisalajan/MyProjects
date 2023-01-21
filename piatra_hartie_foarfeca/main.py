import random


def main():
    ok = True
    while ok:
        lst = ['piatra', 'hartie', 'foarfeca']
        lst2 = ['Palyer1', 'Player2']
        throw1 = random.choice(lst)
        throw2 = random.choice(lst)

        winner = None
        if throw1 == 'piatra' and throw2 == 'hartie':
            winner = lst2[1]
        elif throw1 == 'piatra' and throw2 == 'foarfeca':
            winner = lst2[0]
        elif throw1 == 'piatra' and throw2 == 'piatra':
            winner = 'Egalitate'

        if throw1 == 'hartie' and throw2 == 'foarfeca':
            winner = lst2[1]
        elif throw1 == 'hartie' and throw2 == 'piatra':
            winner = lst2[0]
        elif throw1 == 'hartie' and throw2 == 'hartie':
            winner = 'Egalitate'

        if throw1 == 'foarfeca' and throw2 == 'piatra':
            winner = lst2[1]
        elif throw1 == 'foarfeca' and throw2 == 'hartie':
            winner = lst2[0]
        elif throw1 == 'foarfeca' and throw2 == 'foarfeca':
            winner = 'Egalitate'

        print(f'Player1: {throw1}\nPlayer2: {throw2}\nCastigator: {winner}')

        play_again = input("Play again? yes/no: ")
        if play_again == 'yes':
            ok = True
        elif play_again == 'no':
            ok = False


if __name__ == '__main__':
    main()

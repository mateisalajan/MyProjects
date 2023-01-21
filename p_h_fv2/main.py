
from Actions import Action
from Functions import get_user_selection, get_computer_selection, determine_winner


def main():
    while True:
        try:
            user_action = get_user_selection()
        except ValueError as e:
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Valoarea data nu apartine intrevalului: {range_str}")
            continue

        computer_action = get_computer_selection()
        determine_winner(user_action, computer_action)
        play_again = input("Play again? yes/no: ")
        if play_again.lower() != 'yes':
            break


if __name__ == '__main__':
    main()

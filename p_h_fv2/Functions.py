import random

from Actions import Action


victories = {
    Action.Piatra: [Action.Foarfeca],
    Action.Hartie: [Action.Piatra],
    Action.Foarfeca: [Action.Hartie]
}


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Dati o alegere ({choices_str}): "))
    action = Action(selection)
    return action


def get_computer_selection():
    selection = random.randint(1, len(Action) - 1)
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Amandoi jucatorii au ales {user_action.name}.Egalitate!")
    elif computer_action in defeats:
        print(f"{user_action.name} bate {computer_action.name}.Ai castigat!")
    else:
        print(f"{computer_action.name} bate {user_action.name}.Ai pierdut!")

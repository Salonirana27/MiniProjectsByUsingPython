import random


def get_computer_choice():
    return random.choice(["s", "w", "g"])


def get_choice_name(choice):
    choices = {"s": "Snake", "w": "Water", "g": "Gun"}
    return choices.get(choice, "Invalid")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 0

    if (user_choice == "s" and computer_choice == "w") or \
       (user_choice == "w" and computer_choice == "g") or \
       (user_choice == "g" and computer_choice == "s"):
        return 1

    return -1


def main():
    print("Welcome to Snake-Water-Gun!")
    print("Choose: s = Snake, w = Water, g = Gun")

    while True:
        rounds_input = input("How many rounds do you want to play? ").strip()
        if rounds_input.isdigit() and int(rounds_input) > 0:
            rounds = int(rounds_input)
            break
        print("Please enter a positive whole number.")

    user_score = 0
    computer_score = 0
    draws = 0

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}/{rounds}")

        while True:
            user_choice = input("Your move: ").strip().lower()
            if user_choice in ["s", "w", "g"]:
                break
            print("Invalid choice. Please enter s, w, or g.")

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)

        print(f"You chose: {get_choice_name(user_choice)}")
        print(f"Computer chose: {get_choice_name(computer_choice)}")

        if result == 0:
            draws += 1
            print("It's a draw!")
        elif result == 1:
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

    print("\nGame Over!")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    print(f"Draws: {draws}")

    if user_score > computer_score:
        print("You won the game!")
    elif computer_score > user_score:
        print("Computer won the game!")
    else:
        print("The game ended in a draw!")


if __name__ == "__main__":
    main()

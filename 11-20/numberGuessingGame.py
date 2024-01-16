from random import randint

EASY = 10
HARD = 5

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY
    else:
        return HARD

def checking_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You win! The answer was {answer}.")
        return 0  # Return 0 to signal that the game is won
    return turns - 1

def game():
    print("Welcome to a number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns = difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        turns = checking_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif turns > 0:
            print("Guess again.")

game()

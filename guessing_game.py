import random
computer = random.randint(1,50)
print("""
  === Welcome to the Guessing Game! ===
I am thinking of a number between 1 and 50.
You have 5 attempts to guess it. Good luck!
""")
for x in range(1,6):
    guess = int(input(f"Attempt {x}/5\n -> Enter your guess:\n -->"))
    if guess > computer:
       print ("\nToo high! Try a lower number.")
    elif guess < computer:
       print("\nToo low! Try a higher number.")
    else:
       print(f"🎉 Congratulations!\nYou guessed the secret number in {x} attempts! 🎉")
       break
    print("_____**______")
else:
    print(f"\nGame Over! You've run out of attempts.\nThe secret number was:\n{computer}\n Better luck next time!")

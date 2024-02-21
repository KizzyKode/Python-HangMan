import random
import tkinter as tk

def play_hangman():
    words = ["apple", "banana", "cherry", "durian", "elderberry"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    def guess_letter():
        guess = letter_entry.get().lower()
        letter_entry.delete(0, tk.END)

        if guess in guessed_letters:
            info_label.config(text="You've already guessed that letter. Try again.")
            return

        if len(guess) != 1 or not guess.isalpha():
            info_label.config(text="Invalid input. Please enter a single letter.")
            return

        guessed_letters.append(guess)

        if guess in secret_word:
            info_label.config(text="Good guess!")
        else:
            attempts_left = attempts - len([x for x in guessed_letters if x not in secret_word])
            info_label.config(text="Wrong guess. You have {} attempts left.".format(attempts_left))
            hangman_canvas.itemconfig(parts[6-attempts_left], state=tk.NORMAL)

        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        word_label.config(text=display_word)

        if display_word == secret_word:
            info_label.config(text="Congratulations! You guessed the word: " + secret_word)

        if attempts - len([x for x in guessed_letters if x not in secret_word]) == 0:
            info_label.config(text="Game over! You ran out of attempts.")
            word_label.config(text=secret_word)

    # Create GUI window
    window = tk.Tk()
    window.title("Hangman")

    # Hangman parts
    hangman_canvas = tk.Canvas(window, width=200, height=200)
    hangman_canvas.pack()

    parts = []
    parts.append(hangman_canvas.create_line(40, 190, 160, 190, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_line(100, 190, 100, 20, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_line(100, 20, 170, 20, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_line(170, 20, 170, 40, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_oval(150, 40, 190, 80, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_line(170, 80, 170, 140, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_line(170, 100, 130, 90, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_line(170, 100, 210, 90, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_line(170, 140, 140, 170, state=tk.HIDDEN))
    parts.append(hangman_canvas.create_line(170, 140, 200, 170, state=tk.HIDDEN))

    # Word label
    word_label = tk.Label(window, text="_ " * len(secret_word), font=("Arial", 14))
    word_label.pack(),

    # Letter entry
    letter_entry = tk.Entry(window)
    letter_entry.pack()

    # Guess button
    guess_button = tk.Button(window, text="Guess", command=guess_letter)
    guess_button.pack()


    # Info label
    info_label = tk.Label(window, text="Welcome to Hangman! Guess the secret word. You have {} attempts.".format(attempts))
    info_label.pack()

    def close_window():
        window.destroy()

    # Quit button
    quit_button = tk.Button(window, text="Quit", command=close_window)
    quit_button.pack()

    def reset_game():
        nonlocal secret_word, guessed_letters, attempts
        secret_word = random.choice(words)
        guessed_letters = []
        attempts = 6
        info_label.config(text="Welcome to Hangman! Guess the secret word. You have {} attempts.".format(attempts))
        word_label.config(text="_ " * len(secret_word))
        hangman_canvas.itemconfig(parts[6], state=tk.HIDDEN)
        for i in range(1, 6):
            hangman_canvas.itemconfig(parts[i], state=tk.HIDDEN)

    # Reset button
    reset_button = tk.Button(window, text="Reset", command=reset_game)
    reset_button.pack()

    # Start the game
    window.mainloop()

# Start the game
play_hangman()
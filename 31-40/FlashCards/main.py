from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    if data.empty:
        raise pandas.errors.EmptyDataError("No columns to parse from file")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    # Handle empty file (create default data or show an error message)
    print("The file 'data/words_to_learn.csv' is empty or missing columns.")
    to_learn = []  # Provide a default value or handle it based on your requirements
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    if to_learn:
        current_card = random.choice(to_learn)
        print("Current French word:", current_card["French"])  # Debugging line
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        flip_timer = window.after(3000, func=flip_card)
    else:
        print("No more cards to learn.")



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    global to_learn, current_card
    if current_card in to_learn:
        to_learn.remove(current_card)
        print(len(to_learn))
        updated_data = pandas.DataFrame(to_learn)
        updated_data.to_csv("data/words_to_learn.csv", index=False)
        next_card()
    else:
        print("Current card not found in to_learn list.")



window = Tk()
# Rest of the code...

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

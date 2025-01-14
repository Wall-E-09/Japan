import random
import pandas as pd
import tkinter as tk

hiragana_df = pd.read_csv(r'C:\Users\Home\Documents\GitHub\Japan\data\japanese_hiragana.csv')
katakana_df = pd.read_csv(r'C:\Users\Home\Documents\GitHub\Japan\data\japanese_katakana.csv')

def alphabet_random_symbols ():
    index_of_symbols = random.randint(1, 45)
    hiragana_symbol = hiragana_df.loc[index_of_symbols, "Hiragana"]
    hiragana_romaji = hiragana_df.loc[index_of_symbols, "Romaji"]
    katakana_symbol = katakana_df.loc[index_of_symbols, "Katakana"]
    katakana_romaji = katakana_df.loc[index_of_symbols, "Romanji"]
    #print(f"Hiragana: {hiragana_symbol} ({hiragana_romaji})")
    #print(f"Katakana: {katakana_symbol} ({katakana_romaji})")
    return hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji

def display_symbols(hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji):

    root = tk.Tk()
    root.geometry("")
    root.option_add("*Font", "Helvetica 100")
    root.title("Japanese Symbols")

    hiragana_label = tk.Label(root, text=f"Hiragana: {hiragana_symbol} ({hiragana_romaji})")
    hiragana_label.pack()

    katakana_label = tk.Label(root, text=f"Katakana: {katakana_symbol} ({katakana_romaji})")
    katakana_label.pack()

    root.mainloop()
    
def get_user_input():
    hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji = alphabet_random_symbols()
    user_input = input(f"Enter the romaji for {hiragana_symbol} or {katakana_symbol}: ")

    return user_input

def train_romaji(hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji):
    #user_input = get_user_input()

    root = tk.Tk()
    root.geometry("")
    root.option_add("*Font", "Helvetica 100")
    root.title("Romaji Training")

    prompt_label = tk.Label(root, text=f"Enter the romaji for {hiragana_symbol} or {katakana_symbol}:")
    prompt_label.pack()

    entry = tk.Entry(root, font=("Helvetica", 50))
    entry.pack()

    result_label = tk.Label(root, text="", font=("Helvetica", 50))
    result_label.pack()
    
    submit_button = tk.Button(root, text="Submit", command=lambda: check_answer(hiragana_romaji, katakana_romaji, result_label, entry))
    submit_button.pack()

    root.mainloop()

def check_answer(hiragana_romaji, katakana_romaji, result_label, entry):
    entered_text = entry.get()
    #if user_input.lower() == hiragana_romaji.lower() or user_input.lower() == katakana_romaji.lower():
        #result_label.config(text="Correct!", fg="green")
    #else:
        #
        # result_label.config(text="Incorrect. Try again.", fg="red")

    if entered_text == hiragana_romaji or entered_text == katakana_romaji:
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect, try again.", fg="red")

def main():
    hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji = alphabet_random_symbols()
    display_symbols(hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji)
    train_romaji(hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji)

if __name__ == "__main__":
    main()

#alphabet_random_symbols()

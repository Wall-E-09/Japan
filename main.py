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

def display_symbols():
    hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji = alphabet_random_symbols()

    root = tk.Tk()
    root.geometry("")
    root.option_add("*Font", "Helvetica 100")
    root.title("Japanese Symbols")

    hiragana_label = tk.Label(root, text=f"Hiragana: {hiragana_symbol} ({hiragana_romaji})")
    hiragana_label.pack()

    katakana_label = tk.Label(root, text=f"Katakana: {katakana_symbol} ({katakana_romaji})")
    katakana_label.pack()

    root.mainloop()

def train_romaji():
    hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji = alphabet_random_symbols()
    user_input = check_answer()

def check_answer():
    hiragana_symbol, hiragana_romaji, katakana_symbol, katakana_romaji = alphabet_random_symbols()
    user_input = entry.get()
    if user_input.lower() == hiragana_romaji.lower() or user_input.lower() == katakana_romaji.lower():
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect. Try again.", fg="red")

    root = tk.Tk()
    root.geometry("")
    root.option_add("*Font", "Helvetica 100")
    root.title("Romaji Training")

    prompt_label = tk.Label(root, text=f"Enter the romaji for {hiragana_symbol} or {katakana_symbol}:")
    prompt_label.pack()

    entry = tk.Entry(root, font=("Helvetica", 50))
    entry.pack()

    submit_button = tk.Button(root, text="Submit", command=check_answer)
    submit_button.pack()

    result_label = tk.Label(root, text="", font=("Helvetica", 50))
    result_label.pack()

    root.mainloop()

    return user_input


def main():
    display_symbols()
    train_romaji()

#alphabet_random_symbols()

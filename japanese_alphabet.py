import pandas as pd

hiragana_data = {
    "Hiragana": [
        "あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ",
        "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ",
        "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", "ん",
        
    ],
    "Romaji": [
        "a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so",
        "ta", "chi", "tsu", "te", "to", "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho",
        "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "wo", "n",
        
    ],
    "Type": 
        ["Hiragana"] * 46 
}
katakana_data = {
    "Katakana": [
        "ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ", "サ", "シ", "ス", "セ", "ソ",
        "タ", "チ", "ツ", "テ", "ト", "ナ", "ニ", "ヌ", "ネ", "ノ", "ハ", "ヒ", "フ", "ヘ", "ホ",
        "マ", "ミ", "ム", "メ", "モ", "ヤ", "ユ", "ヨ", "ラ", "リ", "ル", "レ", "ロ", "ワ", "ヲ", "ン"
    ],
    "Romanji": [
        "a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so",
        "ta", "chi", "tsu", "te", "to", "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho",
        "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "wo", "n"
    ],
    "Type": 
        ["Katakana"] * 46
}

basic_words_data = {
    "Word": ["こんにちは", "ありがとう", "さようなら", "すみません", "はい", "いいえ", "おはよう", "おやすみ", "おいしい", "たべる"],
    "Romaji": ["konnichiwa", "arigatou", "sayounara", "sumimasen", "hai", "iie", "ohayou", "oyasumi", "oishii", "taberu"],
    "Meaning": ["Hello", "Thank you", "Goodbye", "Excuse me/Sorry", "Yes", "No", "Good morning", "Good night", "Delicious", "To eat"]
}

basic_kanji_data = {
    "Kanji": ["日", "月", "火", "水", "木", "金", "土", "山", "川", "田"],
    "Onyomi": ["nichi", "getsu", "ka", "sui", "moku", "kin", "do", "san", "sen", "den"],
    "Kunyomi": ["hi", "tsuki", "hi", "mizu", "ki", "kane", "tsuchi", "yama", "kawa", "ta"],
    "Meaning": ["Day/Sun", "Month/Moon", "Fire", "Water", "Wood/Tree", "Gold/Money", "Earth", "Mountain", "River", "Field"]
}

hiragana_df = pd.DataFrame(hiragana_data)
katakana_df = pd.DataFrame(katakana_data)
basic_words_df = pd.DataFrame(basic_words_data)
basic_kanji_df = pd.DataFrame(basic_kanji_data)

hiragana_df.to_csv(r'C:\Users\Home\Documents\GitHub\Japan\data\japanese_hiragana.csv', index=False)
katakana_df.to_csv(r'C:\Users\Home\Documents\GitHub\Japan\data\japanese_katakana.csv', index=False)
basic_words_df.to_csv(r'C:\Users\Home\Documents\GitHub\Japan\data\basic_words.csv', index=False)
basic_kanji_df.to_csv(r'C:\Users\Home\Documents\GitHub\Japan\data\basic_kanji.csv', index=False)

def alphabet_learning():
    while True:
        try:
            num_symbols = int(input_symbols)
            if num_symbols > 0:
                print("Hiragana symbols:")
                print(hiragana_df.sample(n=num_symbols).to_string(index=False))
                print("\nKatakana symbols:")
                print(katakana_df.sample(n=num_symbols).to_string(index=False))
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number or 'quit' to exit.")
        print ("Time to learn alphabet: ")

        input_symbols = input("Input number of symbols: ")
        if input_symbols == 'quit':
            break

def random_symbols():
    for i in range(2):
        print (katakana_data)

random_symbols()
from tkinter import *
import tkinter.messagebox as messagebox

# Dictionary of languages and their translations
languages = {
"hausa": {
    "hello": "Sannu",
    "good morning": "Ina kwana",
    "good afternoon": "Ina wuni",
    "good evening": "Ina yamma",
    "how are you": "Lafiya lau?",
    "thank you": "Na gode",
    "please": "Don Allah",
    "yes": "Eh",
    "no": "A'a",
    "welcome": "Barka da zuwa",
    "goodbye": "Sai an jima",
    "friend": "Aboki",
    "food": "Abinci",
    "water": "Ruwa",
    "house": "Gida"
},
"edo": {
    "hello": "Kóyo",
    "good morning": "Ómóké",
    "good afternoon": "Ómókhùe",
    "good evening": "Ómóké n'ẹvbé",
    "how are you": "Mé rré?",
    "thank you": "Osé",
    "please": "Tó vbé",
    "yes": "Éé",
    "no": "Óó",
    "welcome": "Óghé",
    "goodbye": "Vbé ó",
    "friend": "Ókpá",
    "food": "Ẹ́khà",
    "water": "Amẹ́",
    "house": "Íyà"
    },
 "igala": {
    "hello": "Mẹ́hẹ̀",
    "good morning": "Ọ̀nẹ̀ ọ́ma",
    "good afternoon": "Ọ̀sán ọ́ma",
    "good evening": "Ọ̀yẹ̀ ọ́ma",
    "how are you": "Mẹ́hẹ̀ jẹ́?",
    "thank you": "Ojo",
    "please": "Mẹ́hẹ̀ gba",
    "yes": "Ẹẹ",
    "no": "Kò",
    "welcome": "Mẹ́hẹ̀ wa",
    "goodbye": "Ká fọ̀",
    "friend": "Ọ́rẹ́",
    "food": "Ọ̀nẹ̀",
    "water": "Ámi",
    "house": "Ilẹ̀",
    },
"fulani":{
    "hello": "Jam waali",
    "good morning": "Jam weeti",
    "good afternoon": "Jam weeti",
    "good evening": "Jam weeti",
    "how are you": "No mbada?",
    "thank you": "A jaaraama",
    "please": "Tiiɗno",
    "yes": "Eey",
    "no": "Alaa",
    "welcome": "Jam na",
    "goodbye": "Bisimilla",
    "friend": "Gorko",
    "food": "Ñamnde",
    "water": "Ndiyam",
    "house": "Wuro",
    "child": "Gorko ɗum",
    "man": "Gorko",
    "woman": "Debbo",
    "sun": "Naange",
    "moon": "Lewru"
},
"Zulu": {
        "hello": "sawubona",
        "goodbye": "hamba kahle",
        "please": "ngiyacela",
        "thank you": "ngiyabonga",
        "yes": "yebo",
        "no": "cha",
        "friend": "umngane",
        "family": "umndeni",
        "house": "indlu",
        "food": "ukudla",
        "water": "amanzi",
        "book": "incwadi",
        "school": "isikole",
        "work": "umsebenzi",
        "car": "imoto",
        "dog": "inja",
        "cat": "ikati",
        "love": "uthando",
        "city": "idolobha",
        "life": "impilo",
},}
def translate():
    selected_language = languages_var.get()
    word = word_entry.get().strip().lower()

    if selected_language in languages and word in languages[selected_language]:
        translation = languages[selected_language][word]
        messagebox.showinfo("Translation", f"{word} in {selected_language}: {translation}")
    else:
        messagebox.showwarning("Warning", "Word not found or language not supported.")


# Create the main window
root = Tk()
root.title("Multi-Language Translator")

# Create and pack widgets
Label(root, text="Enter an English word:").pack(pady=10)
word_entry = Entry(root, width=30)
word_entry.pack(pady=10)

# Dropdown for language selection
languages_var = StringVar(value="Select Language")
OptionMenu(root, languages_var, *languages.keys()).pack(pady=10)

# Button to trigger translation
Button(root, text="Translate", command=translate).pack(pady=20)

# Run the application
root.mainloop()



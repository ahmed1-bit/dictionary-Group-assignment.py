# Simple English to Yoruba Dictionary

dictionary = {
    "hello": "báwo",
    "good morning": "ẹ káàárọ̀",
    "good afternoon": "ẹ káàsán",
    "good evening": "ẹ káalẹ́",
    "thank you": "ẹ ṣé",
    "yes": "béèni",
    "no": "rárá",
    "food": "oúnjẹ",
    "water": "omi",
    "house": "ilé",
    "school": "ilé-èkó",
    "love": "ìfẹ́",
    "friend": "ọ̀rẹ́",
    "money": "owó",
    "father": "bàbá",
    "mother": "ìyá",
    "child": "ọmọ",
    "come": "wá",
    "go": "lọ",
    "sleep": "sùn"
}

print("English → Yoruba Dictionary")
print("Type 'exit' to stop\n")

while True:
    word = input("Enter an English word: ").lower()

    if word == "exit":
        print("Bye 👋")
        break

    if word in dictionary:
        print("Yoruba:", dictionary[word])
    else:
        print("Word not found 😕")
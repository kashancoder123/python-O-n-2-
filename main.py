import random

words = ["apple", "banana", "grape", "orange", "melon"]  # changed to list
word = random.choice(words)
scrambled = ''.join(random.sample(word, len(word)))

print(" 🔤 Welcome to Word Scramble! ")
print(f"Can you guess the word? Scrambled word: {scrambled}")

for attempt in range(3):  # 3 tries
    guess = input(f"Attempt {attempt + 1}: ").lower()
    if guess == word:
        print(" 🎉 Correct! You guessed the word.")
        break
    else:
        print(" ❌ Try again.")
else:
    print(f"😢 Out of tries! The word was '{word}'.")
from tqdm import tqdm

dictionary=[]
with open('words.txt','r') as file:
	for line in file:
		dictionary.append(line.strip())

results = dictionary.copy()
guess = []
badLetters = []


print("Which letters does the word not contain?")
print("Press space, if you're done.")
while True:
    badLetter = input()
    if badLetter == " ":
        break
    elif len(badLetter) != 1:
        print("Please type one letter per row")
    elif badLetter.isalpha() == False:
        print("Please type only letters")
    else:
        badLetters.append(badLetter)

wordGuess = input("Type your tested word, if it was correct, type the letter, and if it was incorrect, type a space: ")
wordLength = len(wordGuess)


for letter in range(wordLength):
    if wordGuess[letter] == " ":
        guess.append([])
    else:
        guess.append([wordGuess[letter]])

for word in tqdm(dictionary):
    if len(word) != wordLength:
        results.remove(word)
    else:
        for guessLetter in range(len(guess)):
            if word in results and len(guess[guessLetter]) != 0 and guess[guessLetter][0] != word[guessLetter] or len(guess[guessLetter]) != 0 and guess[guessLetter][0] in badLetters:
                results.remove(word)

print(results)
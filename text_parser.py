text=input("Enter a Text: ")
letters=[]

text.lower()
letters.append(input("1st letter: ").lower())
letters.append(input("2nd letter: ").lower())
letters.append(input("3rd letter: ").lower())

print("\n")
print("Letter Repeted")

let_rep1=text.count(letters[0])
let_rep2=text.count(letters[1])
let_rep3=text.count(letters[2])

print(f"the letter '{letters[0]}' is repeated {let_rep1} times")
print(f"the letter '{letters[1]}' is repeated {let_rep2} times")
print(f"the letter '{letters[2]}' is repeated {let_rep3} times")

print("\n")
print("Words In total")

words=text.split()
print(f"The total number of words are {len(words)}")

print("\n")
print("first and last letter")

first_letter=text[0]
last_letter=text[-1]

print(f"First letter is {first_letter} and last letter is {last_letter}")


print("\n")
print("Inverted Words")
words.reverse()
reversed_text=' '.join(words)
print(f"after inverting the text will be showed as {reversed_text}")

print("\n")
print("Is word 'python' in the text")
is_py='python' in text
dic={False:'No',True:'Yes'}
print(f"Is word 'python' in text {dic[is_py]}")






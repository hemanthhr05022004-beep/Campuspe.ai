# Taking input from user
sentence = input("Enter a sentence: ")

original = sentence
characters_with_spaces = len(sentence)
characters_without_spaces = len(sentence.replace(" ", " "))
words_list = sentence.split()
total_words = len(words_list)
uppercase = sentence.upper()
lowercase = sentence.lower()
title_case = sentence.title()
first_word = words_list[0] if total_words > 0 else ""
last_word = words_list[-1] if total_words > 0 else ""
reversed_sentence = sentence[::-1]

print("\nResults:")
print("Original:", original)
print("Characters (with spaces):", characters_with_spaces)
print("Characters (without spaces):", characters_without_spaces)
print("Words:", total_words)
print("UPPERCASE:", uppercase)
print("lowercase:", lowercase)
print("Title Case:", title_case)
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reversed_sentence)

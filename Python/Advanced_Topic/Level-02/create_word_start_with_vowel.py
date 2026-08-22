sentence = "Hey I am Nirmalya raja, Currently I am doing Coding for Innovate something"
words = sentence.split()

vowel_words = [word for word in words if word[0].lower() in "aeiou"]
print(f'The words which is starts with vowel are given: {list(vowel_words)}')


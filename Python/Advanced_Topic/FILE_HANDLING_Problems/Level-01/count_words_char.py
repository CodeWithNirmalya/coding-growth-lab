with open("demo_file.txt", "r") as f:
    sentence = 0
    word = 0
    char = 0

    for line in f:
        sentence += 1                  # counts lines, not sentences
        word += len(line.split())      # counts words
        char += len(line)              # counts characters (including spaces/newline)

print(f"Total sentences/lines in file: {sentence}")
print(f"Total words in file: {word}")
print(f"Total characters in file: {char}")
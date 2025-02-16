def find_words(words, letter):
    result = [word for word in words if word.count(letter) >= 2]
    return result if result else "No words found"

words = ["banana", "apple", "cherry", "grape"]
letter = "a"

print(find_words(words, letter))


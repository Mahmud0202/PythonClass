def longest_word(words):
    longest = words[0] 
    for word in words[1:]:  
        if len(word) > len(longest):  
            longest = word  
    return  {longest}
words = ["apple", "banana", "cherry", "blueberry"]
print(longest_word(words))

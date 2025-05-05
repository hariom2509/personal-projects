# def longest_even_word(sentence):
#     words = sentence.split()
#     max_length = 0
#     longest_word =""
#     for word in words:
#         if len(word) % 2 == 0:
#             if len(word) > max_length:
#                 max_length = len(word) 
#                 longest_word = word
#         else:
#             longest_word = "0"
#     return longest_word

# def main():
#     sentence = "i opera rod m baloo today"
#     word = longest_even_word(sentence)
#     print(f"the longest word in the sentence is : {word}")

# if __name__ == '__main__':
#     main()

max_word = "0"
s = "i operra rod m bannloon today"
words = s.split()
for word in words:
    if len(word)%2 ==0:
        if len(word) > len(max_word):
            max_word = word
print (max_word)



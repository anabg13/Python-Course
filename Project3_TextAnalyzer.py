print('Welcome to the text analyzer!')

text = input('Introduce the text you want to analyze: '.lower())
letters = []
for i in range(3):
    letter = input(f'Introduce letter {i+1}: '.lower())
    letters.append(letter)

print('First analysis.')
print(f'Letter "{letters[0]}" appears {text.count(letters[0])} times in the text.')
print(f'Letter "{letters[1]}" appears {text.count(letters[1])} times in the text.')
print(f'Letter "{letters[2]}" appears {text.count(letters[2])} times in the text.')
print('-------------------------------------------------------------------')

print('Second analysis.')
words = text.split()
print(f'The text has {len(words)} words.')
print('-------------------------------------------------------------------')

print('Third analysis.')
print('First letter:', text[0])
print('Last letter:', text[-1])
print('-------------------------------------------------------------------')

print('Fourth analysis.')
words.reverse()
text_inv = " ".join(words)
print(f'Inverted text: {text_inv}')
print('-------------------------------------------------------------------')

print('Fifth analysis.')
find = input('Word to find in the text: ')
find_num = text.count(find)
print(f'"{find}" is {find_num} times in the text.')
print('-------------------------------------------------------------------')

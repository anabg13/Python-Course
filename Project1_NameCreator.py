print('Question 1:')
ans1 = input('What is you favourite color?: ')
if not ans1.isalpha():
    print('Error. You must introduce a word.')
    exit()

print('Question 2:')
ans2 = input('What city would you like to visit soon?: ')
if not ans2.isalpha():
    print('Error. You must introduce a word.')
    exit()

print('Your brand name is: "' + ans1 + ' ' + ans2 + '"' '\nHope you like it.')

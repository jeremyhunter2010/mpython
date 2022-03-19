'''
Check if Palindrome

racecar - this is a palindrome
madam - this is a palindrome
truth - this is not a palindrome
'''

print("What word are you checking")
_word = input()

if _word == _word[::-1]:
  print("This is a palindrome")
else :
  print("This is not a palindrome")


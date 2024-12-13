string=input()
input_string=string.lower();

reverse_string=''.join(reversed(input_string))

#lowercase[::-1]

if input_string == reverse_string:
  print("The String is palindrome")
else:
  print("The string is not a palindrome")

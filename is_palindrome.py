def is_palindrome_iterative(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True

is_palindrome_iterative("abba")
# True
is_palindrome_iterative("abcba")
# True
is_palindrome_iterative("")
# True
is_palindrome_iterative("abcd")
# False

def is_palindrome_recursive(my_string):
  if len(my_string) <= 1:
    return True
  if my_string[0] == my_string[-1]:
    return is_palindrome_recursive(my_string[1:-1])
  return False


# test cases
print(is_palindrome_recursive("abba") == True)
print(is_palindrome_recursive("abcba") == True)
print(is_palindrome_recursive("") == True)
print(is_palindrome_recursive("abcd") == False)



#this is O(N), for each extra n it will only do one more recursive step
def recursive_sum_digits(n):
  if n <= 9:
    print("Pop!")
    return n
  last_digit = n % 10
  return last_digit + recursive_sum_digits(n // 10)

print(recursive_sum_digits(1857385455476575435675432745654645664577643))


def iterative_sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

print(iterative_sum_digits(1857385455476575435675432745654645664577643))

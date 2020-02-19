
#this approach can calculate fibonaccis up to a high limit quickly
def fibonacci_iterative_approach(n):
  output = 0
  fibonacci_numbers = []
  #loop to gen fibonacci sequence
  for i in range(n+1):
    if i <= 1:
      fibonacci_numbers.append(i)
    else:
      output = fibonacci_numbers[i-1] + fibonacci_numbers[i-2]
      fibonacci_numbers.append(output)
      print(fibonacci_numbers)
  return output

# test cases
print(fibonacci_iterative_approach(3) == 2)
print(fibonacci_iterative_approach(7) == 13)
print(fibonacci_iterative_approach(0) == 0)
print(fibonacci_iterative_approach(13))
print(fibonacci_iterative_approach(100))

#this recursive approach takes less code and less memory "spacial effiency" but is slower and requires more computation.
# it has a higher O order.
def fibonacci_recursive_approach(n):
    if n < 0:
        ValueError("Input 0 or greater only")
    if n<= 1:
        #every time a recursive function call pops out of the stack we know!
        print("Pop!")
        return n

    #look at how the function moves through the different stages, you can draw the decision tree
    #and see how the function calculates the left hand side of the tree first
    print("now recursing with fibonnaci({}) & fibonacci({})".format(n-1,n-2))
    return fibonacci_recursive_approach(n-1) + fibonacci_recursive_approach(n-2)

print(fibonacci_recursive_approach(3))
print(fibonacci_recursive_approach(7))
print(fibonacci_recursive_approach(0))
print(fibonacci_recursive_approach(15))
#if you want your computer to crash like mine did then uncomment the next line!
#print(fibonacci_recursive_approach(100))

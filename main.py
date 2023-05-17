

def flatten_and_sort(array):
  arr = []
  for item in array:
    for i in item:
      arr.append(i)
    return sorted(arr)

print(flatten_and_sort([]), [])
print(flatten_and_sort([[], []]), [])
print(flatten_and_sort([[], [1]]), [1])
print(flatten_and_sort([[12, 19, 6], [7, 13, 20], [2, 10, 6]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])



# How does this solution ensure data immutability?

#   The function takes an array as an input, sorts it, and returns the sorted array.

# Is this solution a pure function? Why or why not?

#   flatten_and_sort function takes an array as an argument, sorts it, and returns the sorted array.

# Why in particular is functional programming a helpful paradigm when solving this problem?

#   provides clear, concise, and predictable code. 


class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "Repaired!"
    
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
    
  def boost(self):
    self.max_speed *= 2

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self):
    self.condition = "Trashed!"

Racer_1 = Podracer(1, "Trashed!", 5000)
Racer_2 = Podracer(3, "Brand New!", 4500)
Racer_3 = AnakinsPod(2, "Brand New!", 6000)
Racer_4 = SebulbasPod(4, "Brand New!", 3000)

Racer_1.repair()
print(Racer_1.condition) # Output: Repaired!

print(Racer_2.condition) # Output: Brand New!

Racer_3.boost()
print(Racer_3.max_speed) # Output: 4

Racer_4.flame_jet()
print(Racer_4.condition) # Output: Trashed!


# How does this solution demonstrate the four pillars of OOP?

# Encapsulation:
#       We are encapsulating information or code within our classes
    
# Abstraction:
#       By encapsulating our code, we hide unecessary information for our race or game that may be used to cheat.
  
# Inheritance:

# Polymorphism:
#       Each racer class is using the Podracer class interface.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

#       I don't believe so. For making a racing game it makes alot of sense that we have a base race class and that all other racers inherit from that. 

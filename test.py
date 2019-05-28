
def is_prime_versionB(number):
  """ Returns True if number is prime.
  Returns False otherwise.
  """
  # Check is number is even
  if number%2 == 0:
    return False

  # If there are divisor pairs, 
  # one divisor <= number's square root
  max_divisor = int(number**0.5)
  max_divisor += 1 # So range() includes it
  # Check all possible divisors
  # from the odd numbers
  for divisor in range(3, max_divisor, 2):
    if number % divisor == 0: 
      # No remainder, so it's a factor
      return False 

  return True

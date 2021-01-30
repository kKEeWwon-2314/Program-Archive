def get_position(n, k): 
      if (n == 1): 
          return 1
      else: 
          # The position returned by josephus(n - 1, k) is adjusted 
          return (get_position(n - 1, k) + k-1) % n + 1

# driver program
n = int(input('How many people are in the circle today? '))
k = 2
print("The chosen place is", get_position(n, k))
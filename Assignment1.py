def lower(n):
  print(" ")
  print(" Lower Triangle  ")
  print(" ")
  for i in range(n):
      for j in range(i+1):
          print('*', end=" ")
      print()
  print(" ")

def upper(n):
  print(" ")
  print(" Upper Triangle  ")
  print(" ")
  for i in range(n):
      for j in range(i, n):
          print("*", end=" ")
      print()
  print(" ")

def pyramid(n):
  print(" ")
  print(" Pyramid  ")
  print(" ")
  for i in range(n):
      for j in range(n-i-1):
          print(end=" ")
      for j in range(2*i+1):
          print('*', end="")
      print()
  print(" ")

a = int(input("Enter The Number Of Rows : "))

lower(a)
upper(a)
pyramid(a)

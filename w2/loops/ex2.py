n = int(input("please enter a number "))
while n > 0:
  # check even and odd
  if n % 2 ==0:
    print (n,"is an even number")
else:
  print(n,"is an odd number") 
  # decrease number by 1 in each interation 
n = n - 1
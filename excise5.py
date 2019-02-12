print ("Would you like to walk or run?")
user_name = input ()

walk = 1
run = 5

if user_name == input(walk):
  print("walk {}km.".format(walk))
  walk += 1

if user_name == input(run):
    print("run {}km.".format(run))
while run < 5:
    run += 5

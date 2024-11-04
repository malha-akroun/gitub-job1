
for x in range(3, 100):
     if all (x%y !=0 for y in range (2,x)):
            print(x)


 # job 5 
prime = "babnane"
for x in range(0, 100):
    for y in range(2, x):
            if x > 1 and x%y == 0:
                  prime = "non"
                  break
            else:
                  prime = "oui"
    if prime == "oui":
            print(x)
      






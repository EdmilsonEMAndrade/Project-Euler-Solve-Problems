def isPythagorean(a,b,c):
  if a<b<c and (a**2+b**2==c**2):
    return True
  else:
    return False


print(isPythagorean(200,375,425))


for a in range(0,1000):
  print(a)
  for b in range(a+1,1000):
    for c in range(b+1,1000):
      if isPythagorean(a,b,c) == True and a+b+c == 1000:
        print(a,b,c)

      if a+b+c>1000:
        break

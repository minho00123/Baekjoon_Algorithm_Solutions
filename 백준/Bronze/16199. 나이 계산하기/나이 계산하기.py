y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
age1 = 0
age2 = 1
age3 = 0
if y1 == y2:
  print(age1)
  print(age2)
  print(age3)
else:
  if m1 > m2:
    age1 += y2 - y1 - 1
  elif m1 == m2:
    if d1 > d2:
      age1 += y2 - y1 - 1
    else:
      age1 += y2 - y1
  else:
    age1 += y2 - y1
  age2 += y2 - y1
  age3 += y2 - y1
  print(age1)
  print(age2)
  print(age3)

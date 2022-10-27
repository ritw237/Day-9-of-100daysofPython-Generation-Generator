print("Generation Generator!!! Which generation you belong to?")
print()

year = int(input("What is your birth year"))
if year >= 1925 and year<=1946:
  print("You are Traditionalists!")
elif year >= 1947 and year<=1964:
  print("You are Baby Boomers!")
elif year >= 1965 and year<=1981:
  print("You are Generation X!")
elif year >= 1982 and year<=1995:
  print("You are Millenials!")
elif year >= 1996 and year<=2015:
  print("You are Generation Z!")
else:
  print("You belong to an unspecified generation from a forgotten time or from future!")
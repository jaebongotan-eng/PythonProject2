#Chinese Zodiac Program ila CS3

#Ask the user to enter their birth year.
birth_year = int(input("Enter your birth year: "))

#Use an if-else selection structure to validate the birth year input of the user.
if birth_year < 1900:
  print("Invalid year. The year of birth must be earlier than 1900.")
else:
  chinese_zodiac_number = (birth_year - 1900) % 12

# Use an if-else selection structure to determine the user's Chinese Zodiac.
  if chinese_zodiac_number == 0:
    chinese_zodiac = "Rat (鼠 / Shǔ)"

  elif chinese_zodiac_number == 1:
    chinese_zodiac = "Ox (牛 / Niú)"

  elif chinese_zodiac_number == 2:
      chinese_zodiac = "Tiger (虎 / Hǔ)"

  elif chinese_zodiac_number == 3:
      chinese_zodiac = "Rabbit (兔 / Tù)"

  elif chinese_zodiac_number == 4:
      chinese_zodiac = "Dragon (龙 / Lóng)"

  elif chinese_zodiac_number == 5:
      chinese_zodiac = "Snake (蛇 / Shé)"

  elif chinese_zodiac_number == 6:
      chinese_zodiac = "Horse (马 / Mǎ)"

  elif chinese_zodiac_number == 7:
      chinese_zodiac = "Goat (羊 / Yáng)"

  elif chinese_zodiac_number == 8:
      chinese_zodiac = "Monkey (猴 / Hóu)"

  elif chinese_zodiac_number == 9:
      chinese_zodiac = "Rooster (鸡 / Jī)"

  elif chinese_zodiac_number == 10:
      chinese_zodiac = "Dog (狗 / Gǒu)"

  else:
      chinese_zodiac = "Pig (猪 / Zhū)"

  # Print the birth year and Chinese zodiac.
  print(f"Birth year: {birth_year}")

  print(f"Chinese Zodiac: {chinese_zodiac}")
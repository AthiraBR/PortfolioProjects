def ceaser(message, key, mode):
  LETTERS = 'ABCDEFGHIJKLMNOPQRSUVWXYZ'
  translated = ''
  message = message.upper()
  key = key%26

  for i in message:
    temp = LETTERS.find(i)
    if mode == 'encrypt':
      temp = temp + key
    elif mode == 'decrypt':
      temp = temp - key

    if temp >= len(LETTERS):
      temp -= len(LETTERS)
    elif temp < 0:
      temp += len(LETTERS)

    translated += LETTERS[temp]
  print(translated)


print("Encrypt:")
ceaser('CYBRARY',27, 'encrypt')

print("Decrypt:")
ceaser('DZCSBSZ', 27, 'decrypt')

# Position of each letter in the alphabet
pos = {
  'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
  'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
  's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}


def vigerene(str, key, decrypt = False):
  """
  Encrypt or decrypt `str` with `key` using vigerene cipher

  Keyword arguments:
    str (str):      The string to encrypt/decrypt
    key (str):      The key to use when encrypting/decrypting `str`
    decrypt (bool): Whether to encrypt or decrypt `str` (default False)

  Returns:
    res (str): The encrypted/decrypted version of `str` when using `key`
  """
  res = []  # The encrypted charset
  index = 0 # The current index of the character to encrypt

  # Loop through each character of the string to encrypt
  for char in str:
    # Get the positive shift of `char` in the alphabet if encrypting, negative shift if decrypting
    rotation = pos[key.lower()[index]] if decrypt == False else -pos[key.lower()[index]]

    # Append `char` to `res` if not alphanumeric, else shift to
    # the corresponding character matching with `key` and append it to `res`
    if char.lower() not in pos:
      res.append(char)
    elif char.isalpha():
      shift = 97 if char.islower() else 65
      res.append(chr((ord(char) + rotation - shift) % 26 + shift))

    # Update the index after each iteration
    index = 0 if index == (len(key) - 1) else + 1

  return ''.join(res)

# Run the following tests if ran and not imported
if __name__ == '__main__':
  key = 'VeryGoodKey'                   # The key used for encrypting/decrypting
  str = 'Super secret gamer info: 5050' # The string to encrypt
  enc = vigerene(str, key)              # The vigerene string of `str` using `key`
  dec = vigerene(enc, key, True)        # `enc` decrypted using `key`

  # Print the pydoc and ecnrypt/decrypting results
  print(vigerene.__doc__)
  print('Key: %s\nStr: %s\nEnc: %s\nDec: %s' % (key, str, enc, dec))

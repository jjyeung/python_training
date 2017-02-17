def match_ends(words=[]):
  counter = 0
  for word in words:
    w_len = len(word)
    if word and w_len >= 2:
      counter += 1
  return counter

print match_ends()
print match_ends(['aasdf','counter', 'f', '2', '34343'])

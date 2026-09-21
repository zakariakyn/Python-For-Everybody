text = "X-DSPAM-Confidence:    0.8475"

swith = text.find(":")
word = text[swith + 1 :].strip()
num = float(word)

print(num)
'''
Algorithm of Caesar Cipher
The algorithm of Caesar cipher holds the following features

Caesar Cipher Technique is the simple and easy method of encryption technique.

It is simple type of substitution cipher.

Each letter of plain text is replaced by a letter with some fixed number of 
positions down with alphabet.

The following diagram depicts the working of Caesar cipher algorithm implementation
'''
message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))
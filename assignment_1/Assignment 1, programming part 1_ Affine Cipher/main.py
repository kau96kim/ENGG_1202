from affine import *
text = "Attack!"
a = 9
b = 13
cipher = afencode(text, a, b)
print(text, "=>", cipher)

from affine import *
cipher = "Nccnfz!"
a = 9
b = 13
text = afdecode(cipher, a, b)
print(cipher, "=>", text)
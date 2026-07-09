import re
pattern="and"
text='''
ndia and adjacent countries. Relief shown by gradient tints, shading, and spot heights. Depths shown by gradient tints and contours. Shows area from Afghanistan in the west to Thailand in the east. Published under the direction of Colonel Sir S.G. Burrard, K.C.S.I.R.E., F.R.S., Surveyor General of India, 1917. Mounted on cloth and sectioned into 6 pieces. Darkened. Some losses throughout. 186 x 208 cm.



'''
match=re.search(pattern,text)
print(match)
#Sam Smedinghoff
#9/22/17
#name.py - Gives you a "cool" name banner

name = input('What is your name')
ccolor = (input('Enter an RGB code' ))


from ggame import *

bcolor = Color(ccolor,1)
black = Color(0x000000,1)


blackOutline = LineStyle(1,black) #pixels, color
bRectangle = RectangleAsset(1016,,blackOutline,bcolor)
text = TextAsset(name,fill=black,style='bold 20pt Times')

Sprite(bRectangle,(0,0))
Sprite(text,(400, 25))
App().run()


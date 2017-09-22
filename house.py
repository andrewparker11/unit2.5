#Sam Smedinghoff
#9/20/17
#house.py - Makes a house

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black) #pixels, color
redRectangle = RectangleAsset(200,200,blackOutline,red) #width, height, outline, fill

Sprite(redRectangle,(300,200)) #(right,down))
App().run()



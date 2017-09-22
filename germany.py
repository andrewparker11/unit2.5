#Sam Smedinghoff
#9/20/17
#house.py - Makes a house

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)


blackOutline = LineStyle(1,black) #pixels, color
redRectangle = RectangleAsset(200,200,blackOutline,red) #width, height, outline, fill
redRectangle = RectangleAsset(200,200,blackOutline,red) #width, height, outline, fill
text = TextAsset('Flag of Germany',fill=black,style='bold 40pt Times')


Sprite(redRectangle,(300,200)) #(right,down))
Sprite(yellowRectangle,(300,200))
Sprite(blackRectangle,(300,200))
Sprite(text,(100, 100))
App().run()



#Sam Smedinghoff
#9/20/17
#house.py - Makes a house

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)


blackOutline = LineStyle(1,black) #pixels, color
redRectangle = RectangleAsset(200,50,blackOutline,red) #width, height, outline, fill
blackRectangle = RectangleAsset(200,50,blackOutline,black)
yellowRectangle = RectangleAsset(200,50,blackOutline,yellow)
text = TextAsset('Flag of Germany',fill=black,style='bold 20pt Times')


Sprite(redRectangle,(300,100)) #(right,down))
Sprite(yellowRectangle,(300,150))
Sprite(blackRectangle,(300,50))
Sprite(text,(400, 25))
App().run()



#Sam Smedinghoff
#9/22/17
#Germany.py - Makes the flag of germany (not belgium)

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)


blackOutline = LineStyle(1,black) #pixels, color
redRectangle = RectangleAsset(300,50,blackOutline,red) #width, height, outline, fill
blackRectangle = RectangleAsset(300,50,blackOutline,black)
yellowRectangle = RectangleAsset(300,50,blackOutline,yellow)
text = TextAsset('Flag of Germany',fill=black,style='bold 20pt Times')


Sprite(redRectangle,(300,150)) #(right,down))
Sprite(yellowRectangle,(300,200))
Sprite(blackRectangle,(300,100))
Sprite(text,(400, 25))
App().run()



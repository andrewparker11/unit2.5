#Sam Smedinghoff
#9/20/17
#house.py - Makes a house

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black) #pixels, color
redRectangle = RectangleAsset(200,200,blackOutline,red) #width, height, outline, fill
redTriangle = PolygonAsset([(0,0), (120,180), (60,300)],blackOutline,red) #list of endpoints
text = TextAsset('Smeds',fill=green,style='bold 40pt Times')


Sprite(redRectangle,(300,200)) #(right,down))
Sprite(redTriangle,(300,200))
Sprite(text,(200, 100))
App().run()



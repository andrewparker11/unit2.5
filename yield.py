#Sam Smedinghoff
#9/26/17
#yield.py - Gives you a yield sign

from ggame import *

red = Color(0xFF0000,1)
white = Color(0x000000,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black) #pixels, color


blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, linestyle
whiteTriangle = PolygonAsset([(0,0), (120,180), (60,300)],blackOutline,white) #list of endpoints
redTriangle = PolygonAsset([(0,0), (300,0), (150,250)],blackOutline,red) #list of endpoints
text = TextAsset('YIELD',fill=red,style='bold 40pt Times')

Sprite(whiteTriangle)
Sprite(blackLine)
Sprite(redTriangle)
Sprite(text,(300,200))
App().run()


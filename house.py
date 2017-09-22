#Sam Smedinghoff
#9/20/17
#house.py - Makes a house

from ggame import *

red = Color(0xFF0000,1)
black = Color(0x000000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)

blackOutline = LineStyle(1,black) #pixels, color
redRectangle = RectangleAsset(200,200,blackOutline,red) #width, height, outline, fill
redTriangle = PolygonAsset([(0,0), (200,0), (100,-150)],blackOutline,red) #list of endpoints
text = TextAsset('Mi Casa',fill=green,style='bold 40pt Times')


Sprite(redRectangle,(300,200)) #(right,down))
Sprite(redTriangle,(300,200))
Sprite(text,(100, 100))
App().run()



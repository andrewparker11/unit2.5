#Andrew Parker
#9/18/17
#warmup5.py - makes a yellow diamond with my name inside in blue

from ggame import *

yellow = Color(0xFFFF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black) #pixels, color

yellowDiamond = PolygonAsset([(0,0), (120,180), (60,300)],blackOutline,yellow) #list of endpoints
text = TextAsset('Andrew Parker',fill=blue,style='bold 40pt Times')


Sprite(yellowDiamond,(50,50)) #(right,down)
Sprite(text,(300,200))
App().run()
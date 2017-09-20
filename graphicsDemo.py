#Sam Smedinghoff
#9/20/17
#graphicsDemo.py - Intro to ggame

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black) #pixels, color

redRectangle = RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, film)
greenEllipse = EllipseAsset(100,50,blackOutline,green) #horizontal radius, vertical_radius, outline, fill
blackLine = LineAsset(50,160,blackOutline) #x_endpoint, y_endpoint, linestyle
redTriangle = PolygonAsset([(0,0), (120,180), (60,300)],blackOutline,red) #list of endpoints

Sprite(redRectangle)
Sprite(blueCircle,(50,50)) #(right,down)
Sprite(greenEllipse,(200,400)) #(right,down)
Sprite(blackLine)
App().run()

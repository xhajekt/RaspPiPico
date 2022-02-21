import board
import neopixel
import time
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
 
np = neopixel.NeoPixel(board.GP0, 30)
np.brightness = 0.2
    
a = (148, 0, 211)
b = (75, 0, 130)
c = (0, 0, 255)
d = (0, 255, 0)
e = (255, 255, 0)
f = (255, 127, 0)
g = (255,255,255)

while True:
    
# for x in range (255):
#     x=x+20
#     for y in range (255):
#         y=y+20
#         for z in range (255):
#             np.fill((x,y,z))
#             time.sleep(0.1)
#             z=z+20
#             print("Loop number",x,y,z)
    for i in range (0,100,5):
      print(i)
      time.sleep(0.01)
      np.brightness = i/100
      np.fill(g)

#     for i in range (25):
#       np[i-1]=g
#       np[i]=a
#       np[i+1]=b
#       np[i+2]=c
#       np[i+3]=d
#       np[i+4]=e
#       np[i+5]=f
#       np.show()
#       time.sleep(0.01)
#       np.fill(g)
#       print(i)
#     
#     for i in range (24,0,-1):
#       print(i)
#       np[i-1]=g
#       np[i]=a
#       np[i+1]=b
#       np[i+2]=c
#       np[i+3]=d
#       np[i+4]=e
#       np[i+5]=f
#       np.show()
#       time.sleep(0.01)
#       np.fill(g)
      
    for i in range (100,0,-5):
      print(i)
      time.sleep(0.01)
      np.brightness = i/100
      np.fill(g)
    

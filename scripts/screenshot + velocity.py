#-------------------------------------------------------------------------------------------------------------------------------
# Name:         Screenshot + Velocity
# Purpose:      calculate velocity and acceleration from color detection of screenshots
#
# Author:       FrenchPython
#
# Created:      11/25/2018
#---------------------------------------------------------------------------------------------------------------------------
import pprint as pp
import mss as mss
import mss.tools
import PIL
import time
import math
from PIL import Image
import os
import numpy as np
#---------------------------------------------------------DICTIONARIES---------------------------------------------------

tx = {}                                                            
vx = {}
ax = {}

txw = {}
vxw = {}
axw = {}

cx = {}
cxwr = {}
cxwg = {}
cxwb = {}



#-------------------------------------------------Acceleration Function-------------------------------------------
#where x = velocity at any given point y gives deceleration at any given point

def Atw(v):
        
        y = (-0.0003*(v**2)) + (0.02*v) - 3.5948

        return y

def Trim(Atw, v):

        y = (-(1/Atw(v)))*(v-(math.sqrt((385.82/r)*(math.tan(15.75))))) #alpha might be 14.75 from paper assumption 22.5

        return y



        

def Ballposrim(Atw, v):

        y = ( ((385.82/r)*math.tan(15.75)) - (v**2) ) / (2*Atw(v))

        return y


def prettylists():
        
        BallList = pp.pprint(list(vx.values()))
        TimeList = pp.pprint(list(tx.values()))
        AccelerationList = pp.pprint(list(ax.values()))

        return BallList
        return TimeList
#---------------------------------------------------AVERAGE COLOR FUNCTION-------------------------------------------


def average_image_color(filename):                        
	i = Image.open(filename)
	h = i.histogram()

	# split into red, green, blue
	r = h[0:256]
	g = h[256:256*2]
	b = h[256*2: 256*3]

	# perform the weighted average of each channel:
	# the *index* is the channel value, and the *value* is its weight
	return (
		sum( i*w for i, w in enumerate(r) ) / sum(r),
		sum( i*w for i, w in enumerate(g) ) / sum(g),
		sum( i*w for i, w in enumerate(b) ) / sum(b)
	)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        1#print (average_image_color(sys.argv[1]))
    #else:
        #print ('usage: average_image_color.py FILENAME')





#------------------------------------------------------------------COLOR CALIBRATION--------------------------------------------------



START = True

calibrate = input('Calibrate Colors ? ')

if calibrate == 'y':                                                   
        tc0 = time.time()
        color = 0
        for i in range(50):
#------------------------------------------------------------BALL SCREENSHOT CALIBRATION--------------------------------------------
                with mss.mss() as sct:      
                # The screen part to capture
                        monitorb = {"top": 160, "left": 1970, "width": 80, "height": 50}
                        output = 'SSC' + str(i)+ '.png'.format(**monitorb)

                # Grab the data
                        im = sct.grab(monitorb)
        
                # Save to the picture file
                        mss.tools.to_png(im.rgb, im.size, output=output)
                
                
                avc = average_image_color('SSC' + str(i)+ '.png')
                tavc = sum(avc)
                cx[i] = tavc
#------------------------------------------------------------WHEEL SCREENSHOT CALIBRATION--------------------------------------------------
                with mss.mss() as sct:      
                        monitorw = {"top": 325, "left": 1970, "width": 60, "height": 40}
                        output = 'SSWC' + str(i)+ '.png'.format(**monitorw)

                # Grab the data
                        im = sct.grab(monitorw)
        
                # Save to the picture file
                        mss.tools.to_png(im.rgb, im.size, output=output)

                        avcw = average_image_color('SSWC' + str(i)+ '.png')
                        
                        red = avcw[0]
                        green = avcw[1]
                        blue = avcw[2]

                        cxwr[i] = red
                        cxwg[i] = green
                        cxwb[i] = blue


        
                        
                
        calibration = sum(cx.values())/len(cx.values())    #BALL CALIBRATION
        calibrationwr = sum(cxwr.values())/len(cxwr.values()) #WHEEL COLOR CALIBRATION
        calibrationwg = sum(cxwg.values())/len(cxwg.values())
        calibrationwb = sum(cxwb.values())/len(cxwb.values())
        tc1 = time.time()
        TC = tc1 - tc0
        print('Calibration time: ' + str(TC))
        #print('Ball Color Variance: ' + str(np.var(list(cx.values()))))
        print('Calibration Ball: ' + str(calibration))
        print('Calibration Wheel Red: ' + str(calibrationwr))
        print('Calibration Wheel Green: ' + str(calibrationwg))
        print('Calibration Wheel Blue: ' + str(calibrationwb))
        #print('Wheel Color Variance: ' + str(np.var(list(cxw.values()))))

#------------------------------------------------------------DELETE CALIBRATION PICTURES-----------------------------------------
for i in range(49):
        if i < 199:
                os.remove('SSC' + str(i+1)+ '.png')
                os.remove('SSWC' + str(i+1) + '.png')

        else:
                break

        
#-----------------------------------------------------------------START OF LOOP---------------------------------------------                
ready = input('Enter when Ready ')
count = 0
count0 = 0
countw = 0
vw = 0
v = 0

START = True
STARTW = True
tt0 = time.time()

while v == 0 :#vw == 0:
        
#-----------------------------------------------------------BALL---SCREENSHOT------FOR-CALCULATIONS----------------------------------------
        
    with mss.mss() as sct:      #BALL SCREENSHOT
                monitorb #= {"top": 860, "left": 2316, "width": 80, "height": 25}
                output = 'SS' + str(count)+ '.png'.format(**monitorb)
                
                # Grab the data
                im = sct.grab(monitorb)
        
                # Save to the picture file
                mss.tools.to_png(im.rgb, im.size, output=output)

#-----------------------------------------------------------WHEEL----SCREENSHOT-----FOR-CALCULATION--------------------------------------



    with mss.mss() as sct:      #wheel SCREENSHOT
                monitorw #= {"top": 961, "left": 2326, "width": 20, "height": 20}
                output = 'SSW' + str(count)+ '.png'.format(**monitorw)

                # Grab the data
                im = sct.grab(monitorw)
        
                # Save to the picture file
                mss.tools.to_png(im.rgb, im.size, output=output)
                             


    
    
    #average color
    avc = average_image_color('SS' + str(count)+ '.png')
    avcw = average_image_color('SSW' + str(count)+ '.png')
    
    red = avcw[0]  
    green = avcw[1]
    blue = avcw[2]
    
    #print(str(avcw[1]))         #GREEN tuple
    #print('Average Color: ' + str(sum(avc)))
    tavc = sum(avc)
    
    #print(tavc)
    count += 1

    
#-------------------------------------------------------------BALL----VELOCITY----------------------------------------------
    d = float(12.75*float(math.pi)*2)
    r = 12.75
    if tavc > calibration + 5 and START == True and tavc < calibration*2:                        
        start = float(time.time())
        START = False

        time.sleep(0.03)


    elif tavc > calibration + 5 and START == False and tavc < calibration*2:                                             
        end = float(time.time())

        t = float(end) - float(start)
        start = end
            
        v = d/t
        tdiff0 = time.time()

        
        tx[count0] = t
        vx[count0] = v

        print('\nVelocity: ' + str(v))
        #print(str(v))
        count0 += 1

        time.sleep(0.1)

        
#---------------------------------------------------BALL------ACCELERATION-----------------------------------------


    if len(tx) and len(vx) > 1:                                 
        a = (vx[count0-1] - vx[count0-2])/(tx[count0-1])
        #print('Acceleration: ' + str(a))
        ax[count0] = a
     
                
    if len(ax) > 0 :
        averageAcceleration = (sum(ax.values())) / len(ax)
        #print('Average Acceleration ' + str(averageAcceleration)+ '\n')
        
    
#----------------------------------------------------WHEEL------VELOCITY---------------------------------------------------

        
    dw = float(8.26*float(math.pi)*2)
    
    if red < calibrationwr -15 and green > calibrationwg + 15 and blue > calibrationwb and STARTW == True:                        
        startw = float(time.time())
        STARTW = False

        time.sleep(0.1)


    elif red < calibrationwr -5 and green > calibrationwg + 5 and blue > calibrationwb and STARTW == False:                                             
        endw = float(time.time())

        tw = float(endw) - float(startw)
        startw = endw
            
        vw = dw/tw
        tdiff1 = time.time()
        
        txw[countw] = tw
        vxw[countw] = vw

        
        countw += 1

        #time.sleep(0)
        #print(str(vw))
#-------------------------------RESULTS--+--PICTURE--DELETE--------------------------------------------------------------------------------
        

tt1 = time.time()
TT = tt1 - tt0
#Tdiff = tdiff1 - tdiff0
print('\nTotal Time: ' + str(TT)+ '\n# of Pictures: ' + str(count))
print('Wheel Velocity: ' + str(vw))
print('Ball Velocity: ' + str(v))
#print('Wheel Velocity Calculated ' + str(Tdiff) + ' Seconds after Ball Velocity')
print('\n''Time to Trim: ' + str(Trim(Atw, v)))
Ttest0 = time.time()

for i in range(count - 1):
    os.remove('SS' + str(i)+ '.png')
    os.remove('SSW' + str(i)+ '.png')

#print(ax.values())
#print(vx.values())
#-------TEST RESULTS


Enter = input('Enter when ball hits deflector: ')
Ttest1 = time.time()

Ttest = Ttest1 - Ttest0
print('Tdef is this many seconds after Trim: ' + str(Ttest - Trim(Atw, v)))


















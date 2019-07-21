#-------------------------------------------------------------------------------------------------------------------------------
# Name:         R2.0
# Purpose:      Determin ball and wheel location given initial velocity.
#
# Author:       FrenchPython
#
# Created:      02/02/2019
#---------------------------------------------------------------------------------------------------------------------------

import pprint as pp
import mss as mss
import mss.tools
import PIL
from PIL import Image
import time
import numpy as np
import math
import os
import csv

#-------------------------------DIMENTIONS-PORT-2-BLACK----------------------------

#cm
r = 32              #Radius to Rim
rd = 29             #Radius to Deflector
rw = 18             #Radius to Wheel
alpha = 0.2574      #Radians, 30 Degrees
g = 980             #gravity constant ?
d = r*2*math.pi
dw = rw*2*math.pi

#-----------------------------------------DICTIONARIES/LIST-------------------------------------------------------

cx = {} #list of sum of all colors from calibration

cx2 = {} #list of sum of all colors from calculations
tx = {} #list of time of each revolution
vx = {} #list of velocity of ball per revolution

green = {} #list of green:255 values for wheel
txw = {}  #list of wheel time per revolution
vxw = {} #list of wheel velocity
aw = -0.1  #wheel acceleration

WheelNumbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
WheelNumbersReversed = [26, 3, 35, 12, 28, 7, 29, 18, 22, 9, 31, 14, 20, 1, 33, 16, 24, 5, 10, 23, 8, 30, 11, 36, 13, 27, 6, 34, 17, 25, 2, 21, 4, 19, 15, 32, 0]
#-----------------------------------------FUNCTIONS------------------------------------------------------

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


def save(mylist, filename):
    with open('filename', 'a') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(mylist)




def DeflNumber(angle, spread):
    if 0 <= angle <= 9.72:
        DeflNumber = 0
    elif 9.72 <= angle <= 19.4:
        DeflNumber = 32
    elif 19.4 <= angle <= 29.2:
        DeflNumber = 15
    elif 29.2 <= angle <= 38.9:
        DeflNumber = 19
    elif 38.9 <= angle <= 48.6:
        DeflNumber = 4
    elif 48.6 <= angle <= 58.4:
        DeflNumber = 21
    elif 58.4 <= angle <= 68.1:
        DeflNumber = 2
    elif 68.1 <= angle <= 77.8:
        DeflNumber = 25
    elif 77.8 <= angle <= 87.5:
        DeflNumber = 17
    elif 87.5 <= angle <= 97.3:
        DeflNumber = 34
    elif 97.3 <= angle <= 107:
        DeflNumber = 6
    elif 107 <= angle <= 116.7:
        DeflNumber = 27
    elif 116.7 <= angle <= 126.5:
        DeflNumber = 13
    elif 126.5 <= angle <= 136.2:
        DeflNumber = 36
    elif 136.2 <= angle <= 145.9:
        DeflNumber = 11
    elif 145.9 <= angle <= 155.7:
        DeflNumber = 30
    elif 155.7 <= angle <= 165.4:
        DeflNumber = 8
    elif 165.4 <= angle <= 175.1:
        DeflNumber = 23
    elif 175.1 <= angle <= 184.8:
        DeflNumber = 10
    elif 184.8 <= angle <= 194.6:
        DeflNumber = 5
    elif 194.6 <= angle <= 204.3:
        DeflNumber = 24
    elif 204.3 <= angle <= 214:
        DeflNumber = 16
    elif 214 <= angle <= 223.8:
        DeflNumber = 33 
    elif 223.8 <= angle <= 233.5:
        DeflNumber = 1
    elif 233.5 <= angle <= 243.2:
        DeflNumber = 20
    elif 243.2 <= angle <= 253:
        DeflNumber = 14
    elif 254 <= angle <= 262.7:
        DeflNumber = 31
    elif 262.7 <= angle <= 272.4:
        DeflNumber = 9
    elif 272.4 <= angle <= 282.1:
        DeflNumber = 22
    elif 282.1 <= angle <= 291.9:
        DeflNumber = 18
    elif 291.9 <= angle <= 301.6:
        DeflNumber = 29
    elif 301.6 <= angle <= 311.3:
        DeflNumber = 7
    elif 311.3 <= angle <= 321:
        DeflNumber = 28
    elif 321 <= angle <= 330.8:
        DeflNumber = 12
    elif 330.8 <= angle <= 340.5:
        DeflNumber = 35
    elif 340.5 <= angle <= 350.3:
        DeflNumber = 3
    elif 350.3 <= angle <= 360:
        DeflNumber = 26


    index0 = WheelNumbers.index(DeflNumber)
    index1 = WheelNumbers.index(DeflNumber) + spread

    indexR0 = WheelNumbersReversed.index(DeflNumber)
    indexR1 = WheelNumbersReversed.index(DeflNumber) + spread
    

    WheelDirection = input('Wheel Direction: C or CC ? ')
    
    if WheelDirection == 'cc':
        return WheelNumbers[index0:index1]
    if WheelDirection == 'c':
        return WheelNumbersReversed[indexR0:indexR1]
        

        









#-----------------------------COLOR CALIBRATIONs--------------------------------------

while True:

        START = True

        calibrate = input('\nCalibrate ?: ')

        if calibrate == 'y':                                                   
                tc0 = time.time()
                color = 0
                for i in range(150):
#------------------------------------------------------------BALL SCREENSHOT CALIBRATION--------------------------------------------
                        with mss.mss() as sct:      
                        # The screen part to capture
                                monitorb = {"top": 686, "left": 2118, "width": 35 , "height": 30} #CHANGE PIC LOCATION HERE
                                output = 'SSC' + str(i)+ '.png'.format(**monitorb)

                        # Grab the data
                                im = sct.grab(monitorb)
                
                        # Save to the picture file
                                mss.tools.to_png(im.rgb, im.size, output=output)
                        
                        
                        avc = average_image_color('SSC' + str(i)+ '.png')
                        tavc = sum(avc) #sum all colors because we are trying to detect the WHITE ball, so all colors will increase when ball is in pic
                        cx[i] = tavc

        
        tc1 = time.time() #timer for caliibration time
        TC = tc1 - tc0
        print('Calibration time: ' + str(TC))

        calibration = sum(cx.values())/len(cx.values())    #BALL CALIBRATION
        ballcolorstd = np.std(list(cx.values()))













#-----------------------------------------------------------------START OF LOOP---------------------------------------------                
        ready = input('\nEnter when Ready ')
        if ready == 'n':
                break

        
        count = 0
        count0 = 0
        countw = 0
        vw = 0
        v = 0

        START = True
        STARTW = True
        tt0 = time.time()

        while True:



#-----------------------------------SCREENSHOT------FOR-CALCULATIONS--------------------------



            
            with mss.mss() as sct:      #WHEEL SCREENSHOT
                        monitorw = {"top": 768, "left": 2136, "width": 15, "height": 15}
                        output = 'SSW' + str(count)+ '.png'.format(**monitorw)

                        # Grab the data
                        im = sct.grab(monitorw)
                
                        # Save to the picture file
                        mss.tools.to_png(im.rgb, im.size, output=output)
                        
            avcw = average_image_color('SSW' + str(count)+ '.png') #for wheel
            
            green[count] = avcw[1]

            greenSTD = np.std(list(green.values()))   #10
            greenMean = np.mean(list(green.values())) #47
            



                
            with mss.mss() as sct:      #BALL SCREENSHOT
                        monitorb 
                        output = 'SS' + str(count)+ '.png'.format(**monitorb)
                        
                        # Grab the data
                        im = sct.grab(monitorb)
                
                        # Save to the picture file
                        mss.tools.to_png(im.rgb, im.size, output=output)


            #average color for calculation (same as calibration procedure)
            avc = average_image_color('SS' + str(count)+ '.png')
            tavc = sum(avc)
            cx2[count] = tavc
            count += 1
            

#--------------------------------VELOCITY----------------------------------------------


#--------------------BALL-----------------------------
            
            if tavc > calibration + (ballcolorstd*15) and START == True and tavc < calibration*3:
                
                start = float(time.time())      #start timing when ball detected
                START = False                   #Allows elif to be executed

                

        

            elif tavc > calibration + (ballcolorstd*15) and START == False and tavc < calibration*3:
                
                end = float(time.time())        #End timing when ball detected 2nd time 
                t = float(end) - float(start)   #time of revolution
                v = d/t                         #Veloctiy cm/s
                
                if v < 500:  #no double counting 
                    tx[count0] = t                  #Save revolution timings
                    vx[count0] = v                  #Save velocities 
                    count0 += 1                     #For dictionary indexing

                    start = end                     #reset start for next revolution
                
#-----------------WHEEL--------------------------

                    
            if green[count-1] > 80 and STARTW == True:
                
                startw = float(time.time())
                STARTW = False

            elif green[count-1] > 80 and startw > 1 and STARTW == False:

                endw = float(time.time())
                tw = endw - startw
                vw = dw/tw

                if vw < 100:
                    txw[countw] = tw
                    vxw[countw] = vw

                    countw += 1
                    startw = endw
                



#---------------------CALCULATIONS--------------------------

            if 75>vw>5:
                a = (0.0006*(v**2)) - (0.3613*v) + 35.265     #R-squared 98.7%
                Trim = (1/-a)*(v-(math.sqrt((g/r)*math.tan(alpha))))
                Tdefl = Trim - 2
                BallPos = (0 + (v*Tdefl) + ((a*(Tdefl**2))/2)) % 360   #BALL POSITION

                
                vw = vxw[countw-1]
                WheelPos = (0 + (vw*Tdefl) + ((aw*(Tdefl**2))/2)) % 360 #WHEEL POSITION
                #print('\nBall Angle: ' + str(BallPos) + '\nWheel Angle: ' + str(WheelPos))
                
                AngularWheelLoc = abs(abs(BallPos - 360) - WheelPos)
                
                print(DeflNumber(AngularWheelLoc, 2))
           
                break
                




#-----------------------------DATA-COLLECTION--------------------------------------


#save(list(tx.values()), 'balltime.csv')



















































                        

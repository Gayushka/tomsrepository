#-------------------------------------------------------------------------------
# Name:         Screenshot2.0
# Purpose:      detect color change from screenshot pictures
#
# Author:       FrenchPython
#
# Created:      11/25/2018
#-------------------------------------------------------------------------------


import pyscreenshot as SS
import PIL
import time
import pyautogui as gui

from PIL import Image


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
        print (average_image_color(sys.argv[1]))
    else:
        print ('usage: average_image_color.py FILENAME')




count = 0

number_of_pictures = int(input('Enter Number of Pictures: '))

ready = input('Enter x1, y2 ')
coordinates1 = gui.position()

ready = input('Enter x2, y2 ')
coordinates2 = gui.position()

ready = input('Enter when Ready ')

tt0 = time.time()

while count < number_of_pictures:
    t0 = time.time()
    im = SS.grab(bbox=(2042, 159, 2176, 217), childprocess=False)#for testing
    #im = SS.grab(bbox=(coordinates1[0],coordinates1[1], coordinates2[0], coordinates2[1]), childprocess=False)
    im.save('SS' + str(count)+ '.png')
    
    t1 = time.time()

    T = t1 - t0
    #print('Time per picture: '  + str(T))

    #average color
    avc = average_image_color('SS' + str(count)+ '.png')
    print('Average Color: ' + str(sum(avc)))
    tavc = sum(avc)
    
    count += 1



tt1 = time.time()
TT = tt1 - tt0
print('Total Time: ' + str(TT)+ '\n# of Pictures: ' + str(count))



#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shlomi
#
# Created:     07/10/2018
# Copyright:   (c) Shlomi 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import datetime
import time
import json

def main():
    loaded = False
    while True:
        try:
            cmd = input("What do you want to do? 'i' to input values,\n'd' to set parameter values as default,\n'e' exit app,\n'l' load default values from file,\n's' to save default values to file") or "i"
        except:
            cmd = "i"

        if cmd != "i" and cmd != "d" and cmd != "l" and cmd != "s":
            cmd = "i"
        
        if cmd == "l":
            try:
                with open('parameters.json') as f:
                    data = json.load(f)
            except:
                print("Can't load parameters from cached file, please input parameters with 'i' command and save with 's' at the end")
                cmd = "d"
                
        if cmd == "d":
            ballPosition = 0
            ballAcceleration = -8
            Rrim = 14
            Rdef = 13
            Rwheel = 11
            statorIncline = 28
            statorIncline = statorIncline*(3.14159265359/180);
            wheelPosition = 0
            wheelAcceleration = -0.12
            numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
            distRating = {}
            print("Setting default values:")
            print("Ball Position: "+str(ballPosition)+" (Degrees)")
            print("Ball Acceleration: "+str(ballAcceleration)+" (Inches/Sec^2)")
            print("Rrim Radius: "+str(Rrim)+" (Inches)")
            print("Deflectors Radius: "+str(Rdef)+" (Inches)")
            print("Wheel Radius: "+str(Rwheel)+" (Inches)")
            print("Stator Incline: "+str(statorIncline)+" (Degrees)")
            print("Wheel Position: "+str(wheelPosition)+" (Degrees)")
            print("Wheel Acceleration: "+str(wheelAcceleration)+" (Inches/Sec^2)")

            ballVelocity = 0
            wheelVelocity = 0
##            print("Saving to file parameters.json all parameters values")
##            data = { "ballPosition": ballPosition, "Rrim": Rrim, "Rdef": Rdef, "Rwheel": Rwheel, "statorIncline": statorIncline, "ballAcceleration": ballAcceleration, "wheelPosition": wheelPosition, "ballVelocity": ballVelocity, "wheelVelocity": wheelVelocity, "wheelAcceleration": wheelAcceleration }
##
##            with open('parameters.json', 'w') as f:
##                json.dump(data, f, ensure_ascii=False)
        elif cmd == "l":
            try:
                with open('parameters.json') as f:
                    data = json.load(f)

                ballPosition = data['ballPosition']
                ballAcceleration = data['ballAcceleration']
                Rrim = data['Rrim']
                Rdef = data['Rdef']
                Rwheel = data['Rwheel']
                statorIncline = data['statorIncline']
                wheelPosition = data['wheelPosition']
                wheelAcceleration = data['wheelAcceleration']
                distRating = data['distRating']
                numbers = data['numbers']
                print("Setting default values:")
                print("Ball Position: "+str(ballPosition)+" (Degrees)")
                print("Ball Acceleration: "+str(ballAcceleration)+" (Inches/Sec^2)")
                print("Rrim Radius: "+str(Rrim)+" (Inches)")
                print("Deflectors Radius: "+str(Rdef)+" (Inches)")
                print("Wheel Radius: "+str(Rwheel)+" (Inches)")
                print("Stator Incline: "+str(statorIncline)+" (Degrees)")
                print("Wheel Position: "+str(wheelPosition)+" (Degrees)")
                print("Wheel Acceleration: "+str(wheelAcceleration)+" (Inches/Sec^2)")
                print("Roulette Numbers: "+str(numbers))
                print("Distance between deflector number and winning number rating: "+str(distRating))
            except:
                print("No parameters found in cached file")
        elif cmd == "s":
            file = open('parameters.json', 'w+')
            data = { "numbersd" : numbers, "ballPosition": ballPosition, "Rrim": Rrim, "Rdef": Rdef, "Rwheel": Rwheel, "statorIncline": statorIncline, "ballAcceleration": ballAcceleration, "wheelPosition": wheelPosition, "ballVelocity": ballVelocity, "wheelAcceleration": wheelAcceleration }

            json.dump(data, file)
        elif cmd == "i":
            try:
                ballAcceleration = float(input("Please input ball acceleration (Default: -34.13 Inches/Sec^2):") or -34.13)
            except:
                ballAcceleration = -8

            try:
                Rrim = int(input("Please input Rrim radius (Default: 14 Inches):") or 14)
            except:
                Rrim = 14

            try:
                Rdef = int(input("Please input Rdef radius (Default: 13 Inches):") or 13)
            except:
                Rdef = 13

            try:
                Rwheel = int(input("Please input Rwheel radius (Default: 11 Inches):") or 11)
            except:
                Rwheel = 11

            try:
                statorIncline = int(input("Please input Stator Incline (Default: 28 Degrees):") or 28)
            except:
                statorIncline = 28

            statorIncline = float(statorIncline)*(3.14159265359/180);

            try:
                wheelAcceleration = float(input("Please input wheel acceleration (Default: -0.12 Inches/Sec^2):") or -0.12)
            except:
                wheelAcceleration = -0.12

            try:
                numbers = str(input("Please select 1 for american or 2 for european roulette:") or 1)
                if numbers == 1:
                    numbers = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]
                    print("The numbers list you entered is american: "+str(numbers))
                else:
                    numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
                    print("The numbers list you entered is european: "+str(numbers))
            except:
                numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]

            distRating = {}
            
            loaded = True

##        try:
##            startNumber = float(input("Please input start number of roulette:") or 26)
##        except:
##            startNumber = 26

        try:
            wheelPosition = int(input("Please input wheel position (angle) when t=0 (Default: 0 Degrees):") or 0)
        except:
            wheelPosition = 0 # Unknown

        try:
            wheelNumber = int(input("Please input the number on the wheel from which the wheel starts his orbit (angle) when t=0 (Default: 0 Degrees):") or 0)
        except:
            wheelNumber = 0 # Unknown

        try:
            ballPosition = int(input("Please input ball position (angle) when t=0 (Default: 0 Degrees):") or 0)
        except:
            ballPosition = 0

        ballPosition = (ballPosition/180) * 3.14

        try:
            wheelVelocity = input("Please input wheel velocity (Inches/Sec) when t=0 OR click okay for manual calculation:") or "Manual"
        except:
            wheelVelocity = "Manual"

        if wheelVelocity == "Manual":
            try:
                Time1 = input("Please click Ok when the Wheel starts a full circle:") or "OK"
            except:
                Time1 = "OK"
            T1 = float(time.time())
            try:
                Time2 = input("Please click Ok when the Wheel ends a full circle:") or "OK"
            except:
                Time2 = "OK"
            T2 = float(time.time())
            dt = T2 - T1
            wheelVelocity = float((2*3.14159265359*Rrim) / dt);
            print("Wheel Velocity: "+str(wheelVelocity))
        else:
            wheelVelocity = float(wheelVelocity)

        try:
            ballVelocity = input("Please input ball velocity (Inches/Sec) when t=0 OR click okay for manual calculation:") or "Manual"
        except:
            ballVelocity = "Manual"
        ##
        ##    while True:#making a loop
        ##        try: #used try so that if user pressed other than the given key error will not be shown
        ##            if keyboard.is_pressed('a'):#if key 'q' is pressed
        ##                print('You Pressed A Key!')
        ##                break#finishing the loop
        ##            else:
        ##                pass
        ##        except:
        ##            break #if user pressed a key other than the given key the loop will break

        if ballVelocity == "Manual":
            try:
                Time1 = input("Please click Ok when the Ball starts moving around the rim:") or "OK"
            except:
                Time1 = "OK"
            T1 = float(time.time())
            try:
                Time2 = input("Please click Ok when the Ball ends moving around the rim:") or "OK"
            except:
                Time2 = "OK"
            T2 = float(time.time())
            dt = T2 - T1
            ballVelocity = float((2*3.14159265359*Rrim) / dt);
            print("Ball Velocity: "+str(ballVelocity))
        else:
            ballVelocity = float(ballVelocity)

        #print("ballVelocity: "+str(ballVelocity))
        ballAcceleration = ballAcceleration/Rrim
        ballVelocityLinear = ballVelocity
        ballVelocity = ballVelocity/Rrim
        TrimCoefficient = -1/ballAcceleration;
        Gravity = 386.09;

        Trim = TrimCoefficient*(ballVelocity+math.sqrt( (Gravity/Rrim)*math.tan(statorIncline) ));
        #Trim2 = TrimCoefficient*(ballVelocity-math.sqrt( (Gravity/Rrim)*math.tan(statorIncline) ));
        #Trim = 18
        print("Trim: "+str(Trim))
        #print("Trim2: "+str(Trim2))
        #math.tan(statorIncline)
        Tdefl = Trim + ( (1/8)*2*3.14*Rrim / ballVelocityLinear );
        print("Tdefl: "+str(Tdefl))

        ballAngle = float(ballPosition) + (ballVelocity*Tdefl) + 0.5*(ballAcceleration*Tdefl*Tdefl);
        wheelAngle = float(wheelPosition) + (wheelVelocity*Tdefl) + 0.5*(wheelAcceleration*Tdefl*Tdefl);

        print("Total Ball Angle: "+str(ballAngle))
        print("Total Wheel Angle: "+str(wheelAngle))
        print("Number of circles of the Ball: "+str(ballAngle/(3.14*2)))
        ballCircles = ballAngle/(3.14*2)
        print("Angle of the ball at last circle from x-axis: "+str(ballAngle%(3.14*2) * (180/3.14)))
        print("Number of circles of the Wheel: "+str(wheelAngle/(3.14*2)))
        wheelCircles = wheelAngle/(3.14*2)
        print("Angle of the wheel at last circle from x-axis: "+str(wheelAngle%(3.14*2) * (180/3.14)))

        save = 0
        new_numbers_prepend = []
        new_numbers = []
        for num in numbers:
            if num == wheelNumber:
                save = 1
            if save == 1:
                new_numbers.append(num)
            if save == 0:
                new_numbers_prepend.append(num)

        new_numbers_final = []
        for num in new_numbers:
            new_numbers_final.append(num)
        for num in new_numbers_prepend:
            new_numbers_final.append(num)
        
        ballPosition = ballAngle%(3.14*2) * (180/3.14)
        wheelPosition = wheelAngle%(3.14*2) * (180/3.14)
        
        if ballPosition > wheelPosition:
            deg_for_num = 360 / len(numbers)
            testWheelPos = wheelPosition
            for num in reversed(new_numbers_final):
                testWheelPos += deg_for_num
                if testWheelPos > ballPosition:
                    ballNumber = num
                    break
        else:
            deg_for_num = 360 / len(numbers)
            testWheelPos = wheelPosition
            for num in new_numbers_final:
                testWheelPos -= deg_for_num
                if testWheelPos < ballPosition:
                    ballNumber = num
                    break

        print("Ball number in the deflectors:"+str(ballNumber))


##        lenNumbers = len(numbers)
##        for num in numbers:
##            if num == startNumber:
##                angle += (1/lenNumbers ) * 360
##                if angle > wheelAngle:
##                    selNumber = num
##                    break
##
##        echo "Selected Number: "+str(selNumber)


        # 0.029 * (43.98 +-sqrt(27.5*0.52) ) = 1.3862197423941090053994405037719
        # Tdefl = 1.41
        # 0.029 * (43.98 + 3.78)
        # Trim = 1.38

        try:
            winningNumber = int(input("Please input the winning number for the scatter distribution:") or 0)
        except:
            winningNumber = 0 # Unknown

        dist = 0
        found = False
        for num in numbers:
            if found == True:
                dist = dist + 1
            if num == ballNumber or num == winningNumber:
                if found == True:
                    break
                found = True

        print("Distance between Deflector Number ("+str(ballNumber)+") and Winning Number ("+str(winningNumber)+") is "+str(dist))

        ##distRating = {}
        try:
            distRating[dist] = distRating[dist] + 1
        except:
            distRating[dist] = 1
        
        print("Distance ratings are:")
        print(distRating)
        
        try:
            cmd = input("What do you want to do? Press 'p' to start a new game,\n'e' exit app,\n's' to save default values to file") or "p"
        except:
            cmd = "p"

        if cmd == "s":
            print("Saving to file parameters.json all parameters values")
            data = { "numbers" : numbers, "distRating" : distRating, "ballPosition": ballPosition, "Rrim": Rrim, "Rdef": Rdef, "Rwheel": Rwheel, "statorIncline": statorIncline, "ballAcceleration": ballAcceleration, "wheelPosition": wheelPosition, "ballVelocity": ballVelocity, "wheelVelocity": wheelVelocity, "wheelAcceleration": wheelAcceleration }

            with open('parameters.json', 'w') as f:
                json.dump(data, f, ensure_ascii=False)
        elif cmd == "e":
            break


if __name__ == '__main__':
    main()

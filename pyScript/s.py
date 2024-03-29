#MODULES
import win32api #GetAsyncKeyState is not detected
import time #only for delay
import winsound
from serial import Serial #arduino atmega32u4 ;)



#variables#
arduino = Serial('COM3', 9600)

def mouse_move(x, y):
    if x < 0: # 255 SINIR Yani 255 veriyorsa 1 veriyor demektir.
        x = x + 256
    if y < 0:
        y = y + 256
    pax = [x,y]
    arduino.write(pax)


                                                     
                                              
                                                            


#M2- delay (0.0000011) ve sensivity = 0.6
xm2 = [0,0,0,0,0]
ym2 = [1,1,1,1,1]

mp5x = [0,0,0,0,0,0,0,0,0,1,1,1,3,4,4,4,3,4,4,4,4,4,4,3,3,3,2,2,-1,-1,-2,-2,-3,-3,-3,-2,-3,-3,-3,-2,-2,-1,-1,-1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,0,-1,-1,-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1,-2,-2,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-2,-2,-1,-1,-2,-1,-1,-1,-2,-2,-1,-1,-1,-1,-1,-1]
mp5y = [3,3,4,4,4,5,5,4,4,4,4,5,5,5,4,4,4,4,3,3,4,3,3,3,3,3,2,2,2,2,1,1,2,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

thmpx = [-1,-1,-1,-1,-2,-1,-1,-1,0,1,0,1,1,1,2,2,1,1,2,2,2,2,1,1,0,1,0,0,-1,-1,-2,-2,-2,-2,-1,-1,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,2,2,2,2,2,2,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
thmpy = [4,4,5,5,5,5,4,4,5,5,5,4,5,5,4,4,4,4,4,4,4,4,3,3,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,1,2,2,1,1,2,2,1,1,2,2,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1]

#New Recoil Tables

sarx = [0,0]
sary = [8,7]
sardelay=[0.027,0.027]

mp5x = [0,0,0,0,0,0,0,0,1,1,1,1,4,5,5,5,5,5,5,4,5,5,5,4,3,3,3,3,-1,-2,-2,-2,-3,-3,-4,-4,-4,-4,-3,-3,-2,-2,-2,-1,0,0,-3,-2,-2,-2,-2,-1,0,0,0,0,0,0,0,0,2,2,3,3,3,3,3,3,2,2,3,3,3,3,3,4,4,3,3,3,3,3,2,2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,-2,-2,-1,-2,-2,-2,-2,-2,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-2,-2,-2,-1,-1,-1,-1,-2]
mp5y = [8,5,5,5,5,5,6,6,5,6,6,5,6,6,5,5,5,5,4,4,4,4,4,4,3,3,3,3,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,1,2,1,1,2,2,2,1,2,1,1,1,2,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mp5delay=[0.048,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024,0.023,0.024,0.024,0.024]


thompson2x=[-2,-2,-2,-2,-2,-1,-1,0,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-2,-1,-1,-1,-1,-1,-1,-1,2,2,3,3,2,2,2,1,1,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
thompson2y=[11,6,6,6,6,6,5,6,6,6,5,6,6,5,5,5,5,5,5,5,5,4,4,3,3,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1,2,2,1,1,2,1,1,1,2,2,1,1,2,1,1,1,2,2,1,1,2,1,1,1,2,2,1,1]
thompsondelay=[0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,0.029,]


lrx=[-1,-1,-1,-1,-1,-2,-3,-4,-4,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,0,1,1,4,5,5,5,5,4,5,5,4,4,3,3,0,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-4,-3,-3,-4,-4,-3,-3,-3,-3,-2,-3,-3,-2,-3,-2,-2,-1,0,0,0,0,0,7,7,8,8,7,7,8,7,7,8,7,7]
lry=[8,8,8,8,8,8,8,8,8,8,9,9,9,9,4,4,4,4,4,3,2,2,2,2,2,2,2,2,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,1,0,0,1]

akx=[ -3, -3, -3, -3, -3, -3, -2, -2, -2, -2, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, -5, -4, -4, -4, -4, -4, -4, -4, -4, -4, 0, -4, -4, -3, -3, -3, -3, -3, -3, -3, -3, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 0, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -3, -2, -2, -2, -2, -2, -2, -2, -2, -2, 0, -3, -3, -3, -3, -3, -3, -3, -2, -2, -2, 0, -4, -4, -4, -3, -3, -3, -3, -3, -3, -3, 0, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3, 0, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3, 0, -4, -4, -3, -3, -3, -3, -3, -3, -3, -3, 0, -3, -3, -3, -3, -3, -3, -2, -2, -2, -2, 0, -2, -2, -2, -2, -2, -2, -2, -2, -1, -1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 0, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 0, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
aky=[4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 0, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 0, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 0, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 0, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]


ak = False
lr = False
sar = False
m2 = False
mp5 = False
thommy = False

frequency = 1000
soundTime = 200


def baslangic():
    global ak
    global lr
    global sar
    global m2
    global mp5
    global thommy

    def doak():
        while ak == True:
            if win32api.GetAsyncKeyState(0x24) < 0:
                time.sleep(0.5)
                print("DISCONNECTING...")
                baslangic()
                break
            for i in range(len(akx)):
                if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) <0:
                    mouse_move(akx[i] * 2,aky[i] * 2) 
                    time.sleep(0.011)        
                else:
                    break
    def dolr():
        while lr ==True:
            if win32api.GetAsyncKeyState(0x24) < 0:
                time.sleep(0.5)
                print("DISCONNECTING...")
                winsound.Beep(frequency, soundTime)
                baslangic()
                break
            for i in range(len(lrx)):  #this path for changing recoil table#
                if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) <0:
                    mouse_move(lrx[i],lry[i]) #this path for changing recoil table#
                    time.sleep(0.040)
                else:
                    break
    def dosar():
        while sar == True:
            if win32api.GetAsyncKeyState(0x24) < 0: # Tab button for open menu ( you can change it)
                time.sleep(0.5)
                print("DISCONNECTING...")
                baslangic()
                break
            for i in range(len(sarx)):  #
                if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) <0:
                    mouse_move(sarx[i],sary[i]) #this path for changing recoil table#
                    time.sleep(sardelay[i])
                else:
                    break
    def dom2():
        while m2 == True:
            if win32api.GetAsyncKeyState(0x24) < 0:
                time.sleep(0.5)
                print("DISCONNECTING...")
                baslangic()
                break
            for i in range(len(xm2)):
                if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) <0:
                    mouse_move(xm2[i],ym2[i])
                    time.sleep(0.0000011)
                else:
                    break
    def domp5():
        while mp5 == True:
            if win32api.GetAsyncKeyState(0x24) < 0:
                time.sleep(0.5)
                print("DISCONNECTING...")
                baslangic()
                break
            for i in range(len(mp5x)):
                if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) < 0:
                    mouse_move(mp5x[i],mp5y[i])
                    time.sleep(0.025)
                else:
                    break
    def dothommy():
        while thommy == True:
            if win32api.GetAsyncKeyState(0x24) < 0:
                time.sleep(0.5)
                print("DISCONNECTING...")
                baslangic()
                break
            for i in range (len(thmpx)):
                if win32api.GetAsyncKeyState(0x01) < 0 and win32api.GetAsyncKeyState(0x02) <0:
                    mouse_move(thmpx[i],thmpy[i])
                    time.sleep(0.020)
                else:
                    break

    baslat = input("CHOOSE YOUR WEAPON ...:")
    if baslat == "1":
        print("AK IS READY TO USE!")
        ak = True
        doak()
    elif baslat == "2":
        print("LR IS READY TO USE!")
        lr = True
        dolr()
    elif baslat =="3":
        print("SAR IS READY TO USE!")
        sar = True
        dosar()
    elif baslat == "4":
        print("M2 IS READY TO USE!")
        m2 = True
        dom2() 
    elif baslat == "5":
        print("MP5 IS READY TO USE!")
        mp5 = True
        domp5()
    elif baslat == "6":
        print("THOMPSON IS READY TO USE!")
        thommy = True
        dothommy()
    else:
        print("ERROR!")
    




print("     ▄  ▄███▄      ▄   ████▄    ▄▄▄▄▄    ▄  █   ▄   ") 
print("▀▄   █ █▀   ▀      █  █   █   █     ▀▄ █   █    █ ")
print("  █ ▀  ██▄▄    ██   █ █   █ ▄  ▀▀▀▀▄   ██▀▀█ █   █ ")
print(" ▄ █   █▄   ▄▀ █ █  █ ▀████  ▀▄▄▄▄▀    █   █ █   █ ")
print("█   ▀▄ ▀███▀   █  █ █                     █  █▄ ▄█ ")
print(" ▀             █   ██                    ▀    ▀▀▀  ")                                                                                                           
print(" ")
print("AK = 1   ~~   LR = 2   ~~   SAR = 3   ~~   M2 = 4   ~~   MP5 = 5   ~~   THOMPSON = 6")
print("WELCOME TO HUMANIZED RECOIL CONTROL SYSTEM!")
baslangic()




 




                                                   
















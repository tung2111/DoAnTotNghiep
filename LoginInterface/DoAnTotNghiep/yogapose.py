
import  cv2, os
import time
import practies as pr
import numpy as np
import texttime as tt
from datetime import datetime



detector = pr.poseDetector()
giayquakhu =0
dem =  0
z =1    # chon dong tac yoga 1
check = False   #kiem tra dong tac yoga dung/sai
cap = ''
def init(a):
    global cap, detector
    if (a):
        print("bat cam")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    else:
        print("tat cam")
        cap = ''

#print (img.shape)  # h, w, c

def dem_thoigian(time):
    global giayquakhu, dem,z
    # dd/mm/YY H:M:S
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    giayhientai = tt.giay
    if giayhientai != giayquakhu:
        giayquakhu = giayhientai
        dem = dem + 1
        if dem == time+1:   # khi dem = so giay quy dinh .khong che cac tu the yoga
            dem =0          # giay tra ve 0
            z +=1           # tang thu tu dong tac lenh
            if z==5:        #
                z=1
    return dem, z

def run(x,y,z):
    global detector, cap, overlayList,dem, check
    success, image = cap.read()
    image = cv2.flip(image, 2)
    image = cv2.resize(image, (1280, 720))
    image = detector.findPose(image,False)
    lmList =detector.findPosition(image,False)
    if len(lmList) !=0:
        arm_r = detector.findAngle(image, 12, 14, 16)
        arm_l = detector.findAngle(image, 11, 13, 15)
        upbody_r = detector.findAngle(image, 24, 12, 14)
        upbody_l = detector.findAngle(image, 23, 11, 13)
        knee_r = detector.findAngle(image, 24, 26, 28)
        knee_l = detector.findAngle(image, 23, 25, 27)
        hip_r = detector.findAngle(image, 12, 24, 26)
        # arm_l = detector.findAngle(image, 11, 13, 15)
        knee_l1 = detector.findAngle(image, 11, 23, 25)

        # Pose Warrior
        if z==1:
            per_arm_r = np.interp(arm_r, (175, 185), (0, 100))
            per_arm_l = np.interp(arm_l, (177, 180), (0, 100))
            # per_upbody_r = np.interp(upbody_r, (90, 105), (0, 100))
            # per_upbody_l = np.interp(upbody_l, (270, 280), (100, 0))
            per_knee_r = np.interp(knee_r, (125, 125), (100, 0))
            per_knee_l = np.interp(knee_l, (170, 200), (0, 100))
            if (per_arm_r > 20 and per_arm_l > 20 and per_knee_r > 20 and per_knee_l > 20):
                #dem time
                check = True
                tt.enabletimer = True
                # time_hen, z = dem_thoigian(time)

            else:
                dem = 0
                check = False
                tt.enabletimer = False


        # Pose Tree
        elif (z == 2):
            per_arm_r = np.interp(arm_r, (25, 80), (100, 0))
            per_arm_l = np.interp(arm_l, (200, 325), (0, 100))
            # per_upbody_r = np.interp(upbody_r, (45, 70), (100, 0))  # vai phai
            # per_upbody_l = np.interp(upbody_l, (309, 290), (0, 100))
            per_knee_r = np.interp(knee_r, (30, 68), (100, 0))
            per_knee_l = np.interp(knee_l, (170, 190), (0, 100))
            per_hip_r = np.interp(hip_r, (250, 260), (0, 100))
            if (per_arm_r > 20 and per_arm_l > 20 and per_knee_r > 20 and per_knee_l > 20 and per_hip_r > 10):
                check = True
                tt.enabletimer = True
                # time_hen, z = dem_thoigian(time)

            else:
                dem = 0
                check = False
                tt.enabletimer = False
         #Pose Triangle
        elif (z == 3):
            per_arm_r = np.interp(arm_r, (184, 194), (0, 100))
            per_arm_l = np.interp(arm_l, (154, 178), (100, 0))
            # per_upbody_r = np.interp(upbody_r, (80, 94), (0, 100))  # vai phai
            # per_upbody_l = np.interp(upbody_l, (274, 300), (100, 0))
            per_knee_r = np.interp(knee_r, (160, 178), (0, 100))
            per_knee_l = np.interp(knee_l, (180, 190), (0, 100))
            per_hip_r = np.interp(hip_r, (136, 186), (100, 0))
            if (per_arm_r > 20 and per_arm_l > 20 and per_knee_r > 20 and per_knee_l > 20 and per_hip_r > 10):
                check = True
                tt.enabletimer = True
                # time_hen, z = dem_thoigian(time)
            else:
                dem = 0
                check = False
                tt.enabletimer = False

        # Plank ( khu???u tay)
        elif z == 5:
            per_arm_l = np.interp(arm_l, (260, 300), (0, 100))
            per_knee_l = np.interp(knee_l1, (175, 200), (0, 100))
            if (per_arm_l > 20 and per_knee_l > 20):
                # dem time
                check = True
                tt.enabletimer = True
                # time_hen, z = dem_thoigian(time)

            else:
                dem = 0
                check = False
                tt.enabletimer = False
        #Plank ( ch???ng th???ng tay)
        elif z == 4:
            per_arm_l = np.interp(arm_l, (200, 220), (0, 100))
            per_knee_l = np.interp(knee_l1, (175, 200), (0, 100))

            if (per_arm_l > 20 and per_knee_l > 20):
                # dem time
                check = True
                tt.enabletimer = True
                # time_hen, z = dem_thoigian(time)

            else:
                dem = 0
                check = False
                tt.enabletimer = False
        # Pose Boat
        elif z == 6:
            per_arm_l = np.interp(arm_l, (185, 195), (0, 100))
            per_knee_l = np.interp(knee_l1, (250, 260), (0, 100))
            if (per_arm_l > 20 and per_knee_l > 20):
                # dem time
                check = True
                tt.enabletimer = True
                # time_hen, z = dem_thoigian(time)

            else:
                dem = 0
                tt.enabletimer = False
        # Cobra Pose
        elif z == 7:

            per_arm_l = np.interp(arm_l, (200, 210), (0, 100))
            per_knee_l = np.interp(knee_l1, (135, 145), (0, 100))

            if (per_arm_l > 20 and per_knee_l > 20):
                # dem time
                check = True
                tt.enabletimer = True
                # time_hen, z = dem_thoigian(time)

            else:
                dem = 0
                check = False
                tt.enabletimer = False

        # elif (z == 8):
        #     cv2.rectangle(image, (10, 450), (650, 650), (170, 232, 238), cv2.FILLED)
        #     cv2.putText(image, f"HOAN THANH" , (20, 600),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 15)


    image = cv2.resize(image, (x, y))
    return image, check, dem, z

import cv2, time
import numpy as np
from practies import poseDetector


cap = ''
detector = poseDetector()
count = 0
rep_up = 0
pTime = 0
per = 0

def init(a):
    global cap, detector, count
    if (a):
        print("bat cam")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    else:
        print("tat cam")
        cap = ''   # giai phong cap.realease
        count = 0


def run(x, y, z):   #x, y la resize kichs thuoc     z: quy dinh cac chuc nang chuong trinh
    global count, rep_up, pTime, detector,cap, per,per_l,per_r
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    start = time.time()
    success, img = cap.read()



    img = cv2.resize(img, (1192, 617))
    img = cv2.flip(img, 2)
    img = detector.findPose(img, draw=False)
    lmList= detector.findPosition(img, draw=False)
    if len(lmList)!=0:
        #dumbell shoulder
        if z == 4:
            wrist = []
            dumbelstatus = True
            if len(lmList) != 0:
                arm_r = detector.findAngle(img, 12, 14, 16)
                arm_l = detector.findAngle(img, 11, 13, 15)
                upbody_r = detector.findAngle(img, 24, 12, 14, False)
                upbody_l = detector.findAngle(img, 23, 11, 13, False)
                per_l = np.interp(upbody_l, (235, 270), (100, 0))
                per_r = np.interp(upbody_r, (95, 124), (0, 100))
                per = per_r
                if lmList[11][2] > lmList[14][2]:  # khuy tay cao hon vai
                    wrist.append(
                        [lmList[14][1], lmList[14][2] - detector.lenght(img, 14, 16)])  # ve co tay chuan ben phai
                    wrist.append(
                        [lmList[13][1], lmList[13][2] - detector.lenght(img, 14, 16)])  # ve co tay chuan trai
                    angle_r = detector.cosin2goc(img, wrist[0], 14, 16)
                    angle_l = detector.cosin2goc(img, wrist[1], 13, 15)


        #barbel crul
        if z== 2:
            #right arm
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle,(220,300),(0,100))
            bar = np.interp(angle,(220,300),(650,100))
            dumbelstatus = False
        elif z==0:
            # left arm
            angle = detector.findAngle(img, 12, 14, 16)
            per = np.interp(angle, (50, 140), (100, 0))
            bar = np.interp(angle, (50, 140), (100, 650))
            dumbelstatus = False
        #  Leg raise
        elif z==9:
            #abs
            angle = detector.findAngle(img, 11, 23, 25)
            per = np.interp(angle, (190, 240), (0, 100))
            bar = np.interp(angle, (190, 240), (650, 100))
            dumbelstatus = False
        elif z==5:
            # squat
            angle = detector.findAngle(img,24,26,28)
            per = np.interp(angle,(190,260),(0,100))
            bar = np.interp(angle,(190,260),(650,100))
            dumbelstatus = False
        elif z == 1:
            # pushup hit dat
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (220, 310), (0, 100))
            bar = np.interp(angle, (220, 310), (650, 100))
            angle1 = detector.findAngle(img, 11, 23, 25)
            per1 = np.interp(angle1, (150, 180), (100, 0))
            dumbelstatus = False
        #Skull crusher (taysau +ghế)
        elif z == 6:
            #tay trái
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (220, 280), (0, 100))
            bar = np.interp(angle, (220, 280), (650, 100))
            angle1 = detector.findAngle(img, 11, 23, 25)
            dumbelstatus = False
        elif z == 7:
            #tay phãi
            angle = detector.findAngle(img, 12, 14, 16)
            per = np.interp(angle, (80, 130), (100, 0))
            bar = np.interp(angle, (80, 130), (100, 650))
            angle1 = detector.findAngle(img, 12, 24, 26)
            dumbelstatus = False
        # Crunch gập bụng
        elif z == 8:
            angle = detector.findAngle(img, 11, 23, 25)
            per = np.interp(angle, (230, 270), (0, 100))
            bar = np.interp(angle, (230, 270), (650, 100))
            dumbelstatus = False
        # Dumbbell flyes (ngực trước với tạ đơn)
        elif z == 3:
            angle = detector.findAngle(img, 13, 11, 23)
            per = np.interp(angle, (290, 340), (100, 0))
            bar = np.interp(angle, (290, 340), (100, 650))
            dumbelstatus = False


        #check for rep
        color = (255,0,255)
        if per == 100:
            color = (255,0,255)
            if rep_up==0:
                count+=0.5
                rep_up =1
        if per == 0:
            color = (0, 255, 0)
            if rep_up == 1:
                count+=0.5
                rep_up = 0
        if(dumbelstatus == True):
            if (per_l == 100 and per_r == 100):
                color = (255, 0, 255)
                if rep_up == 0:
                    count += 0.5
                    rep_up = 1
            if (per_l == 0 and per_r == 0):
                color = (0, 255, 0)
                if rep_up == 1:
                    count += 0.5
                    rep_up = 0
#ve bar
        if dumbelstatus == False:
            cv2.rectangle(img, (1100,100),(1160,600),(255,255,255),1)
            cv2.rectangle(img, (1100, int(bar)), (1160, 600), (102,255,102), cv2.FILLED)
            cv2.putText(img,f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 3)

    img = cv2.resize(img, (x, y))
    # # End time
    # end = time.time()
    #
    # # Time elapsed
    # seconds = end - start
    # print ("Time taken : {0} seconds".format(seconds))
    #
    # # Calculate frames per second
    # fps  = 1 / seconds
    # print("Estimated frames per second : {0}".format(fps))
    # cv2.putText(img, f'{int(fps)} FPS', (70, 75), cv2.FONT_HERSHEY_PLAIN, 4,
    #             (0, 0, 255), 3)
    return img, per, count




import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtWidgets, QtCore
# from PyQt5.uic.properties import QtGui
import sys, time, threading, playsound, winsound
from PySide2 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PySide2.QtGui import QPixmap, QColor
import firebase_admin
from PySide2.QtGui import QColor, QIcon,QPalette
from PySide2.QtWidgets import *
from PySide2.QtMultimediaWidgets import QVideoWidget
from win32con import WM_DESTROY
from win32gui import RegisterClass, GetModuleHandle
from winxpgui import WNDCLASS

import home, fillprofile, MainMenu, login, welcomescreen, createacc, Setting, Gym, ui_splash_screen, timetable, Calo, \
    Mealselect,Yoga,MealSelectDinner,MealSelectLunch,MealSelectBreakFast
import barbell_cruls as bc
import yogapose as yp
import texttime as tt
from firebase_admin import credentials, db
import sqlite3
import chat_client
from PySide2.QtCore import Qt, QUrl
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from win10toast import ToastNotifier
import time
from datetime import datetime
Name=''
CaloNeed = 0
Height = 0
Age = 0
Weight = 0
Index = 0
TocalCalo = 0
ListMeal = []
CheckboxMeal=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

ListMealLunch = []
CheckboxMealLunch=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

ListMealDinner = []
CheckboxMealDinner=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
              False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
counter = 0
jumper = 10
progress_val = 0
user = ""
password = ""
confirmpassword = ""
i = 0
func = 0
func_yoga=0
rep = 0
ui = ''
cp = 0
img = ''
Image_TimeTable = 0
flagRight = 1  # 1 la co the bac RIGHT
check = False  # kiem tra yoga dung sai
check2 = False  # khong che nhac
giay_tt = False
z = 0
y = 0
#variable for notification
status = True
# declare object to notify
toast = ToastNotifier()
# define global variabl to store Total Calo
CaloBreakFast = 0
CaloLunch = 0
CaloDinner = 0
IMG = ["border-image : url(:/Image/hit-dat.jpg)\n;", "border-image : url(:/Image/dumbbell_shoulder.jpg);\n",
       "border-image: url(:/Image/nguc-truoc-voi-ta-don.jpg);\n",
       "border-image: url(:/Image/ta-don1.jpg);\n", "border-image : url(:/Image/tay-sau-voi-ghe.jpg);\n",
       "border-image : url(:/Image/swat.jpg);\n"
    , "border-image: url(:/Image/gap-bung.jpg);\n", "border-image : url(:/Image/blank-thang-tay.jpg);\n"]
Mon = ["border-image : url(:/Image/hit-dat.jpg);\n", "border-image : url(:/Image/hit-dat.jpg);\n",
       "border-image: url(:/Image/nguc-truoc-voi-ta-don.jpg);\n"]
Tue = ["border-image: url(:/Image/ta-don1.jpg);\n", "border-image : url(:/Image/tay-sau-voi-ghe.jpg);\n",
       "border-image : url(:/Image/swat.jpg);\n"]
Wed = ["border-image : url(:/Image/nguc-truoc-voi-ta-don.jpg);\n", "border-image: url(:/Image/swat.jpg);\n",
       "border-image :url(:/Image/tay-sau-voi-ghe.jpg);\n"]
Thurs = ["border-image: url(:/Image/hit-dat.jpg);\n", "border-image : url(:/Image/blank-thang-tay.jpg);\n",
         "border-image: url(:/Image/gap-bung.jpg);\n"]
Fri = ["border-image : url(:/Image/dumbbell_shoulder.jpg);\n", "border-image : url(:/Image/tay-sau-voi-ghe.jpg);\n",
       "border-image: url(:/Image/swat.jpg);\n"]
Sat = ["border-image: url(:/Image/hit-dat.jpg);\n", "border-image : url(:/Image/gap-bung.jpg);\n",
       "border-image: url(:/Image/tay-sau-voi-ghe.jpg);\n"]

cred = credentials.Certificate("firebase-sdk.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://fitnessapp-5b974-default-rtdb.firebaseio.com/'})
# read timetable data
File_Mon = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Mon.txt","r")
File_Tue = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Tue.txt","r")
File_Wed = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Wed.txt","r")
File_Thurs = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Thurs.txt","r")
File_Fri = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Fri.txt","r")
File_Sat = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Sat.txt","r")
for size in range(len(Mon)):
    Mon[size] = File_Mon.readline()
    Tue[size] = File_Tue.readline()
    Wed[size] = File_Wed.readline()
    Thurs[size] = File_Thurs.readline()
    Fri[size] = File_Fri.readline()
    Sat[size] = File_Sat.readline()
#close file
File_Mon.close()
File_Tue.close()
File_Wed.close()
File_Thurs.close()
File_Fri.close()
File_Sat.close()


checkbox = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox.txt","r")
ListMealWidget = open(r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal.txt","r")
for indexCheckbox in range(69):
    if checkbox.readline() == 'True\n':
        CheckboxMeal[indexCheckbox] =    True
    else:
        CheckboxMeal[indexCheckbox] =    False

        #
number = 0
for indexmeal in range(10):
    LoadMealFromFile = ListMealWidget.readline().strip('\n')
    if LoadMealFromFile != '':
        ListMeal.append(LoadMealFromFile)

print (ListMeal)
#close file
checkbox.close()
ListMealWidget.close()
# ref = db.reference('/')
# ref.set({
#     '1':{
#         'User': 'tung',
#         'Password': '123'
#     },
#     '2':{
#         'User': 'vuong',
#         'Password': '123'
#     },
#     '3': {
#         'User': 'vuong',
#         'Password': '123'
#     }

# })
# Get CurrentTime
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

print("Current Time is :", current_time)

def LoginScreen():
    global ui
    MainWindow.setFixedSize(800, 450)
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
    ui.login.clicked.connect(loginfunction)



def loginfunction():
    global Name,Weight,Height,Age,CaloNeed
    user = ui.emailfield.text()
    password = ui.passwordfield.text()
    if len(user) == 0 or len(password) == 0:
        ui.error.setText("Please input all fields.")

    else:
        for i in range(1, 3):
            User = db.reference(str(i) + '/User').get()
            Password = db.reference(str(i) + '/Password').get()
            print()
            if (Password == password) and (User == user):
                print("Successfully logged in.")
                Name = db.reference(str(user) + '/Name').get()
                Weight = db.reference(str(user) + '/Weight').get()
                Height = db.reference(str(user) + '/Height').get()
                Age = db.reference(str(user) + '/Age').get()
                CaloNeed = db.reference(str(user) + '/CaloNeed').get()
                # ui.error.setText("Login Success")
                MainWindowSceen()
                break;
            else:
                ui.error.setText("Invalid username or password")


def LoadmainScreen():
    global cp
    cp = 0
    yp.init(0)
    bc.init(0)
    #savedata
    File_Mon = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Mon.txt", "w")
    File_Tue = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Tue.txt", "w")
    File_Wed = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Wed.txt", "w")
    File_Thurs = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Thurs.txt", "w")
    File_Fri = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Fri.txt", "w")
    File_Sat = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Sat.txt", "w")
    for size in range(len(Mon)):
        File_Mon.writelines(Mon[size])
        File_Tue.writelines(Tue[size])
        File_Wed.writelines(Wed[size])
        File_Thurs.writelines(Thurs[size])
        File_Fri.writelines(Fri[size])
        File_Sat.writelines(Sat[size])
        #close file
    File_Mon.close()
    File_Tue.close()
    File_Wed.close()
    File_Thurs.close()
    File_Fri.close()
    File_Sat.close()
    #load mainwindow
    MainWindowSceen()


def UpdateProfile():
    global ui,CaloNeed
    ui = fillprofile.Ui_MainWindow()
    MainWindow.setFixedSize(1201, 801)
    ui.setupUi(MainWindow)

    Name = db.reference(str(user) + '/Name').get()
    Weight = db.reference(str(user) + '/Weight').get()
    Height = db.reference(str(user) + '/Height').get()
    Age = db.reference(str(user) + '/Age').get()
    CaloNeed = int(db.reference(str(user) + '/CaloNeed').get())
    #wait

    ui.username.setText(str(Name))
    ui.Height_2.setText(str(Height))
    ui.Age.setText(str(Age))
    ui.Weight.setText(str(Weight))
    ui.signup.clicked.connect(getdatafrominput)


def getdatafrominput():
    global Weight,CaloNeed,Height,Age,Name

    Name = str(ui.username.text())
    Weight = int(ui.Weight.text())
    Height = int(ui.Height_2.text())
    Age = int(ui.Age.text())
    CaloNeed = int(((Weight * 13.397) + (4.799 * Height) - (5.677 * Age) + 447.593) * 1.55)
    ref = db.reference('/')
    ref.update({
        str(user):{
                'Name'   : str(Name),
                'Height' : Height,
                'Weight' : Weight,
                'Age'    : Age,
                'CaloNeed' :CaloNeed
        }})




def ChangePassWord():
    print("ChangePass")


def TimeTableFunction():
    global ui
    ui = timetable.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Back_TimeTable.clicked.connect(LoadmainScreen)

    ui.pushButton.setStyleSheet(Mon[0])
    ui.pushButton_2.setStyleSheet(Mon[1])
    ui.pushButton_3.setStyleSheet(Mon[2])
    ui.pushButton_4.setStyleSheet(Tue[0])
    ui.pushButton_5.setStyleSheet(Tue[1])
    ui.pushButton_6.setStyleSheet(Tue[2])
    ui.pushButton_7.setStyleSheet(Wed[0])
    ui.pushButton_8.setStyleSheet(Wed[1])
    ui.pushButton_9.setStyleSheet(Wed[2])
    ui.pushButton_10.setStyleSheet(Thurs[0])
    ui.pushButton_11.setStyleSheet(Thurs[1])
    ui.pushButton_12.setStyleSheet(Thurs[2])
    ui.pushButton_13.setStyleSheet(Fri[0])
    ui.pushButton_14.setStyleSheet(Fri[1])
    ui.pushButton_15.setStyleSheet(Fri[2])
    ui.pushButton_16.setStyleSheet(Sat[0])
    ui.pushButton_17.setStyleSheet(Sat[1])
    ui.pushButton_18.setStyleSheet(Sat[2])

    # Monday
    ui.pushButton.clicked.connect(changeImageMonIMG0)
    ui.pushButton_2.clicked.connect(changeImageMonIMG2)
    ui.pushButton_3.clicked.connect(changeImageMonIMG3)

    # Tuesday
    ui.pushButton_4.clicked.connect(changeImageTueIMG4)
    ui.pushButton_5.clicked.connect(changeImageTueIMG5)
    ui.pushButton_6.clicked.connect(changeImageTueIMG6)

    # Wed
    ui.pushButton_7.clicked.connect(changeImageWedIMG7)
    ui.pushButton_8.clicked.connect(changeImageWedIMG8)
    ui.pushButton_9.clicked.connect(changeImageWedIMG9)
    # Thurs
    ui.pushButton_10.clicked.connect(changeImageThursIMG10)
    ui.pushButton_11.clicked.connect(changeImageThursIMG11)
    ui.pushButton_12.clicked.connect(changeImageThursIMG12)
    # Fri
    ui.pushButton_13.clicked.connect(changeImageFriIMG13)
    ui.pushButton_14.clicked.connect(changeImageFriIMG14)
    ui.pushButton_15.clicked.connect(changeImageFriIMG15)
    # Sat
    ui.pushButton_16.clicked.connect(changeImageSatIMG16)
    ui.pushButton_17.clicked.connect(changeImageSatIMG17)
    ui.pushButton_18.clicked.connect(changeImageSatIMG18)


def changeImageMonIMG0():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Mon[0] = IMG[Image_TimeTable]
    ui.pushButton.setStyleSheet(Mon[0])


def changeImageMonIMG2():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Mon[1] = IMG[Image_TimeTable]
    ui.pushButton_2.setStyleSheet(Mon[1])


def changeImageMonIMG3():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Mon[2] = IMG[Image_TimeTable]
    ui.pushButton_3.setStyleSheet(Mon[2])


def changeImageTueIMG4():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Tue[0] = IMG[Image_TimeTable]
    ui.pushButton_4.setStyleSheet(Tue[0])


def changeImageTueIMG5():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Tue[1] = IMG[Image_TimeTable]
    ui.pushButton_5.setStyleSheet(Tue[1])


def changeImageTueIMG6():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Tue[2] = IMG[Image_TimeTable]
    ui.pushButton_6.setStyleSheet(Tue[2])


def changeImageWedIMG7():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Wed[0] = IMG[Image_TimeTable]
    ui.pushButton_7.setStyleSheet(Wed[0])


def changeImageWedIMG8():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Wed[1] = IMG[Image_TimeTable]
    ui.pushButton_8.setStyleSheet(Wed[1])


def changeImageWedIMG9():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Wed[2] = IMG[Image_TimeTable]
    ui.pushButton_9.setStyleSheet(Wed[2])


def changeImageThursIMG10():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Thurs[0] = IMG[Image_TimeTable]
    ui.pushButton_10.setStyleSheet(Thurs[0])


def changeImageThursIMG11():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Thurs[1] = IMG[Image_TimeTable]
    ui.pushButton_11.setStyleSheet(Thurs[1])


def changeImageThursIMG12():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Thurs[2] = IMG[Image_TimeTable]
    ui.pushButton_12.setStyleSheet(Thurs[2])


def changeImageFriIMG13():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Fri[0] = IMG[Image_TimeTable]
    ui.pushButton_13.setStyleSheet(Fri[0])


def changeImageFriIMG14():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Fri[1] = IMG[Image_TimeTable]
    ui.pushButton_14.setStyleSheet(Fri[1])


def changeImageFriIMG15():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Fri[2] = IMG[Image_TimeTable]
    ui.pushButton_15.setStyleSheet(Fri[2])


def changeImageSatIMG16():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Sat[0] = IMG[Image_TimeTable]
    ui.pushButton_16.setStyleSheet(Sat[0])


def changeImageSatIMG17():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Sat[1] = IMG[Image_TimeTable]
    ui.pushButton_17.setStyleSheet(Sat[1])


def changeImageSatIMG18():
    global Image_TimeTable
    if Image_TimeTable <= 6:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Sat[2] = IMG[Image_TimeTable]
    ui.pushButton_18.setStyleSheet(Sat[2])



def GymFunction():
    global ui,cp
    global volume
    volume = 0
    ui = Gym.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # t = threading.Thread(target=main)
    # t.start()
    ui.Start.clicked.connect(lambda: count_task(z))
    ui.back.clicked.connect(LoadmainScreen)
    ui.mute_2.clicked.connect(mute)
    ui.comboBox.currentTextChanged.connect(comboboxFuntion)
    ui.SeeVideo.clicked.connect(MediaPlayer)



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('player.png'))

        p =self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.init_ui()


        self.show()


    def init_ui(self):

        #create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)


        #create videowidget object

        videowidget = QVideoWidget()


        #create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)



        #create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)



        #create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)



        #create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)


        #create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0,0,0,0)

        #set widgets to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)



        #create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)


        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)


        #media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video",r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\VideoGuide\video-dong-tac-gym")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)



    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()



    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )

    def position_changed(self, position):
        self.slider.setValue(position)


    def duration_changed(self, duration):
        self.slider.setRange(0, duration)


    def set_position(self, position):
        self.mediaPlayer.setPosition(position)


    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

def MediaPlayer():
    global  DisplayMedia
    DisplayMedia = Window()


def comboboxFuntion():
    global z
    string = ui.comboBox.currentText()
    if string == "Barbell Cruls Left":
        z = 0
    elif string == "Push Up":
        z = 1
    elif string == "Barbell Cruls Right":
        z = 2
    elif string == "Dumbbell flyes":
        z = 3
    elif string == "Dumbbell_shoulder":
        z = 4
    elif string == "Swat":
        z = 5
    elif string == "Skull Crusher Left":
        z = 6
    elif string == "Skull Crusher Right":
        z = 7
    elif string == "Crunch":
        z = 8
    else :
        z = 9


def comboboxFuntionYoga():
    global y
    string = ui.comboBox_yoga.currentText()
    if string == "Warrior pose":
        y = 0
    elif string == "Tree pose":
        y = 1
    elif string == "Triangle poset":
        y = 2
    elif string == "Plank Straight Arm":
        y = 3
    elif string == "Plank With Elbow":
        y = 4
    elif string == "Boat pose":
        y = 5
    else:
        y = 6

def mute():
    global volume
    if volume == 0:
        ui.mute_2.setStyleSheet("QPushButton {border-image : url(:/MENU/mute.png)}")
        winsound.PlaySound(None, winsound.SND_PURGE)
        volume = 1;
    else:
        ui.mute_2.setStyleSheet("QPushButton {border-image : url(:/MENU/unmute.png)}")
        volume = 0;
        winsound.PlaySound('NhacGym1.WAV', winsound.SND_ASYNC)




def YogaFunction():
    global ui
    global volume,cp
    volume = 0
    ui = Yoga.Ui_MainWindow()
    ui.setupUi(MainWindow)
    # t = threading.Thread(target=main)
    # t.start()
    ui.Start_yoga.clicked.connect(lambda: count_task_yoga(y))
    ui.back_yoga.clicked.connect(LoadmainScreen)
    ui.mute_yoga.clicked.connect(mute)
    ui.comboBox_yoga.currentTextChanged.connect(comboboxFuntionYoga)
    ui.SeeVideo_yoga.clicked.connect(MediaPlayer)


def MealFunction():
    global ui,CaloDinner,CaloLunch,CaloBreakFast
    ui = Calo.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(MealSelectForBreakFast)
    ui.pushButton_2.clicked.connect(MealSelectWindowForLunch)
    ui.pushButton_3.clicked.connect(MealSelectWindowForDinner)
    ui.Back_Calo.clicked.connect(LoadmainScreen)
    # Display Calo to table
    ui.label_14.setText(str(CaloDinner))
    ui.label_10.setText(str(CaloLunch))
    ui.label_6.setText(str(CaloBreakFast))

class MealSelectForBreakFast:
    def __init__(self):
        global window,CaloBreakFast,ui_1, CheckboxMeal, ListMeal
        window = QtWidgets.QMainWindow()
        ui_1 = MealSelectBreakFast.Ui_MainWindow()
        ui_1.setupUi(window)
        window.show()
        #Display Calo For breakfase
        ui_1.label_12.setText(str(TocalCalo))

        # display meal to listview
        ui_1.listWidget_2.clear()
        ui_1.listWidget_2.addItems(ListMeal)

        # Display checkbox
        ui_1.gaxaot.setChecked(CheckboxMeal[0])
        ui_1.gakho.setChecked(CheckboxMeal[1])
        ui_1.mucxao.setChecked(CheckboxMeal[2])
        ui_1.suongnuong.setChecked(CheckboxMeal[3])
        ui_1.suongram.setChecked(CheckboxMeal[4])
        ui_1.thitheoquay.setChecked(CheckboxMeal[5])
        ui_1.thitboxao.setChecked(CheckboxMeal[6])
        ui_1.thitkhotieu.setChecked(CheckboxMeal[7])
        ui_1.camoikho.setChecked(CheckboxMeal[8])
        ui_1.cari.setChecked(CheckboxMeal[9])
        ui_1.bobia.setChecked(CheckboxMeal[10])
        ui_1.cabacmachien.setChecked(CheckboxMeal[11])
        ui_1.cabacmakho.setChecked(CheckboxMeal[12])
        ui_1.cangukho.setChecked(CheckboxMeal[13])
        ui_1.chalua.setChecked(CheckboxMeal[14])
        ui_1.ganheoxao.setChecked(CheckboxMeal[15])
        ui_1.goikhobo.setChecked(CheckboxMeal[16])
        ui_1.goitom.setChecked(CheckboxMeal[17])
        ui_1.khoquaxaotrung.setChecked(CheckboxMeal[18])
        ui_1.lapxuongchien.setChecked(CheckboxMeal[19])
        ui_1.mucxaothapcam.setChecked(CheckboxMeal[20])
        ui_1.boxaomang.setChecked(CheckboxMeal[21])
        ui_1.boxaonam.setChecked(CheckboxMeal[22])
        ui_1.thitkhotrung.setChecked(CheckboxMeal[23])
        ui_1.bunrieu.setChecked(CheckboxMeal[24])
        ui_1.bunbohue.setChecked(CheckboxMeal[25])
        ui_1.bunthitnuong.setChecked(CheckboxMeal[26])
        ui_1.bunxao.setChecked(CheckboxMeal[27])
        ui_1.canhkhoqua.setChecked(CheckboxMeal[28])
        ui_1.chaolong.setChecked(CheckboxMeal[29])
        ui_1.bo.setChecked(CheckboxMeal[31])
        ui_1.chuoi.setChecked(CheckboxMeal[32])
        ui_1.thom.setChecked(CheckboxMeal[33])
        ui_1.xoai.setChecked(CheckboxMeal[34])
        ui_1.saurieng.setChecked(CheckboxMeal[35])
        ui_1.mangcut.setChecked(CheckboxMeal[36])
        ui_1.coc.setChecked(CheckboxMeal[37])
        ui_1.nho.setChecked(CheckboxMeal[38])
        ui_1.duahau.setChecked(CheckboxMeal[39])
        ui_1.buoi.setChecked(CheckboxMeal[40])
        ui_1.khoailang.setChecked(CheckboxMeal[41])
        ui_1.le.setChecked(CheckboxMeal[42])
        ui_1.bapluoc.setChecked(CheckboxMeal[43])
        ui_1.khoaitay.setChecked(CheckboxMeal[44])
        ui_1.dauphong.setChecked(CheckboxMeal[45])
        ui_1.dudu.setChecked(CheckboxMeal[46])
        ui_1.sori.setChecked(CheckboxMeal[47])
        ui_1.cam.setChecked(CheckboxMeal[48])
        ui_1.oi.setChecked(CheckboxMeal[49])
        ui_1.thanhlong.setChecked(CheckboxMeal[50])
        ui_1.chebap.setChecked(CheckboxMeal[51])
        ui_1.chechuoi.setChecked(CheckboxMeal[52])
        ui_1.chedauden.setChecked(CheckboxMeal[53])
        ui_1.chedauxanh.setChecked(CheckboxMeal[54])
        ui_1.chenep.setChecked(CheckboxMeal[55])
        ui_1.chetroinuoc.setChecked(CheckboxMeal[56])
        ui_1.xoibap.setChecked(CheckboxMeal[57])
        ui_1.xoidauden.setChecked(CheckboxMeal[58])
        ui_1.xoidauphong.setChecked(CheckboxMeal[59])
        ui_1.xoigac.setChecked(CheckboxMeal[60])
        ui_1.cafe.setChecked(CheckboxMeal[61])
        ui_1.nuocam.setChecked(CheckboxMeal[62])
        ui_1.nuocchanh.setChecked(CheckboxMeal[63])
        ui_1.nuocmia.setChecked(CheckboxMeal[64])
        ui_1.nuocrauma.setChecked(CheckboxMeal[65])
        ui_1.suachua.setChecked(CheckboxMeal[66])
        ui_1.trungcut.setChecked(CheckboxMeal[67])
        ui_1.trungga.setChecked(CheckboxMeal[68])
        ui_1.trungvit.setChecked(CheckboxMeal[69])

        ui_1.Save.clicked.connect(SaveMealBreakFast)
        # ui_1.Save.setEnabled(False)

        # if checkbox change state will call function
        ui_1.gaxaot.stateChanged.connect(gaxaot)
        ui_1.gakho.stateChanged.connect(gakho)
        ui_1.mucxao.stateChanged.connect(mucxao)
        ui_1.suongnuong.stateChanged.connect(suongnuong)
        ui_1.suongram.stateChanged.connect(suongram)
        ui_1.thitheoquay.stateChanged.connect(thitheoquay)
        ui_1.thitboxao.stateChanged.connect(thitboxao)
        ui_1.thitkhotieu.stateChanged.connect(thitkhotieu)
        ui_1.camoikho.stateChanged.connect(camoikho)
        ui_1.cari.stateChanged.connect(cari)
        ui_1.bobia.stateChanged.connect(bobia)
        ui_1.cabacmachien.stateChanged.connect(cabacmachien)
        ui_1.cabacmakho.stateChanged.connect(cabacmakho)
        ui_1.cangukho.stateChanged.connect(cangukho)
        ui_1.chalua.stateChanged.connect(chalua)
        ui_1.ganheoxao.stateChanged.connect(ganheoxao)
        ui_1.goikhobo.stateChanged.connect(goikhobo)
        ui_1.goitom.stateChanged.connect(goitom)
        ui_1.khoquaxaotrung.stateChanged.connect(khoquaxaotrung)
        ui_1.lapxuongchien.stateChanged.connect(lapxuongchien)
        ui_1.mucxaothapcam.stateChanged.connect(mucxaothapcam)
        ui_1.boxaomang.stateChanged.connect(boxaomang)
        ui_1.boxaonam.stateChanged.connect(boxaonam)
        ui_1.thitkhotrung.stateChanged.connect(thitkhotrung)
        ui_1.bunrieu.stateChanged.connect(bunrieu)
        ui_1.bunbohue.stateChanged.connect(bunbohue)
        ui_1.bunthitnuong.stateChanged.connect(bunthitnuong)
        ui_1.bunxao.stateChanged.connect(bunxao)
        ui_1.canhkhoqua.stateChanged.connect(canhkhoqua)
        ui_1.chaolong.stateChanged.connect(chaolong)
        ui_1.bo.stateChanged.connect(bo)
        ui_1.chuoi.stateChanged.connect(chuoi)
        ui_1.thom.stateChanged.connect(thom)
        ui_1.xoai.stateChanged.connect(xoai)
        ui_1.saurieng.stateChanged.connect(saurieng)
        ui_1.mangcut.stateChanged.connect(mangcut)
        ui_1.coc.stateChanged.connect(coc)
        ui_1.nho.stateChanged.connect(nho)
        ui_1.duahau.stateChanged.connect(duahau)
        ui_1.buoi.stateChanged.connect(buoi)
        ui_1.khoailang.stateChanged.connect(khoailang)
        ui_1.le.stateChanged.connect(le)
        ui_1.bapluoc.stateChanged.connect(bapluoc)
        ui_1.khoaitay.stateChanged.connect(khoaitay)
        ui_1.dauphong.stateChanged.connect(dauphong)
        ui_1.dudu.stateChanged.connect(dudu)
        ui_1.sori.stateChanged.connect(sori)
        ui_1.cam.stateChanged.connect(cam)
        ui_1.oi.stateChanged.connect(oi)
        ui_1.thanhlong.stateChanged.connect(thanhlong)
        ui_1.chebap.stateChanged.connect(chebap)
        ui_1.chechuoi.stateChanged.connect(chechuoi)
        ui_1.chedauden.stateChanged.connect(chedauden)
        ui_1.chedauxanh.stateChanged.connect(chedauxanh)
        ui_1.chenep.stateChanged.connect(chenep)
        ui_1.chetroinuoc.stateChanged.connect(chetroinuoc)
        ui_1.xoibap.stateChanged.connect(xoibap)
        ui_1.xoidauden.stateChanged.connect(xoidauden)
        ui_1.xoidauphong.stateChanged.connect(xoidauphong)
        ui_1.xoigac.stateChanged.connect(xoigac)
        ui_1.cafe.stateChanged.connect(cafe)
        ui_1.nuocam.stateChanged.connect(nuocam)
        ui_1.nuocchanh.stateChanged.connect(nuocchanh)
        ui_1.nuocmia.stateChanged.connect(nuocmia)
        ui_1.nuocrauma.stateChanged.connect(nuocrauma)
        ui_1.suachua.stateChanged.connect(suachua)
        ui_1.trungcut.stateChanged.connect(trungcut)
        ui_1.trungga.stateChanged.connect(trungga)
        ui_1.trungvit.stateChanged.connect(trungvit)

def SaveMealBreakFast():
    global FOOD, ListMeal, CheckboxMeal,CaloBreakFast
    ListMealDB = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal.txt",
        "w")
    CheckboxDB = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox.txt",
        "w")
    CaloBreakFast = str(ui_1.label_4.text())
        # ListMeal
    for d in range(len(ListMeal)):
        ListMealDB.writelines(ListMeal[d] + '\n')
        # Checkbox
    for e in range(len(CheckboxMeal)):
        CheckboxDB.writelines(str(CheckboxMeal[e]) + '\n')


class MealSelectWindowForLunch:
    def __init__(self):
        global window,ui_1, CheckboxMeal, ListMeal,CaloLunch
        window = QtWidgets.QMainWindow()
        ui_1 = MealSelectLunch.Ui_MainWindow()
        ui_1.setupUi(window)
        window.show()
        #Display Calo For Lunch
        ui_1.label_12.setText(str(TocalCalo))

        # display meal to listview
        ui_1.listWidget_4.clear()
        ui_1.listWidget_4.addItems(ListMeal)

        # Display checkbox
        ui_1.gaxaot.setChecked(CheckboxMeal[0])
        ui_1.gakho.setChecked(CheckboxMeal[1])
        ui_1.mucxao.setChecked(CheckboxMeal[2])
        ui_1.suongnuong.setChecked(CheckboxMeal[3])
        ui_1.suongram.setChecked(CheckboxMeal[4])
        ui_1.thitheoquay.setChecked(CheckboxMeal[5])
        ui_1.thitboxao.setChecked(CheckboxMeal[6])
        ui_1.thitkhotieu.setChecked(CheckboxMeal[7])
        ui_1.camoikho.setChecked(CheckboxMeal[8])
        ui_1.cari.setChecked(CheckboxMeal[9])
        ui_1.bobia.setChecked(CheckboxMeal[10])
        ui_1.cabacmachien.setChecked(CheckboxMeal[11])
        ui_1.cabacmakho.setChecked(CheckboxMeal[12])
        ui_1.cangukho.setChecked(CheckboxMeal[13])
        ui_1.chalua.setChecked(CheckboxMeal[14])
        ui_1.ganheoxao.setChecked(CheckboxMeal[15])
        ui_1.goikhobo.setChecked(CheckboxMeal[16])
        ui_1.goitom.setChecked(CheckboxMeal[17])
        ui_1.khoquaxaotrung.setChecked(CheckboxMeal[18])
        ui_1.lapxuongchien.setChecked(CheckboxMeal[19])
        ui_1.mucxaothapcam.setChecked(CheckboxMeal[20])
        ui_1.boxaomang.setChecked(CheckboxMeal[21])
        ui_1.boxaonam.setChecked(CheckboxMeal[22])
        ui_1.thitkhotrung.setChecked(CheckboxMeal[23])
        ui_1.bunrieu.setChecked(CheckboxMeal[24])
        ui_1.bunbohue.setChecked(CheckboxMeal[25])
        ui_1.bunthitnuong.setChecked(CheckboxMeal[26])
        ui_1.bunxao.setChecked(CheckboxMeal[27])
        ui_1.canhkhoqua.setChecked(CheckboxMeal[28])
        ui_1.chaolong.setChecked(CheckboxMeal[29])
        ui_1.bo.setChecked(CheckboxMeal[31])
        ui_1.chuoi.setChecked(CheckboxMeal[32])
        ui_1.thom.setChecked(CheckboxMeal[33])
        ui_1.xoai.setChecked(CheckboxMeal[34])
        ui_1.saurieng.setChecked(CheckboxMeal[35])
        ui_1.mangcut.setChecked(CheckboxMeal[36])
        ui_1.coc.setChecked(CheckboxMeal[37])
        ui_1.nho.setChecked(CheckboxMeal[38])
        ui_1.duahau.setChecked(CheckboxMeal[39])
        ui_1.buoi.setChecked(CheckboxMeal[40])
        ui_1.khoailang.setChecked(CheckboxMeal[41])
        ui_1.le.setChecked(CheckboxMeal[42])
        ui_1.bapluoc.setChecked(CheckboxMeal[43])
        ui_1.khoaitay.setChecked(CheckboxMeal[44])
        ui_1.dauphong.setChecked(CheckboxMeal[45])
        ui_1.dudu.setChecked(CheckboxMeal[46])
        ui_1.sori.setChecked(CheckboxMeal[47])
        ui_1.cam.setChecked(CheckboxMeal[48])
        ui_1.oi.setChecked(CheckboxMeal[49])
        ui_1.thanhlong.setChecked(CheckboxMeal[50])
        ui_1.chebap.setChecked(CheckboxMeal[51])
        ui_1.chechuoi.setChecked(CheckboxMeal[52])
        ui_1.chedauden.setChecked(CheckboxMeal[53])
        ui_1.chedauxanh.setChecked(CheckboxMeal[54])
        ui_1.chenep.setChecked(CheckboxMeal[55])
        ui_1.chetroinuoc.setChecked(CheckboxMeal[56])
        ui_1.xoibap.setChecked(CheckboxMeal[57])
        ui_1.xoidauden.setChecked(CheckboxMeal[58])
        ui_1.xoidauphong.setChecked(CheckboxMeal[59])
        ui_1.xoigac.setChecked(CheckboxMeal[60])
        ui_1.cafe.setChecked(CheckboxMeal[61])
        ui_1.nuocam.setChecked(CheckboxMeal[62])
        ui_1.nuocchanh.setChecked(CheckboxMeal[63])
        ui_1.nuocmia.setChecked(CheckboxMeal[64])
        ui_1.nuocrauma.setChecked(CheckboxMeal[65])
        ui_1.suachua.setChecked(CheckboxMeal[66])
        ui_1.trungcut.setChecked(CheckboxMeal[67])
        ui_1.trungga.setChecked(CheckboxMeal[68])
        ui_1.trungvit.setChecked(CheckboxMeal[69])
        # ui_1.Save.setEnabled(False)

        # if checkbox change state will call function
        ui_1.gaxaot.stateChanged.connect(gaxaot)
        ui_1.gakho.stateChanged.connect(gakho)
        ui_1.mucxao.stateChanged.connect(mucxao)
        ui_1.suongnuong.stateChanged.connect(suongnuong)
        ui_1.suongram.stateChanged.connect(suongram)
        ui_1.thitheoquay.stateChanged.connect(thitheoquay)
        ui_1.thitboxao.stateChanged.connect(thitboxao)
        ui_1.thitkhotieu.stateChanged.connect(thitkhotieu)
        ui_1.camoikho.stateChanged.connect(camoikho)
        ui_1.cari.stateChanged.connect(cari)
        ui_1.bobia.stateChanged.connect(bobia)
        ui_1.cabacmachien.stateChanged.connect(cabacmachien)
        ui_1.cabacmakho.stateChanged.connect(cabacmakho)
        ui_1.cangukho.stateChanged.connect(cangukho)
        ui_1.chalua.stateChanged.connect(chalua)
        ui_1.ganheoxao.stateChanged.connect(ganheoxao)
        ui_1.goikhobo.stateChanged.connect(goikhobo)
        ui_1.goitom.stateChanged.connect(goitom)
        ui_1.khoquaxaotrung.stateChanged.connect(khoquaxaotrung)
        ui_1.lapxuongchien.stateChanged.connect(lapxuongchien)
        ui_1.mucxaothapcam.stateChanged.connect(mucxaothapcam)
        ui_1.boxaomang.stateChanged.connect(boxaomang)
        ui_1.boxaonam.stateChanged.connect(boxaonam)
        ui_1.thitkhotrung.stateChanged.connect(thitkhotrung)
        ui_1.bunrieu.stateChanged.connect(bunrieu)
        ui_1.bunbohue.stateChanged.connect(bunbohue)
        ui_1.bunthitnuong.stateChanged.connect(bunthitnuong)
        ui_1.bunxao.stateChanged.connect(bunxao)
        ui_1.canhkhoqua.stateChanged.connect(canhkhoqua)
        ui_1.chaolong.stateChanged.connect(chaolong)
        ui_1.bo.stateChanged.connect(bo)
        ui_1.chuoi.stateChanged.connect(chuoi)
        ui_1.thom.stateChanged.connect(thom)
        ui_1.xoai.stateChanged.connect(xoai)
        ui_1.saurieng.stateChanged.connect(saurieng)
        ui_1.mangcut.stateChanged.connect(mangcut)
        ui_1.coc.stateChanged.connect(coc)
        ui_1.nho.stateChanged.connect(nho)
        ui_1.duahau.stateChanged.connect(duahau)
        ui_1.buoi.stateChanged.connect(buoi)
        ui_1.khoailang.stateChanged.connect(khoailang)
        ui_1.le.stateChanged.connect(le)
        ui_1.bapluoc.stateChanged.connect(bapluoc)
        ui_1.khoaitay.stateChanged.connect(khoaitay)
        ui_1.dauphong.stateChanged.connect(dauphong)
        ui_1.dudu.stateChanged.connect(dudu)
        ui_1.sori.stateChanged.connect(sori)
        ui_1.cam.stateChanged.connect(cam)
        ui_1.oi.stateChanged.connect(oi)
        ui_1.thanhlong.stateChanged.connect(thanhlong)
        ui_1.chebap.stateChanged.connect(chebap)
        ui_1.chechuoi.stateChanged.connect(chechuoi)
        ui_1.chedauden.stateChanged.connect(chedauden)
        ui_1.chedauxanh.stateChanged.connect(chedauxanh)
        ui_1.chenep.stateChanged.connect(chenep)
        ui_1.chetroinuoc.stateChanged.connect(chetroinuoc)
        ui_1.xoibap.stateChanged.connect(xoibap)
        ui_1.xoidauden.stateChanged.connect(xoidauden)
        ui_1.xoidauphong.stateChanged.connect(xoidauphong)
        ui_1.xoigac.stateChanged.connect(xoigac)
        ui_1.cafe.stateChanged.connect(cafe)
        ui_1.nuocam.stateChanged.connect(nuocam)
        ui_1.nuocchanh.stateChanged.connect(nuocchanh)
        ui_1.nuocmia.stateChanged.connect(nuocmia)
        ui_1.nuocrauma.stateChanged.connect(nuocrauma)
        ui_1.suachua.stateChanged.connect(suachua)
        ui_1.trungcut.stateChanged.connect(trungcut)
        ui_1.trungga.stateChanged.connect(trungga)
        ui_1.trungvit.stateChanged.connect(trungvit)
        ui_1.Save.clicked.connect(SaveMealLunch)

def SaveMealLunch():
        global FOOD, FRUIT, OTHER, ListMeal, CheckboxMeal,CaloLunch
        ListMealDB = open(
            r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal_Lunch.txt",
            "w")
        CheckboxDB = open(
            r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox_Lunch.txt",
            "w")
        CaloLunch = ui_1.label_4.text()
        #ListView
        for d in range(len(ListMealLunch)):
            ListMealDB.writelines(ListMealLunch[d] + '\n')
        # Checkbox
        for e in range(len(CheckboxMeal)):
            CheckboxDB.writelines(str(CheckboxMealLunch[e]) + '\n')


class MealSelectWindowForDinner():
    def __init__(self):
        global window,ui_1, CheckboxMeal, ListMeal,CaloDinner
        window = QtWidgets.QMainWindow()
        ui_1 = MealSelectDinner.Ui_MainWindow()
        ui_1.setupUi(window)
        window.show()
        #Display Calo For breakfase
        ui_1.label_12.setText(str(TocalCalo))

        # display meal to listview
        ui_1.listWidget_4.clear()
        ui_1.listWidget_4.addItems(ListMeal)

        # Display checkbox
        ui_1.gaxaot.setChecked(CheckboxMeal[0])
        ui_1.gakho.setChecked(CheckboxMeal[1])
        ui_1.mucxao.setChecked(CheckboxMeal[2])
        ui_1.suongnuong.setChecked(CheckboxMeal[3])
        ui_1.suongram.setChecked(CheckboxMeal[4])
        ui_1.thitheoquay.setChecked(CheckboxMeal[5])
        ui_1.thitboxao.setChecked(CheckboxMeal[6])
        ui_1.thitkhotieu.setChecked(CheckboxMeal[7])
        ui_1.camoikho.setChecked(CheckboxMeal[8])
        ui_1.cari.setChecked(CheckboxMeal[9])
        ui_1.bobia.setChecked(CheckboxMeal[10])
        ui_1.cabacmachien.setChecked(CheckboxMeal[11])
        ui_1.cabacmakho.setChecked(CheckboxMeal[12])
        ui_1.cangukho.setChecked(CheckboxMeal[13])
        ui_1.chalua.setChecked(CheckboxMeal[14])
        ui_1.ganheoxao.setChecked(CheckboxMeal[15])
        ui_1.goikhobo.setChecked(CheckboxMeal[16])
        ui_1.goitom.setChecked(CheckboxMeal[17])
        ui_1.khoquaxaotrung.setChecked(CheckboxMeal[18])
        ui_1.lapxuongchien.setChecked(CheckboxMeal[19])
        ui_1.mucxaothapcam.setChecked(CheckboxMeal[20])
        ui_1.boxaomang.setChecked(CheckboxMeal[21])
        ui_1.boxaonam.setChecked(CheckboxMeal[22])
        ui_1.thitkhotrung.setChecked(CheckboxMeal[23])
        ui_1.bunrieu.setChecked(CheckboxMeal[24])
        ui_1.bunbohue.setChecked(CheckboxMeal[25])
        ui_1.bunthitnuong.setChecked(CheckboxMeal[26])
        ui_1.bunxao.setChecked(CheckboxMeal[27])
        ui_1.canhkhoqua.setChecked(CheckboxMeal[28])
        ui_1.chaolong.setChecked(CheckboxMeal[29])
        ui_1.bo.setChecked(CheckboxMeal[31])
        ui_1.chuoi.setChecked(CheckboxMeal[32])
        ui_1.thom.setChecked(CheckboxMeal[33])
        ui_1.xoai.setChecked(CheckboxMeal[34])
        ui_1.saurieng.setChecked(CheckboxMeal[35])
        ui_1.mangcut.setChecked(CheckboxMeal[36])
        ui_1.coc.setChecked(CheckboxMeal[37])
        ui_1.nho.setChecked(CheckboxMeal[38])
        ui_1.duahau.setChecked(CheckboxMeal[39])
        ui_1.buoi.setChecked(CheckboxMeal[40])
        ui_1.khoailang.setChecked(CheckboxMeal[41])
        ui_1.le.setChecked(CheckboxMeal[42])
        ui_1.bapluoc.setChecked(CheckboxMeal[43])
        ui_1.khoaitay.setChecked(CheckboxMeal[44])
        ui_1.dauphong.setChecked(CheckboxMeal[45])
        ui_1.dudu.setChecked(CheckboxMeal[46])
        ui_1.sori.setChecked(CheckboxMeal[47])
        ui_1.cam.setChecked(CheckboxMeal[48])
        ui_1.oi.setChecked(CheckboxMeal[49])
        ui_1.thanhlong.setChecked(CheckboxMeal[50])
        ui_1.chebap.setChecked(CheckboxMeal[51])
        ui_1.chechuoi.setChecked(CheckboxMeal[52])
        ui_1.chedauden.setChecked(CheckboxMeal[53])
        ui_1.chedauxanh.setChecked(CheckboxMeal[54])
        ui_1.chenep.setChecked(CheckboxMeal[55])
        ui_1.chetroinuoc.setChecked(CheckboxMeal[56])
        ui_1.xoibap.setChecked(CheckboxMeal[57])
        ui_1.xoidauden.setChecked(CheckboxMeal[58])
        ui_1.xoidauphong.setChecked(CheckboxMeal[59])
        ui_1.xoigac.setChecked(CheckboxMeal[60])
        ui_1.cafe.setChecked(CheckboxMeal[61])
        ui_1.nuocam.setChecked(CheckboxMeal[62])
        ui_1.nuocchanh.setChecked(CheckboxMeal[63])
        ui_1.nuocmia.setChecked(CheckboxMeal[64])
        ui_1.nuocrauma.setChecked(CheckboxMeal[65])
        ui_1.suachua.setChecked(CheckboxMeal[66])
        ui_1.trungcut.setChecked(CheckboxMeal[67])
        ui_1.trungga.setChecked(CheckboxMeal[68])
        ui_1.trungvit.setChecked(CheckboxMeal[69])

        ui_1.Save.clicked.connect(SaveMealDinner)
        # ui_1.Save.setEnabled(False)

        # if checkbox change state will call function
        ui_1.gaxaot.stateChanged.connect(gaxaot)
        ui_1.gakho.stateChanged.connect(gakho)
        ui_1.mucxao.stateChanged.connect(mucxao)
        ui_1.suongnuong.stateChanged.connect(suongnuong)
        ui_1.suongram.stateChanged.connect(suongram)
        ui_1.thitheoquay.stateChanged.connect(thitheoquay)
        ui_1.thitboxao.stateChanged.connect(thitboxao)
        ui_1.thitkhotieu.stateChanged.connect(thitkhotieu)
        ui_1.camoikho.stateChanged.connect(camoikho)
        ui_1.cari.stateChanged.connect(cari)
        ui_1.bobia.stateChanged.connect(bobia)
        ui_1.cabacmachien.stateChanged.connect(cabacmachien)
        ui_1.cabacmakho.stateChanged.connect(cabacmakho)
        ui_1.cangukho.stateChanged.connect(cangukho)
        ui_1.chalua.stateChanged.connect(chalua)
        ui_1.ganheoxao.stateChanged.connect(ganheoxao)
        ui_1.goikhobo.stateChanged.connect(goikhobo)
        ui_1.goitom.stateChanged.connect(goitom)
        ui_1.khoquaxaotrung.stateChanged.connect(khoquaxaotrung)
        ui_1.lapxuongchien.stateChanged.connect(lapxuongchien)
        ui_1.mucxaothapcam.stateChanged.connect(mucxaothapcam)
        ui_1.boxaomang.stateChanged.connect(boxaomang)
        ui_1.boxaonam.stateChanged.connect(boxaonam)
        ui_1.thitkhotrung.stateChanged.connect(thitkhotrung)
        ui_1.bunrieu.stateChanged.connect(bunrieu)
        ui_1.bunbohue.stateChanged.connect(bunbohue)
        ui_1.bunthitnuong.stateChanged.connect(bunthitnuong)
        ui_1.bunxao.stateChanged.connect(bunxao)
        ui_1.canhkhoqua.stateChanged.connect(canhkhoqua)
        ui_1.chaolong.stateChanged.connect(chaolong)
        ui_1.bo.stateChanged.connect(bo)
        ui_1.chuoi.stateChanged.connect(chuoi)
        ui_1.thom.stateChanged.connect(thom)
        ui_1.xoai.stateChanged.connect(xoai)
        ui_1.saurieng.stateChanged.connect(saurieng)
        ui_1.mangcut.stateChanged.connect(mangcut)
        ui_1.coc.stateChanged.connect(coc)
        ui_1.nho.stateChanged.connect(nho)
        ui_1.duahau.stateChanged.connect(duahau)
        ui_1.buoi.stateChanged.connect(buoi)
        ui_1.khoailang.stateChanged.connect(khoailang)
        ui_1.le.stateChanged.connect(le)
        ui_1.bapluoc.stateChanged.connect(bapluoc)
        ui_1.khoaitay.stateChanged.connect(khoaitay)
        ui_1.dauphong.stateChanged.connect(dauphong)
        ui_1.dudu.stateChanged.connect(dudu)
        ui_1.sori.stateChanged.connect(sori)
        ui_1.cam.stateChanged.connect(cam)
        ui_1.oi.stateChanged.connect(oi)
        ui_1.thanhlong.stateChanged.connect(thanhlong)
        ui_1.chebap.stateChanged.connect(chebap)
        ui_1.chechuoi.stateChanged.connect(chechuoi)
        ui_1.chedauden.stateChanged.connect(chedauden)
        ui_1.chedauxanh.stateChanged.connect(chedauxanh)
        ui_1.chenep.stateChanged.connect(chenep)
        ui_1.chetroinuoc.stateChanged.connect(chetroinuoc)
        ui_1.xoibap.stateChanged.connect(xoibap)
        ui_1.xoidauden.stateChanged.connect(xoidauden)
        ui_1.xoidauphong.stateChanged.connect(xoidauphong)
        ui_1.xoigac.stateChanged.connect(xoigac)
        ui_1.cafe.stateChanged.connect(cafe)
        ui_1.nuocam.stateChanged.connect(nuocam)
        ui_1.nuocchanh.stateChanged.connect(nuocchanh)
        ui_1.nuocmia.stateChanged.connect(nuocmia)
        ui_1.nuocrauma.stateChanged.connect(nuocrauma)
        ui_1.suachua.stateChanged.connect(suachua)
        ui_1.trungcut.stateChanged.connect(trungcut)
        ui_1.trungga.stateChanged.connect(trungga)
        ui_1.trungvit.stateChanged.connect(trungvit)

def SaveMealDinner():
    global ListMeal, CheckboxMeal,CaloDinner
    ListMealDB = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal_Dinner.txt",
        "w")
    CheckboxDB = open(
        r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox_Dinner.txt",
        "w")
    CaloDinner = str(ui_1.label_4.text())
    for d in range(len(ListMealDinner)):
        ListMealDB.writelines(ListMealDinner[d] + '\n')
        #     # Checkbix
    for e in range(len(CheckboxMeal)):
        CheckboxDB.writelines(str(CheckboxMealDinner[e]) + '\n')

def gaxaot():
    global TocalCalo,FOOD,Index,CheckboxMeal,ListMeal,OTHER,FRUIT
    if ui_1.gaxaot.isChecked() == True:
        TocalCalo += 270
        # FOOD.append('gaxaot')
        ListMeal.append('gaxaot')
        CheckboxMeal[0] = True
    else:
        ui_1.gaxaot.isChecked() == False
        TocalCalo -= 270
        # FOOD.remove('gaxaot')
        ListMeal.remove('gaxaot')
        CheckboxMeal[0] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)

def gakho():
    global TocalCalo,FOOD,Index
    if ui_1.gakho.isChecked() == True:
        TocalCalo += 300
        # FOOD.append('gakho')
        ListMeal.append('gakho')
        CheckboxMeal[1] = True
    else:
        ui_1.gakho.isChecked() == False
        TocalCalo -= 300
        # FOOD.remove('gakho')
        ListMeal.remove('gakho')
        CheckboxMeal[1] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def mucxao():
    global TocalCalo,FOOD
    if ui_1.mucxao.isChecked() == True:
        TocalCalo += 180
        # FOOD.append('mucxao')
        ListMeal.append('mucxao')
        CheckboxMeal[2] = True
    else:
        ui_1.mucxao.isChecked() == False
        TocalCalo -= 180
        # FOOD.remove('mucxao')
        ListMeal.remove('mucxao')
        CheckboxMeal[2] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def suongnuong():
    global TocalCalo,FOOD
    if ui_1.suongnuong.isChecked() == True:
        TocalCalo += 110
        # FOOD.append('suongnuong')
        ListMeal.append('suongnuong')
        CheckboxMeal[3] = True
    else:
        ui_1.suongnuong.isChecked() == False
        TocalCalo -= 110
        FOOD.remove('suongnuong')
        # ListMeal.remove('suongnuong')
        CheckboxMeal[3] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def suongram():
    global TocalCalo,FOOD
    if ui_1.suongram.isChecked() == True:
        TocalCalo += 150
        # FOOD.append('suongram')
        ListMeal.append('suongram')
        CheckboxMeal[4] = True
    else:
        ui_1.suongram.isChecked() == False
        TocalCalo -= 150
        # FOOD.remove('suongram')
        ListMeal.remove('suongram')
        CheckboxMeal[4] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def thitheoquay():
    global TocalCalo,FOOD
    if ui_1.thitheoquay.isChecked() == True:
        TocalCalo += 145
        # FOOD.append('thitheoquay')
        ListMeal.append('thitheoquay')
        CheckboxMeal[5] = True
    else:
        ui_1.thitheoquay.isChecked() == False
        TocalCalo -= 145
        # FOOD.remove('thitheoquay')
        ListMeal.remove('thitheoquay')
        CheckboxMeal[5] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def thitboxao():
    global TocalCalo,FOOD
    if ui_1.thitboxao.isChecked() == True:
        TocalCalo += 200
        # FOOD.append('thitboxao')
        ListMeal.append('thitboxao')
        CheckboxMeal[6] = True
    else:
        ui_1.thitboxao.isChecked() == False
        TocalCalo -= 200
        # FOOD.remove('thitboxao')
        ListMeal.remove('thitboxao')
        CheckboxMeal[6] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def thitkhotieu():
    global TocalCalo,FOOD
    if ui_1.thitkhotieu.isChecked() == True:
        TocalCalo += 200
        # FOOD.append('thitkhotieu')
        ListMeal.append('thitkhotieu')
        CheckboxMeal[7] = True
    else:
        ui_1.thitkhotieu.isChecked() == False
        TocalCalo -= 200
        # FOOD.remove('thitkhotieu')
        ListMeal.remove('thitkhotieu')
        CheckboxMeal[7] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def camoikho():
    global TocalCalo,FOOD
    if ui_1.camoikho.isChecked() == True:
        TocalCalo += 105
        # FOOD.append('camoikho')
        ListMeal.append('camoikho')
        CheckboxMeal[8] = True
    else:
        ui_1.camoikho.isChecked() == False
        TocalCalo -= 105
        # FOOD.remove('camoikho')
        ListMeal.remove('camoikho')
        CheckboxMeal[8] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def cari():
    global TocalCalo,FOOD
    if ui_1.cari.isChecked() == True:
        TocalCalo += 278
        # FOOD.append('cari')
        ListMeal.append('cari')
        CheckboxMeal[9] = True
    else:
        ui_1.cari.isChecked() == False
        TocalCalo -= 278
        # FOOD.remove('cari')
        ListMeal.remove('cari')
        CheckboxMeal[9] = True
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def bobia():
    global TocalCalo,FOOD
    if ui_1.bobia.isChecked() == True:
        TocalCalo += 100
        # FOOD.append('bobia')
        ListMeal.append('bobia')
        CheckboxMeal[10] = True
    else:
        ui_1.bobia.isChecked() == False
        TocalCalo -= 100
        # FOOD.remove('bobia')
        ListMeal.remove('bobia')
        CheckboxMeal[10] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def cabacmachien():
    global TocalCalo,FOOD
    if ui_1.cabacmachien.isChecked() == True:
        TocalCalo += 135
        # FOOD.append('cabacmachien')
        ListMeal.append('cabacmachien')
        CheckboxMeal[11] = True
    else:
        ui_1.cabacmachien.isChecked() == False
        TocalCalo -= 135
        # FOOD.remove('cabacmachien')
        ListMeal.remove('cabacmachien')
        CheckboxMeal[11] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def cabacmakho():
    global TocalCalo,FOOD
    if ui_1.cabacmakho.isChecked() == True:
        TocalCalo += 167
        # FOOD.append('cabacmakho')
        ListMeal.append('cabacmakho')
        CheckboxMeal[12] = True
    else:
        ui_1.cabacmakho.isChecked() == False
        TocalCalo -= 167
        # FOOD.remove('cabacmakho')
        ListMeal.remove('cabacmakho')
        CheckboxMeal[12] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def cangukho():
    global TocalCalo,FOOD
    if ui_1.cangukho.isChecked() == True:
        TocalCalo += 122
        # FOOD.append('cangukho')
        ListMeal.append('cangukho')
        CheckboxMeal[13] = True
    else:
        ui_1.cangukho.isChecked() == False
        TocalCalo -= 122
        # FOOD.remove('cangukho')
        ListMeal.remove('cangukho')
        CheckboxMeal[13] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def chalua():
    global TocalCalo,FOOD
    if ui_1.chalua.isChecked() == True:
        TocalCalo += 100
        # FOOD.append('chalua')
        ListMeal.append('chalua')
        CheckboxMeal[14] = True
    else:
        ui_1.chalua.isChecked() == False
        TocalCalo -= 100
        # FOOD.remove('chalua')
        ListMeal.remove('chalua')
        CheckboxMeal[14] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def ganheoxao():
    global TocalCalo,FOOD
    if ui_1.ganheoxao.isChecked() == True:
        TocalCalo += 200
        # FOOD.append('ganheoxao')
        ListMeal.append('ganheoxao')
        CheckboxMeal[15] = True
    else:
        ui_1.ganheoxao.isChecked() == False
        TocalCalo -= 200
        # FOOD.remove('ganheoxao')
        ListMeal.remove('ganheoxao')
        CheckboxMeal[15] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def goikhobo():
    global TocalCalo,FOOD
    if ui_1.goikhobo.isChecked() == True:
        TocalCalo += 268
        # FOOD.append('goikhobo')
        ListMeal.append('goikhobo')
        CheckboxMeal[16] = True
    else:
        ui_1.goikhobo.isChecked() == False
        TocalCalo -= 268
        # FOOD.remove('goikhobo')
        ListMeal.remove('goikhobo')
        CheckboxMeal[16] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def goitom():
    global TocalCalo,FOOD
    if ui_1.goitom.isChecked() == True:
        TocalCalo += 147
        # FOOD.append('goitom')
        ListMeal.append('goitom')
        CheckboxMeal[17] = True
    else:
        ui_1.goitom.isChecked() == False
        TocalCalo -= 147
        # FOOD.remove('goitom')
        ListMeal.remove('goitom')
        CheckboxMeal[17] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def khoquaxaotrung():
    global TocalCalo,FOOD
    if ui_1.khoquaxaotrung.isChecked() == True:
        TocalCalo += 115
        # FOOD.append('khoquaxaotrung')
        ListMeal.append('khoquaxaotrung')
        CheckboxMeal[18] = True
    else:
        ui_1.khoquaxaotrung.isChecked() == False
        TocalCalo -= 115
        # FOOD.remove('khoquaxaotrung')
        ListMeal.remove('khoquaxaotrung')
        CheckboxMeal[18] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def lapxuongchien():
    global TocalCalo,FOOD
    if ui_1.lapxuongchien.isChecked() == True:
        TocalCalo += 300
        # FOOD.append('lapxuongchien')
        ListMeal.append('lapxuongchien')
        CheckboxMeal[19] = True
    else:
        ui_1.lapxuongchien.isChecked() == False
        TocalCalo -= 300
        # FOOD.remove('lapxuongchien')
        ListMeal.remove('lapxuongchien')
        CheckboxMeal[19] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def mucxaothapcam():
    global TocalCalo,FOOD
    if ui_1.mucxaothapcam.isChecked() == True:
        TocalCalo += 135
        # FOOD.append('mucxaothapcam')
        ListMeal.append('mucxaothapcam')
        CheckboxMeal[20] = True
    else:
        ui_1.mucxaothapcam.isChecked() == False
        TocalCalo -= 135
        # FOOD.remove('mucxaothapcam')
        ListMeal.remove('mucxaothapcam')
        CheckboxMeal[20] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def boxaomang():
    global TocalCalo,FOOD
    if ui_1.boxaomang.isChecked() == True:
        TocalCalo += 105
        # FOOD.append('boxaomang')
        ListMeal.append('boxaomang')
        CheckboxMeal[21] = True
    else:
        ui_1.boxaomang.isChecked() == False
        TocalCalo -= 105
        # FOOD.remove('boxaomang')
        ListMeal.remove('boxaomang')
        CheckboxMeal[21] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def boxaonam():
    global TocalCalo,FOOD
    if ui_1.boxaonam.isChecked() == True:
        TocalCalo += 150
        # FOOD.append('boxaonam')
        ListMeal.append('boxaonam')
        CheckboxMeal[22] = True
    else:
        ui_1.gaxboxaonamaot.isChecked() == False
        TocalCalo -= 150
        # FOOD.remove('boxaonam')
        ListMeal.remove('boxaonam')
        CheckboxMeal[22] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def thitkhotrung():
    global TocalCalo,FOOD
    if ui_1.thitkhotrung.isChecked() == True:
        TocalCalo += 315
        # FOOD.append('thitkhotrung')
        ListMeal.append('thitkhotrung')
        CheckboxMeal[23] = True
    else:
        ui_1.thitkhotrung.isChecked() == False
        TocalCalo -= 315
        # FOOD.remove('thitkhotrung')
        ListMeal.remove('thitkhotrung')
        CheckboxMeal[23] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def bunrieu():
    global TocalCalo,FOOD
    if ui_1.bunrieu.isChecked() == True:
        TocalCalo += 482
        # FOOD.append('bunrieu')
        ListMeal.append('bunrieu')
        CheckboxMeal[24] = True
    else:
        ui_1.bunrieu.isChecked() == False
        TocalCalo -= 482
        # FOOD.remove('bunrieu')
        ListMeal.remove('bunrieu')
        CheckboxMeal[24] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def bunbohue():
    global TocalCalo,FOOD
    if ui_1.bunbohue.isChecked() == True:
        TocalCalo += 479
        # FOOD.append('bunbohue')
        ListMeal.append('bunbohue')
        CheckboxMeal[25] = True
    else:
        ui_1.bunbohue.isChecked() == False
        TocalCalo -= 479
        # FOOD.remove('bunbohue')
        ListMeal.remove('bunbohue')
        CheckboxMeal[25] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def bunthitnuong():
    global TocalCalo,FOOD
    if ui_1.bunthitnuong.isChecked() == True:
        TocalCalo += 451
        # FOOD.append('bunthitnuong')
        ListMeal.append('bunthitnuong')
        CheckboxMeal[26] = True
    else:
        ui_1.bunthitnuong.isChecked() == False
        TocalCalo -= 451
        # FOOD.remove('bunthitnuong')
        ListMeal.remove('bunthitnuong')
        CheckboxMeal[26] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def bunxao():
    global TocalCalo
    if ui_1.bunxao.isChecked() == True:
        TocalCalo += 570
        # FOOD.append('bunxao')
        ListMeal.append('bunxao')
        CheckboxMeal[27] = True
    else:
        ui_1.bunxao.isChecked() == False
        TocalCalo -= 570
        # FOOD.remove('bunxao')
        ListMeal.remove('bunxao')
        CheckboxMeal[27] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def canhkhoqua():
    global TocalCalo,FOOD
    if ui_1.canhkhoqua.isChecked() == True:
        TocalCalo += 88
        # FOOD.append('canhkhoqua')
        ListMeal.append('canhkhoqua')
        CheckboxMeal[28] = True
    else:
        ui_1.canhkhoqua.isChecked() == False
        TocalCalo -= 479
        # FOOD.remove('canhkhoqua')
        ListMeal.remove('canhkhoqua')
        CheckboxMeal[28] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def chaolong():
    global TocalCalo,FOOD
    if ui_1.chaolong.isChecked() == True:
        TocalCalo += 412
        # FOOD.append('chaolong')
        ListMeal.append('chaolong')
        CheckboxMeal[29] = True
    else:
        ui_1.chaolong.isChecked() == False
        TocalCalo -= 412
        # FOOD.remove('chaolong')
        ListMeal.remove('chaolong')
        CheckboxMeal[29] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)

    ############################### Fruist######################
def bo():
    global TocalCalo,FRUIT
    if ui_1.bo.isChecked() == True:
        TocalCalo += 184
        # FRUIT.append('bo')
        ListMeal.append('bo')
        CheckboxMeal[31] = True
    else:
        ui_1.bo.isChecked() == False
        TocalCalo -= 184
        # FRUIT.remove('bo')
        ListMeal.remove('bo')
        CheckboxMeal[31] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def chuoi():
    global TocalCalo,FRUIT
    if ui_1.chuoi.isChecked() == True:
        TocalCalo += 35
        # FRUIT.append('chuoi')
        ListMeal.append('chuoi')
        CheckboxMeal[32] = True
    else:
        ui_1.chuoi.isChecked() == False
        TocalCalo -= 35
        # FRUIT.append('chuoi')
        ListMeal.append('chuoi')
        CheckboxMeal[32] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def thom():
    global TocalCalo,FRUIT
    if ui_1.thom.isChecked() == True:
        TocalCalo += 17
        # FRUIT.append('thom')
        ListMeal.append('thom')
        CheckboxMeal[33] = True
    else:
        ui_1.thom.isChecked() == False
        TocalCalo -= 17
        # FRUIT.remove('thom')
        ListMeal.remove('thom')
        CheckboxMeal[33] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def xoai():
    global TocalCalo,FRUIT
    if ui_1.xoai.isChecked() == True:
        TocalCalo += 179
        # FRUIT.append('xoai')
        ListMeal.append('xoai')
        CheckboxMeal[34] = True
    else:
        ui_1.xoai.isChecked() == False
        TocalCalo -= 179
        # FRUIT.remove('xoai')
        ListMeal.remove('xoai')
        CheckboxMeal[34] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def saurieng():
    global TocalCalo,FRUIT
    if ui_1.saurieng.isChecked() == True:
        TocalCalo += 28
        # FRUIT.append('saurieng')
        ListMeal.append('saurieng')
        CheckboxMeal[35] = True
    else:
        ui_1.saurieng.isChecked() == False
        TocalCalo -= 28
        # FRUIT.remove('saurieng')
        ListMeal.remove('saurieng')
        CheckboxMeal[35] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def mangcut():
    global TocalCalo,FRUIT
    if ui_1.mangcut.isChecked() == True:
        TocalCalo += 13
        # FRUIT.append('mangcut')
        ListMeal.append('mangcut')
        CheckboxMeal[36] = True
    else:
        ui_1.mangcut.isChecked() == False
        TocalCalo -= 13
        # FRUIT.remove('mangcut')
        ListMeal.remove('mangcut')
        CheckboxMeal[36] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def coc():
    global TocalCalo,FRUIT
    if ui_1.coc.isChecked() == True:
        TocalCalo += 34
        # FRUIT.append('coc')
        ListMeal.append('coc')
        CheckboxMeal[37] = True
    else:
        ui_1.coc.isChecked() == False
        TocalCalo -= 34
        # FRUIT.remove('coc')
        ListMeal.remove('coc')
        CheckboxMeal[37] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def nho():
    global TocalCalo,FRUIT
    if ui_1.nho.isChecked() == True:
        TocalCalo += 68
        # FRUIT.append('nho')
        ListMeal.append('nho')
        CheckboxMeal[38] = True
    else:
        ui_1.nho.isChecked() == False
        TocalCalo -= 68
        # FRUIT.remove('nho')
        ListMeal.remove('nho')
        CheckboxMeal[38] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def duahau():
    global TocalCalo,FRUIT
    if ui_1.duahau.isChecked() == True:
        TocalCalo += 21
        # FRUIT.append('duahau')
        ListMeal.append('duahau')
        CheckboxMeal[39] = True
    else:
        ui_1.duahau.isChecked() == False
        TocalCalo -= 21
        # FRUIT.remove('duahau')
        ListMeal.remove('duahau')
        CheckboxMeal[39] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def buoi():
    global TocalCalo,FRUIT
    if ui_1.buoi.isChecked() == True:
        TocalCalo += 8
        # FRUIT.append('buoi')
        ListMeal.append('buoi')
        CheckboxMeal[40] = True
    else:
        ui_1.buoi.isChecked() == False
        TocalCalo -= 8
        # FRUIT.remove('buoi')
        ListMeal.remove('buoi')
        CheckboxMeal[40] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def khoailang():
    global TocalCalo,FRUIT
    if ui_1.khoailang.isChecked() == True:
        TocalCalo += 131
        # FRUIT.append('khoailang')
        ListMeal.append('khoailang')
        CheckboxMeal[41] = True
    else:
        ui_1.khoailang.isChecked() == False
        TocalCalo -= 131
        # FRUIT.remove('khoailang')
        ListMeal.remove('khoailang')
        CheckboxMeal[41] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def le():
    global TocalCalo,FRUIT
    if ui_1.le.isChecked() == True:
        TocalCalo += 91
        # FRUIT.append('le')
        ListMeal.append('le')
        CheckboxMeal[42] = True
    else:
        ui_1.le.isChecked() == False
        TocalCalo -= 91
        # FRUIT.remove('le')
        ListMeal.remove('le')
        CheckboxMeal[42] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def bapluoc():
    global TocalCalo,FRUIT
    if ui_1.bapluoc.isChecked() == True:
        TocalCalo += 192
        # FRUIT.append('bapluoc')
        ListMeal.append('bapluoc')
        CheckboxMeal[43] = True
    else:
        ui_1.bapluoc.isChecked() == False
        TocalCalo -= 192
        # FRUIT.remove('bapluoc')
        ListMeal.remove('bapluoc')
        CheckboxMeal[43] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def khoaitay():
    global TocalCalo,FRUIT
    if ui_1.khoaitay.isChecked() == True:
        TocalCalo += 131
        # FRUIT.append('khoaitay')
        ListMeal.append('khoaitay')
        CheckboxMeal[44] = True
    else:
        ui_1.khoaitay.isChecked() == False
        TocalCalo -= 131
        # FRUIT.remove('khoaitay')
        ListMeal.remove('khoaitay')
        CheckboxMeal[44] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def dauphong():
    global TocalCalo,FRUIT
    if ui_1.dauphong.isChecked() == True:
        TocalCalo += 395
        # FRUIT.append('dauphong')
        ListMeal.append('dauphong')
        CheckboxMeal[45] = True
    else:
        ui_1.dauphong.isChecked() == False
        TocalCalo -= 395
        # FRUIT.remove('dauphong')
        ListMeal.remove('dauphong')
        CheckboxMeal[45] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def dudu():
    global TocalCalo,FRUIT
    if ui_1.dudu.isChecked() == True:
        TocalCalo += 125
        # FRUIT.append('dudu')
        ListMeal.append('dudu')
        CheckboxMeal[46] = True
    else:
        ui_1.dudu.isChecked() == False
        TocalCalo -= 125
        # FRUIT.remove('dudu')
        ListMeal.remove('dudu')
        CheckboxMeal[46] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def sori():
    global TocalCalo,FRUIT
    if ui_1.sori.isChecked() == True:
        TocalCalo += 14
        # FRUIT.append('sori')
        ListMeal.append('sori')
        CheckboxMeal[47] = True
    else:
        ui_1.sori.isChecked() == False
        TocalCalo -= 14
        # FRUIT.remove('sori')
        ListMeal.remove('sori')
        CheckboxMeal[47] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def cam():
    global TocalCalo,FRUIT
    if ui_1.cam.isChecked() == True:
        TocalCalo += 68
        # FRUIT.append('cam')
        ListMeal.append('cam')
        CheckboxMeal[48] = True
    else:
        ui_1.cam.isChecked() == False
        TocalCalo -= 68
        # FRUIT.remove('cam')
        ListMeal.remove('cam')
        CheckboxMeal[48] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def oi():
    global TocalCalo,FRUIT
    if ui_1.oi.isChecked() == True:
        TocalCalo += 53
        # FRUIT.append('oi')
        ListMeal.append('oi')
        CheckboxMeal[49] = True
    else:
        ui_1.oi.isChecked() == False
        TocalCalo -= 53
        # FRUIT.remove('oi')
        ListMeal.remove('oi')
        CheckboxMeal[49] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def thanhlong():
    global TocalCalo,FRUIT
    if ui_1.thanhlong.isChecked() == True:
        TocalCalo += 225
        # FRUIT.append('thanhlong')
        ListMeal.append('thanhlong')
        CheckboxMeal[50] = True
    else:
        ui_1.thanhlong.isChecked() == False
        TocalCalo -= 225
        # FRUIT.remove('thanhlong')
        ListMeal.remove('thanhlong')
        CheckboxMeal[50] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
###########################Orther################
def chebap():
    global TocalCalo,OTHER
    if ui_1.chebap.isChecked() == True:
        TocalCalo += 325
        ListMeal.append('chebap')
        # OTHER.append('chebap')
        CheckboxMeal[51] = True
    else:
        ui_1.chebap.isChecked() == False
        TocalCalo -= 325
        ListMeal.remove('chebap')
        # OTHER.remove('chebap')
        CheckboxMeal[51] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def chechuoi():
    global TocalCalo,OTHER
    if ui_1.chechuoi.isChecked() == True:
        TocalCalo += 332
        ListMeal.append('chechuoi')
        # OTHER.append('chechuoi')
        CheckboxMeal[52] = True
    else:
        ui_1.chechuoi.isChecked() == False
        TocalCalo -= 332
        ListMeal.remove('chechuoi')
        # OTHER.remove('chechuoi')
        CheckboxMeal[52] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def chedauden():
    global TocalCalo,OTHER
    if ui_1.chedauden.isChecked() == True:
        TocalCalo += 419
        ListMeal.append('chedauden')
        # OTHER.append('chedauden')
        CheckboxMeal[53] = True
    else:
        ui_1.chedauden.isChecked() == False
        TocalCalo -= 419
        ListMeal.remove('chedauden')
        # OTHER.remove('chedauden')
        CheckboxMeal[53] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def chedauxanh():
    global TocalCalo,OTHER
    if ui_1.chedauxanh.isChecked() == True:
        TocalCalo += 359
        ListMeal.append('chedauxanh')
        # OTHER.append('chedauxanh')
        CheckboxMeal[54] = True
    else:
        ui_1.chedauxanh.isChecked() == False
        TocalCalo -= 359
        ListMeal.remove('chedauxanh')
        # OTHER.remove('chedauxanh')
        CheckboxMeal[54] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def chenep():
    global TocalCalo,OTHER
    if ui_1.chenep.isChecked() == True:
        TocalCalo += 420
        ListMeal.append('chenep')
        # OTHER.append('chenep')
        CheckboxMeal[55] = True
    else:
        ui_1.chenep.isChecked() == False
        TocalCalo -= 420
        ListMeal.remove('chenep')
        # OTHER.remove('chenep')
        CheckboxMeal[55] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def chetroinuoc():
    global TocalCalo,OTHER
    if ui_1.chetroinuoc.isChecked() == True:
        TocalCalo += 513
        ListMeal.append('chetroinuoc')
        # OTHER.append('chetroinuoc')
        CheckboxMeal[56] = True
    else:
        ui_1.chetroinuoc.isChecked() == False
        TocalCalo -= 513
        ListMeal.remove('chetroinuoc')
        # OTHER.remove('chetroinuoc')
        CheckboxMeal[56] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def xoibap():
    global TocalCalo,OTHER
    if ui_1.xoibap.isChecked() == True:
        TocalCalo += 332
        ListMeal.append('xoibap')
        # OTHER.append('xoibap')
        CheckboxMeal[57] = True
    else:
        ui_1.xoibap.isChecked() == False
        TocalCalo -= 332
        ListMeal.remove('xoibap')
        # OTHER.remove('xoibap')
        CheckboxMeal[57] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def xoidauden():
    global TocalCalo,OTHER
    if ui_1.xoidauden.isChecked() == True:
        TocalCalo += 550
        ListMeal.append('xoidauden')
        # OTHER.append('xoidauden')
        CheckboxMeal[58] = True
    else:
        ui_1.xoidauden.isChecked() == False
        TocalCalo -= 550
        ListMeal.remove('xoidauden')
        # OTHER.remove('xoidauden')
        CheckboxMeal[58] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def xoidauphong():
    global TocalCalo,OTHER
    if ui_1.xoidauphong.isChecked() == True:
        TocalCalo += 650
        ListMeal.append('xoidauphong')
        # OTHER.append('xoidauphong')
        CheckboxMeal[59] = True
    else:
        ui_1.xoidauphong.isChecked() == False
        TocalCalo -= 650
        ListMeal.remove('xoidauphong')
        # OTHER.remove('xoidauphong')
        CheckboxMeal[59] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def xoigac():
    global TocalCalo,OTHER
    if ui_1.xoigac.isChecked() == True:
        TocalCalo += 590
        ListMeal.append('xoigac')
        # OTHER.append('xoigac')
        CheckboxMeal[60] = True
    else:
        ui_1.xoigac.isChecked() == False
        TocalCalo -= 590
        ListMeal.remove('xoigac')
        # OTHER.remove('xoigac')
        CheckboxMeal[60] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def cafe():
    global TocalCalo,OTHER
    if ui_1.cafe.isChecked() == True:
        TocalCalo += 40
        ListMeal.append('cafe')
        # OTHER.append('cafe')
        CheckboxMeal[61] = True
    else:
        ui_1.cafe.isChecked() == False
        TocalCalo -= 40
        ListMeal.remove('cafe')
        # OTHER.remove('cafe')
        CheckboxMeal[61] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def nuocam():
    global TocalCalo,OTHER
    if ui_1.nuocam.isChecked() == True:
        TocalCalo += 226
        ListMeal.append('nuocam')
        # OTHER.append('nuocam')
        CheckboxMeal[62] = True
    else:
        ui_1.nuocam.isChecked() == False
        TocalCalo -= 226
        ListMeal.remove('nuocam')
        # OTHER.remove('nuocam')
        CheckboxMeal[62] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def nuocchanh():
    global TocalCalo,OTHER
    if ui_1.nuocchanh.isChecked() == True:
        TocalCalo += 150
        ListMeal.append('nuocchanh')
        # OTHER.append('nuocchanh')
        CheckboxMeal[63] = True
    else:
        ui_1.nuocchanh.isChecked() == False
        TocalCalo -= 150
        ListMeal.remove('nuocchanh')
        # OTHER.remove('nuocchanh')
        CheckboxMeal[63] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def nuocmia():
    global TocalCalo,OTHER
    if ui_1.nuocmia.isChecked() == True:
        TocalCalo += 100
        ListMeal.append('nuocmia')
        # OTHER.append('nuocmia')
        CheckboxMeal[64] = True
    else:
        ui_1.nuocmia.isChecked() == False
        TocalCalo -= 100
        ListMeal.remove('nuocmia')
        # OTHER.remove('nuocmia')
        CheckboxMeal[64] = True
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def nuocrauma():
    global TocalCalo,OTHER
    if ui_1.nuocrauma.isChecked() == True:
        TocalCalo += 174
        ListMeal.append('nuocrauma')
        # OTHER.append('nuocrauma')
        CheckboxMeal[65] = True
    else:
        ui_1.nuocrauma.isChecked() == False
        TocalCalo -= 174
        ListMeal.remove('nuocrauma')
        # OTHER.remove('nuocrauma')
        CheckboxMeal[65] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def suachua():
    global TocalCalo,OTHER
    if ui_1.suachua.isChecked() == True:
        TocalCalo += 150
        ListMeal.append('suachua')
        # OTHER.append('suachua')
        CheckboxMeal[66] = True
    else:
        ui_1.suachua.isChecked() == False
        TocalCalo -= 150
        ListMeal.remove('suachua')
        # OTHER.remove('suachua')
        CheckboxMeal[66] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def trungcut():
    global TocalCalo,OTHER
    if ui_1.trungcut.isChecked() == True:
        TocalCalo += 17
        ListMeal.append('trungcut')
        # OTHER.append('trungcut')
        CheckboxMeal[67] = True
    else:
        ui_1.trungcut.isChecked() == False
        TocalCalo -= 17
        ListMeal.remove('trungcut')
        # OTHER.remove('trungcut')
        CheckboxMeal[67] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def trungga():
    global TocalCalo,OTHER
    if ui_1.trungga.isChecked() == True:
        TocalCalo += 58
        ListMeal.append('trungga')
        # OTHER.append('trungga')
        CheckboxMeal[68] = True
    else:
        ui_1.trungga.isChecked() == False
        TocalCalo -= 58
        ListMeal.remove('trungga')
        # OTHER.remove('trungga')
        CheckboxMeal[68] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)
def trungvit():
    global TocalCalo,OTHER
    if ui_1.trungvit.isChecked() == True:
        TocalCalo += 70
        ListMeal.append('trungvit')
        # OTHER.append('trungvit')
        CheckboxMeal[69] = True
    else:
        ui_1.trungvit.isChecked() == False
        TocalCalo -= 70
        ListMeal.remove('trungvit')
        # OTHER.remove('trungvit')
        CheckboxMeal[69] = False
    ui_1.label_4.setText(str(TocalCalo))
    ui_1.listWidget_2.clear()
    ui_1.listWidget_2.addItems(ListMeal)


def SettingFunction():
    ui = Setting.Ui_MainWindow()
    MainWindow.setFixedSize(544, 513)
    ui.setupUi(MainWindow)
    ui.updateprofile.clicked.connect(UpdateProfile)
    ui.changepassword.clicked.connect(ChangePassWord)
    ui.logout.clicked.connect(LoginScreen)
    ui.logout_2.clicked.connect(LoadmainScreen)


def SupportFunction():
    chat_client.FirstScreen("Tung")


def signupfunction():
    global user
    global password
    user = ui.user.text()
    password = ui.password.text()
    confirmpassword = ui.confirmpassword.text()
    if len(user) == 0 or len(password) == 0 or len(confirmpassword) == 0:
        ui.error.setText("Please fill in all inputs.")

    elif password != confirmpassword:
        ui.error.setText("Passwords do not match.")
    else:
        # cred = credentials.Certificate("firebase-sdk.json")
        # firebase_admin.initialize_app(cred, {'databaseURL': 'https://fitnessapp-5b974-default-rtdb.firebaseio.com/'})
        # ref = db.reference('3')
        # ref.set({
        #     'User': user,
        #     'Pasword': password
        # })
        conn = sqlite3.connect("shop_data.db")
        cur = conn.cursor()

        user_info = [user, password]
        cur.execute('INSERT INTO login_info (username, password) VALUES (?,?)', user_info)
        conn.commit()
        conn.close()


# def CreateScreen():
#     global ui
#     MainWindow.setFixedSize(800, 450)
#     ui = createacc.Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     ui.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
#     ui.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
#     ui.signup.clicked.connect(signupfunction)
#     MainWindow.show()


def WelcomeScreen():
    ui = welcomescreen.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.login.clicked.connect(LoginScreen)


class MainWindowSceen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        MainWindow.setFixedSize(1201, 708)
        self.ui = MainMenu.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.ui.TimeTable.clicked.connect(TimeTableFunction)
        self.ui.Gym.clicked.connect(GymFunction)
        self.ui.Yoga.clicked.connect(YogaFunction)
        self.ui.Meal.clicked.connect(MealFunction)
        self.ui.Profile.clicked.connect(UpdateProfile)
        self.ui.Chat.clicked.connect(SupportFunction)
        self.ui.label_3.setText(str(CaloNeed))

        self.Calo = db.reference('StatusValue').child('Calo')
        # self.Meal = db.reference('StatusValue').child('Meal')
        # self.Status = db.reference('StatusValue').child('Status')

        # processbar calo
        self.setValue(self.Calo.get(), self.ui.labelPercentageCPU, self.ui.circularProgressCPU,
                      "rgb(255, 170, 0)")
        # self.ui.label_3.setText(CaloNeed)
        # processbar Status
        # self.setValue(self.Meal.get(), self.ui.labelPercentageGPU, self.ui.circularProgressGPU,
        #               "rgba(85, 255, 127, 255)")
        # # processbar Meal
        # self.setValue(self.Status.get(), self.ui.labelPercentageRAM, self.ui.circularProgressRAM,
        #               "rgba(255, 0, 127, 255)")

        ## ==> SET VALUES TO DEF progressBarValue

    def setValue(self, slider, labelPercentage, progressBarName, color):
        # GET SLIDER VALUE
        # value = slider.value()
        value = slider

        # CONVERT VALUE TO INT
        sliderValue = int(value)

        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

        # CALL DEF progressBarValue
        self.progressBarValue(sliderValue, progressBarName, color)

        ## ==> APPLY VALUES TO PROGREESBAR
        # self.ui.sliderCPU.valueChanged.connect(lambda: setValue(self, self.ui.sliderCPU, self.ui.labelPercentageCPU, self.ui.circularProgressCPU, "rgba(85, 170, 255, 255)"))
        # self.ui.sliderGPU.valueChanged.connect(lambda: setValue(self, self.ui.sliderGPU, self.ui.labelPercentageGPU, self.ui.circularProgressGPU, "rgba(85, 255, 127, 255)"))
        # self.ui.sliderRAM.valueChanged.connect(lambda: setValue(self, self.ui.sliderRAM, self.ui.labelPercentageRAM, self.ui.circularProgressRAM, "rgba(255, 0, 127, 255)"))

        ## ==> DEF START VALUES
        # self.ui.sliderCPU.setValue(25)
        # self.ui.sliderGPU.setValue(65)
        # self.ui.sliderRAM.setValue(45)

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value, widget, color):
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)


## ==> SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_splash_screen.Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        # self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(10)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        t = threading.Thread(target=main)
        t.start()
        ## ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if (value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            MainWindow.show()
            LoginScreen()

            # CLOSE SPLASH SCREEN
            self.close()
            t = threading.Thread(target=main)
            t.start()

        # INCREASE COUNTER
        counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


# GYM
def count_task(z):  # z la chuc nang duoc quy dinh trong Gym
    # #func (function): lay chuc nang trong thu vien barbell_cruls
    global cp, func, giay_tt, func_yoga
    # playS("sound\\Button_1_down.wav", 0)
    # playS("sound\\count.wav", 1)
    cp = 0
    bc.init(0)
    time.sleep(0.1)
    bc.init(1)
    tt.giay = 0
    # giay_tt = False
    cp = 1
    if (z == 0):
        func = 0
        func_yoga = 0
    elif (z == 1):
        func = 1
        func_yoga = 1
    elif (z == 2):
        func = 2
        func_yoga = 2
    elif (z == 3):
        func = 3
        func_yoga = 3
    elif (z == 4):
        func = 4
        func_yoga = 4
    elif (z == 5):
        func = 5
        func_yoga = 5
    elif (z == 6):
        func = 6
        func_yoga = 6
    elif (z == 7):
        func = 7
        func_yoga = 6
    elif(z == 8):
        func = 8
        func_yoga = 6
    else:
        func = 9
        func_yoga = 6

    # winsound.PlaySound('NhacGym1.WAV', winsound.SND_ASYNC)


def count_task_yoga(y):  # z la chuc nang duoc quy dinh trong Yoga
    global cp, giay_tt, func_yoga
    # playS("sound\\Button_1_down.wav", 0)
    # playS("sound\\count.wav", 1)
    cp = 0
    yp.init(0)
    time.sleep(0.1)
    yp.init(1)
    tt.giay = 0
    # giay_tt = False
    cp = 2

    if (y == 0):
        func_yoga = 0
    elif (y == 1):
        func_yoga = 1
    elif (y == 2):
        func_yoga = 2
    elif (y == 3):
        func_yoga = 3
    elif (y == 4):
        func_yoga = 4
    elif (y == 5):
        func_yoga = 5
    else:
        func_yoga = 6

def hienhinhyoga(a):
        # hien thi anh len khung information
        image_path = "hinh\\" + a  # path to your image file
        image_profile = QtGui.QImage(image_path)  # QImage object
        image_profile = image_profile.scaled(261, 241)  # To scale image for example and keep its Aspect Ration
        ui.information_yoga.setPixmap(QtGui.QPixmap.fromImage(image_profile))

def hienhinh(a, b, per):
    if (per <= 20):
        # hien thi anh len khung information
        image_path = "hinh\\" + a  # path to your image file
        image_profile = QtGui.QImage(image_path)  # QImage object
        image_profile = image_profile.scaled(261, 241)  # To scale image for example and keep its Aspect Ration
        ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))



    elif (per >= 90):
        # label_Image = QtGui.QLabel(frame)
        image_path = "hinh\\" + b  # path to your image file
        image_profile = QtGui.QImage(image_path)  # QImage object
        image_profile = image_profile.scaled(261, 241)  # To scale image for example and keep its Aspect Ration
        ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))

def h_playS(a, b):  # b la cho phep chay vong lap    #0 la 1 lan, 1 la nhieu lan
    # AM THANH
    # playsound.playsound(a)
    winsound.PlaySound(a, winsound.SND_LOOP + (winsound.SND_ASYNC & b))


def playS(a, b):
    s = threading.Thread(target=h_playS, args=(a, b))
    s.start()


def h_playS1(a):  # b la cho phep chay vong lap    #0 la 1 lan, 1 la nhieu la
	# AM THANH
	playsound.playsound(a)


def playS1(a):
        s = threading.Thread(target=h_playS1, args=(a,))
        s.start()




############################################################################
#######  CHUONG TRINH CHINH
############################################################################
def main():
    global img, ui, rep, func, flagRight, check, dem, yoga_hinh, phut_tt, check2,func_yoga,CaloNeed,now,toast,status
    bc.count = 0
    while True:
        print(CaloNeed)
        if (now.hour == 8) & (status == True):
            toast = ToastNotifier()
            toast.show_toast(
                "Fitness App",
                "Let do exercise",
                duration=20,
                icon_path=r"C:\Users\TEMP\Downloads\LoginInterface\pyqt5-full-app-tutorial-for-beginners-main\emojis\icon.ico",
                threaded=True,
            )
            status = False
        if cp == 1:
            # playS("sound\\Button_1_down.wav", 0)
            img, per, rep = bc.run(600, 450, func)
            # hien thi hinh anh len khung view label
            image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            ui.view.setPixmap(QtGui.QPixmap.fromImage(image))

            # hien thi dem thoi gian
            ui.timeLabel.setText("00:" + str(int(tt.giay / 10)) + str(int(tt.giay % 10)))
            ui.lcdNumber.display(rep)
            hienhinh("tay-tadon -2.jpg", "tay-tadon-1.jpg", per)


        if cp == 2:
            # playS("sound\\Button_1_down.wav", 0)
            img, check, dem, z = yp.run(600, 450, func_yoga)
            # hien thi hinh anh len khung view label
            image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            ui.view_yoga.setPixmap(QtGui.QPixmap.fromImage(image))

            # hien thi dem thoi gian
            ui.timeLabel_yoga.setText("00:" + str(int(tt.giay / 10)) + str(int(tt.giay % 10)))
            # ui.lcdNumber_yoga.display(rep)
            hienhinhyoga("pose-tree.jpg")


app = QApplication(sys.argv)
splashscreen = SplashScreen()
MainWindow = QtWidgets.QMainWindow()
window = QtWidgets.QMainWindow()
MainWindow.setFixedSize(340, 340)
tt.init()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")

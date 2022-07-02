import sys
# from PyQt5 import QtWidgets
from PySide2 import QtGui, QtWidgets, QtCore
# from PyQt5.uic.properties import QtGui
import sys, time, threading, playsound, winsound
from PySide2 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PySide2.QtGui import QPixmap, QColor
import firebase_admin
from PySide2.QtGui import QColor, QIcon,QPalette
from PySide2.QtWidgets import *
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2extn.SpiralProgressBar import spiralProgressBar
import  fillprofile, MainMenu, login, Gym, ui_splash_screen, timetable, Calo, \
    Yoga,MealSelectDinner,MealSelectLunch,MealSelectBreakFast
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

running = False
max_value = 20
Name=''
CaloNeed = 0
Height = 0
Age = 0
Weight = 0
Index = 0
TocalCalo = 0
TocalCaloBreakFast = 0
TocalCaloDinner = 0
TocalCaloLunch = 0
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
func_yoga=1
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
y = 1
#variable for notification
status = True
# declare object to notify
toast = ToastNotifier()




IMG = ["border-image : url(:/Image/hit-dat.jpg)\n;", "border-image : url(:/Image/dumbbell_shoulder.jpg);\n",
       "border-image: url(:/Image/nguc-truoc-voi-ta-don.jpg);\n",
       "border-image: url(:/Image/ta-don1.jpg);\n", "border-image : url(:/Image/tay-sau-voi-ghe.jpg);\n",
       "border-image : url(:/Image/swat.jpg);\n"
    , "border-image: url(:/Image/gap-bung.jpg);\n", "border-image : url(:/Image/blank-thang-tay.jpg);\n","border-image : url(:/Image/White_full.png);\n"]
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
File_Mon = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Mon.txt","r")
File_Tue = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Tue.txt","r")
File_Wed = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Wed.txt","r")
File_Thurs = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Thurs.txt","r")
File_Fri = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Fri.txt","r")
File_Sat = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Sat.txt","r")
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
checkbox = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox.txt","r")
checkboxLunch = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox_Lunch.txt","r")
checkboxDinner = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox_Dinner.txt","r")
ListMealWidgetBreakfast = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal.txt","r")
ListMealWidgetLunch = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal_Lunch.txt","r")
ListMealWidgetDinner = open(r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal_Dinner.txt","r")
for indexCheckbox in range(69):
    #breakfasst
    if checkbox.readline() == 'True\n':
        CheckboxMeal[indexCheckbox] =True
    else:
        CheckboxMeal[indexCheckbox] =False
    #Lunch
    if checkboxLunch.readline() == 'True\n':
        CheckboxMealLunch[indexCheckbox] =True
    else:
        CheckboxMealLunch[indexCheckbox] =False
        #dinner
    if checkboxDinner.readline() == 'True\n':
        CheckboxMealDinner[indexCheckbox] =True
    else:
        CheckboxMealDinner[indexCheckbox] =False
for indexmeal in range(10):
    LoadMealFromFile = ListMealWidgetBreakfast.readline().strip('\n')
    LoadMealFromFileLunch = ListMealWidgetLunch.readline().strip('\n')
    LoadMealFromFileDinner = ListMealWidgetDinner.readline().strip('\n')
    if LoadMealFromFile != '':
        ListMeal.append(LoadMealFromFile)
    if LoadMealFromFileLunch != '':
        ListMealLunch.append(LoadMealFromFileLunch)
    if LoadMealFromFileDinner != '':
        ListMealDinner.append(LoadMealFromFileDinner)
# print (ListMeal)
# print (ListMealLunch)
# print (ListMealDinner)

#close file
checkbox.close()
ListMealWidgetBreakfast.close()
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
#
# })
# Get CurrentTime
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
#
# print("Current Time is :", current_time)

def LoginScreen():
    global ui
    MainWindow.setFixedSize(800, 450)
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
    ui.login.clicked.connect(loginfunction)



def loginfunction():
    global Name,Weight,Height,Age,CaloNeed,user,TocalCaloBreakFast,TocalCaloLunch,TocalCaloDinner
    user = ui.emailfield.text()
    password = ui.passwordfield.text()
    if len(user) == 0 or len(password) == 0:
        ui.error.setText("Please input all fields.")

    else:
        for i in range(1, 3):
            User = db.reference(str(i) + '/User').get()
            Password = db.reference(str(i) + '/Password').get()
            if (Password == password) and (User == user):
                print("Successfully logged in.")
                Name = db.reference(str(user)).child('ProFile/Name').get()
                Weight = db.reference(str(user)).child('ProFile/Weight').get()
                Height = db.reference(str(user)).child('ProFile/Height').get()
                Age = db.reference(str(user)).child('ProFile/Age').get()
                CaloNeed = db.reference(str(user)).child('ProFile/CaloNeed').get()
                TocalCaloBreakFast = db.reference(str(user)).child('ToTalCaloBreakFast').get()
                TocalCaloLunch = db.reference(str(user)).child('ToTalCaloLunch').get()
                TocalCaloDinner = db.reference(str(user)).child('ToTalCaloDinner').get()
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
    winsound.PlaySound(None, winsound.SND_PURGE)
    #savedata
    File_Mon = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Mon.txt", "w")
    File_Tue = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Tue.txt", "w")
    File_Wed = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Wed.txt", "w")
    File_Thurs = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Thurs.txt", "w")
    File_Fri = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Fri.txt", "w")
    File_Sat = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Sat.txt", "w")
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
    global ui,user
    ui = fillprofile.Ui_MainWindow()
    MainWindow.setFixedSize(903, 706)
    ui.setupUi(MainWindow)

    #wait

    ui.username.setText(str(Name))
    ui.Height_2.setText(str(Height))
    ui.Age.setText(str(Age))
    ui.Weight.setText(str(Weight))
    ui.signup.clicked.connect(getdatafrominput)
    ui.signup_2.clicked.connect(MainWindowSceen)


def getdatafrominput():
    global Weight,CaloNeed,Height,Age,Name,user

    Name = str(ui.username.text())
    Weight = int(ui.Weight.text())
    Height = int(ui.Height_2.text())
    Age = int(ui.Age.text())
    CaloNeed = int(((Weight * 13.397) + (4.799 * Height) - (5.677 * Age) + 447.593) * 1.55)
    ref = db.reference('/').child(str(user))
    ref.update({
        str('ProFile'):{
                'Name'   : str(Name),
                'Height' : Height,
                'Weight' : Weight,
                'Age'    : Age,
                'CaloNeed' :CaloNeed
        }});

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
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Mon[0] = IMG[Image_TimeTable]
    ui.pushButton.setStyleSheet(Mon[0])


def changeImageMonIMG2():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Mon[1] = IMG[Image_TimeTable]
    ui.pushButton_2.setStyleSheet(Mon[1])


def changeImageMonIMG3():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Mon[2] = IMG[Image_TimeTable]
    ui.pushButton_3.setStyleSheet(Mon[2])


def changeImageTueIMG4():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Tue[0] = IMG[Image_TimeTable]
    ui.pushButton_4.setStyleSheet(Tue[0])


def changeImageTueIMG5():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Tue[1] = IMG[Image_TimeTable]
    ui.pushButton_5.setStyleSheet(Tue[1])


def changeImageTueIMG6():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Tue[2] = IMG[Image_TimeTable]
    ui.pushButton_6.setStyleSheet(Tue[2])


def changeImageWedIMG7():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Wed[0] = IMG[Image_TimeTable]
    ui.pushButton_7.setStyleSheet(Wed[0])


def changeImageWedIMG8():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Wed[1] = IMG[Image_TimeTable]
    ui.pushButton_8.setStyleSheet(Wed[1])


def changeImageWedIMG9():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Wed[2] = IMG[Image_TimeTable]
    ui.pushButton_9.setStyleSheet(Wed[2])


def changeImageThursIMG10():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Thurs[0] = IMG[Image_TimeTable]
    ui.pushButton_10.setStyleSheet(Thurs[0])


def changeImageThursIMG11():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Thurs[1] = IMG[Image_TimeTable]
    ui.pushButton_11.setStyleSheet(Thurs[1])


def changeImageThursIMG12():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Thurs[2] = IMG[Image_TimeTable]
    ui.pushButton_12.setStyleSheet(Thurs[2])


def changeImageFriIMG13():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Fri[0] = IMG[Image_TimeTable]
    ui.pushButton_13.setStyleSheet(Fri[0])


def changeImageFriIMG14():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Fri[1] = IMG[Image_TimeTable]
    ui.pushButton_14.setStyleSheet(Fri[1])


def changeImageFriIMG15():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Fri[2] = IMG[Image_TimeTable]
    ui.pushButton_15.setStyleSheet(Fri[2])


def changeImageSatIMG16():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Sat[0] = IMG[Image_TimeTable]
    ui.pushButton_16.setStyleSheet(Sat[0])


def changeImageSatIMG17():
    global Image_TimeTable
    if Image_TimeTable <= 7:
        Image_TimeTable += 1
    else:
        Image_TimeTable = 0
    Sat[1] = IMG[Image_TimeTable]
    ui.pushButton_17.setStyleSheet(Sat[1])


def changeImageSatIMG18():
    global Image_TimeTable
    if Image_TimeTable <= 7:
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
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video",r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\VideoGuide\video-dong-tac-gym")

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
        y = 1
    elif string == "Tree pose":
        y = 2
    elif string == "Triangle pose":
        y = 3
    elif string == "Plank High":
        y = 4
    elif string == "Plank Low":
        y = 5
    elif string == "Boat pose":
        y = 6
    elif string == "Cobra pose":
        y = 7

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

def mute_yoga():
    global volume
    if volume == 0:
        ui.mute_2.setStyleSheet("QPushButton {border-image : url(:/MENU/mute.png)}")
        winsound.PlaySound(None, winsound.SND_PURGE)
        volume = 1;
    else:
        ui.mute_2.setStyleSheet("QPushButton {border-image : url(:/MENU/unmute.png)}")
        volume = 0;
        winsound.PlaySound('NhacGym1.WAV', winsound.SND_ASYNC)

class YogaWinDow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Yoga.Ui_MainWindow()
		self.ui.setupUi(self)
		#self.show()
		# self.ui.pushButton.clicked.connect(self.go)
		# self.ui.pushButton1.clicked.connect(self.change)
		QtCore.QTimer.singleShot(0,lambda:self.ui.widget.rpb_setValue(0))
		self.ui.widget.rpb_setBarStyle('Hybrid2')
		self.ui.widget.rpb_setLineColor((255, 255, 255))
		self.ui.widget.rpb_setMaximum(300)
		# self.ui.Start_yoga.clicked.connect(self.go)




def update():
    global progress_val
    ui.widget.rpb_setValue(progress_val)
    if progress_val > 299:
        progress_val = 0
        timer.stop()
    progress_val += 1


def YogaFunction():
    global ui
    ui = Yoga.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.Start_yoga.clicked.connect(lambda: count_task_yoga(y))
    ui.back_yoga.clicked.connect(LoadmainScreen)
    ui.mute_yoga.clicked.connect(mute_yoga)
    ui.comboBox_yoga.currentTextChanged.connect(comboboxFuntionYoga)
    ui.widget.rpb_setBarStyle('Hybrid2')
    ui.widget.rpb_setLineColor((255, 255, 255))
    ui.widget.rpb_setMaximum(max_value)
    ui.SeeVideo_yoga.clicked.connect(MediaPlayer)
    ui.spinBox.setValue(max_value)
    ui.spinBox.valueChanged.connect(show_result)

def show_result():
    global max_value
    max_value = ui.spinBox.value()
    ui.widget.rpb_setMaximum(max_value)

def MealFunction():
    global ui,toast
    ui = Calo.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(MealSelectForBreakFast)
    ui.pushButton_2.clicked.connect(MealSelectWindowForLunch)
    ui.pushButton_3.clicked.connect(MealSelectWindowForDinner)
    ui.label_7.setText(str(int(CaloNeed * 0.15)))
    ui.label_11.setText(str(int(CaloNeed * 0.5)))
    ui.label_15.setText(str(int(CaloNeed * 0.2)))
    ui.Back_Calo.clicked.connect(LoadmainScreen)

    #Load data from file text
    TocalCaloBreakFast = db.reference(str(user)).child('ToTalCaloBreakFast').get()
    TocalCaloLunch = db.reference(str(user)).child('ToTalCaloLunch').get()
    TocalCaloDinner = db.reference(str(user)).child('ToTalCaloDinner').get()

    #Load to roundprocessbar
    # processbar calo
    # Display Calo to table
    ui.label_14.setText(str(TocalCaloDinner))
    ui.label_10.setText(str(TocalCaloLunch))
    ui.label_6.setText(str(TocalCaloBreakFast))
    ui.Eat.setText(str(TocalCaloDinner+TocalCaloLunch+TocalCaloBreakFast))
    if ( (TocalCaloDinner + TocalCaloBreakFast + TocalCaloLunch) > CaloNeed):
        toast.show_toast(
            "Fitness App",
            "Bạn đang ăn quá mức calo tiêu chuẩn",
            duration=20,
            icon_path=r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\emojis\icon.ico",
            threaded=True,
        )
    else:
        toast.show_toast(
            "Fitness App",
            "Bạn đang ăn ít hơn calo tiêu chuẩn.",
            duration=20,
            icon_path=r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\emojis\icon.ico",
            threaded=True,
        )

        # processbar calo
        setValue(TocalCaloLunch+ TocalCaloBreakFast + TocalCaloDinner , ui.labelPercentageCPU,ui.circularProgressCPU,
                      "rgb(255, 170, 0)")


def setValue(slider, labelPercentage, progressBarName, color):
            # GET SLIDER VALUE
            # value = slider.value()
    value = slider

            # CONVERT VALUE TO INT
    sliderValue = int(value)

            # HTML TEXT PERCENTAGE
    htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
    labelPercentage.setText(htmlText.replace("{VALUE}", str(int((sliderValue/CaloNeed)*100))))

            # CALL DEF progressBarValue
    progressBarValue(int((sliderValue/CaloNeed)*100), progressBarName, color)

def progressBarValue(value, widget, color):
            # PROGRESSBAR STYLESHEET BASE
    styleSheet = """
        QFrame{
            border-radius: 110px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

            # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
            # stop works of 1.000 to 0.000
    if(value > 100):
        progress = (100 - 100) / 100.0
    else:
        print(int((value/CaloNeed)*100) / 100.0)
        progress = ((100 - value) / 100.0)

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

class MealSelectForBreakFast:
    def __init__(self):
        global window,CaloBreakFast,ui_1, CheckboxMeal, ListMeal,TocalCalo
        window = QtWidgets.QMainWindow()
        ui_1 = MealSelectBreakFast.Ui_MainWindow()
        ui_1.setupUi(window)
        window.show()
        TocalCaloBreakFast = db.reference(str(user)).child('ToTalCaloBreakFast').get()
        #Display Calo For breakfase
        ui_1.label_12.setText(str(TocalCaloBreakFast))
        TocalCalo = TocalCaloBreakFast
        # display meal to listview
        ui_1.listWidget_4.clear()
        ui_1.listWidget_4.addItems(ListMeal)

        # Display checkbox
        ui_1.gaxaot_2.setChecked(CheckboxMeal[0])
        ui_1.gakho_2.setChecked(CheckboxMeal[1])
        ui_1.mucxao_2.setChecked(CheckboxMeal[2])
        ui_1.suongnuong_2.setChecked(CheckboxMeal[3])
        ui_1.suongram_2.setChecked(CheckboxMeal[4])
        ui_1.thitheoquay_2.setChecked(CheckboxMeal[5])
        ui_1.thitboxao_2.setChecked(CheckboxMeal[6])
        ui_1.thitkhotieu_2.setChecked(CheckboxMeal[7])
        ui_1.camoikho_2.setChecked(CheckboxMeal[8])
        ui_1.cari_2.setChecked(CheckboxMeal[9])
        ui_1.bobia_2.setChecked(CheckboxMeal[10])
        ui_1.cabacmachien_2.setChecked(CheckboxMeal[11])
        ui_1.cabacmakho_2.setChecked(CheckboxMeal[12])
        ui_1.cangukho_2.setChecked(CheckboxMeal[13])
        ui_1.chalua_2.setChecked(CheckboxMeal[14])
        ui_1.ganheoxao_2.setChecked(CheckboxMeal[15])
        ui_1.goikhobo_2.setChecked(CheckboxMeal[16])
        ui_1.goitom_2.setChecked(CheckboxMeal[17])
        ui_1.khoquaxaotrung_2.setChecked(CheckboxMeal[18])
        ui_1.lapxuongchien_2.setChecked(CheckboxMeal[19])
        ui_1.mucxaothapcam_2.setChecked(CheckboxMeal[20])
        ui_1.boxaomang_2.setChecked(CheckboxMeal[21])
        ui_1.boxaonam_2.setChecked(CheckboxMeal[22])
        ui_1.thitkhotrung_2.setChecked(CheckboxMeal[23])
        ui_1.bunrieu_2.setChecked(CheckboxMeal[24])
        ui_1.bunbohue_2.setChecked(CheckboxMeal[25])
        ui_1.bunthitnuong_2.setChecked(CheckboxMeal[26])
        ui_1.bunxao_2.setChecked(CheckboxMeal[27])
        ui_1.canhkhoqua_2.setChecked(CheckboxMeal[28])
        ui_1.chaolong_2.setChecked(CheckboxMeal[29])
        ui_1.bo_2.setChecked(CheckboxMeal[31])
        ui_1.chuoi_2.setChecked(CheckboxMeal[32])
        ui_1.thom_2.setChecked(CheckboxMeal[33])
        ui_1.xoai_2.setChecked(CheckboxMeal[34])
        ui_1.saurieng_2.setChecked(CheckboxMeal[35])
        ui_1.mangcut_2.setChecked(CheckboxMeal[36])
        ui_1.coc_2.setChecked(CheckboxMeal[37])
        ui_1.nho_2.setChecked(CheckboxMeal[38])
        ui_1.duahau_2.setChecked(CheckboxMeal[39])
        ui_1.buoi_2.setChecked(CheckboxMeal[40])
        ui_1.khoailang_2.setChecked(CheckboxMeal[41])
        ui_1.le_2.setChecked(CheckboxMeal[42])
        ui_1.bapluoc_2.setChecked(CheckboxMeal[43])
        ui_1.khoaitay_2.setChecked(CheckboxMeal[44])
        ui_1.dauphong_2.setChecked(CheckboxMeal[45])
        ui_1.dudu_2.setChecked(CheckboxMeal[46])
        ui_1.sori_2.setChecked(CheckboxMeal[47])
        ui_1.cam_2.setChecked(CheckboxMeal[48])
        ui_1.oi_2.setChecked(CheckboxMeal[49])
        ui_1.thanhlong_2.setChecked(CheckboxMeal[50])
        ui_1.chebap_2.setChecked(CheckboxMeal[51])
        ui_1.chechuoi_2.setChecked(CheckboxMeal[52])
        ui_1.chedauden_2.setChecked(CheckboxMeal[53])
        ui_1.chedauxanh_2.setChecked(CheckboxMeal[54])
        ui_1.chenep_2.setChecked(CheckboxMeal[55])
        ui_1.chetroinuoc_2.setChecked(CheckboxMeal[56])
        ui_1.xoibap_2.setChecked(CheckboxMeal[57])
        ui_1.xoidauden_2.setChecked(CheckboxMeal[58])
        ui_1.xoidauphong_2.setChecked(CheckboxMeal[59])
        ui_1.xoigac_2.setChecked(CheckboxMeal[60])
        ui_1.cafe_2.setChecked(CheckboxMeal[61])
        ui_1.nuocam_2.setChecked(CheckboxMeal[62])
        ui_1.nuocchanh_2.setChecked(CheckboxMeal[63])
        ui_1.nuocmia_2.setChecked(CheckboxMeal[64])
        ui_1.nuocrauma_2.setChecked(CheckboxMeal[65])
        ui_1.suachua_2.setChecked(CheckboxMeal[66])
        ui_1.trungcut_2.setChecked(CheckboxMeal[67])
        ui_1.trungga_2.setChecked(CheckboxMeal[68])
        ui_1.trungvit_2.setChecked(CheckboxMeal[69])

        ui_1.Save.clicked.connect(SaveMealBreakFast)
        # ui_1.Save.setEnabled(False)

        # if checkbox change state will call function
        ui_1.gaxaot_2.stateChanged.connect(lambda: gaxaot(ListMeal,CheckboxMeal))
        ui_1.gakho_2.stateChanged.connect(lambda: gakho(ListMeal,CheckboxMeal))
        ui_1.mucxao_2.stateChanged.connect(lambda:mucxao(ListMeal,CheckboxMeal))
        ui_1.suongnuong_2.stateChanged.connect(lambda:suongnuong(ListMeal,CheckboxMeal))
        ui_1.suongram_2.stateChanged.connect(lambda:suongram(ListMeal,CheckboxMeal))
        ui_1.thitheoquay_2.stateChanged.connect(lambda:thitheoquay(ListMeal,CheckboxMeal))
        ui_1.thitboxao_2.stateChanged.connect(lambda:thitboxao(ListMeal,CheckboxMeal))
        ui_1.thitkhotieu_2.stateChanged.connect(lambda:thitkhotieu(ListMeal,CheckboxMeal))
        ui_1.camoikho_2.stateChanged.connect(lambda:camoikho(ListMeal,CheckboxMeal))
        ui_1.cari_2.stateChanged.connect(lambda:cari(ListMeal,CheckboxMeal))
        ui_1.bobia_2.stateChanged.connect(lambda:bobia(ListMeal,CheckboxMeal))
        ui_1.cabacmachien_2.stateChanged.connect(lambda:cabacmachien(ListMeal,CheckboxMeal))
        ui_1.cabacmakho_2.stateChanged.connect(lambda:cabacmakho(ListMeal,CheckboxMeal))
        ui_1.cangukho_2.stateChanged.connect(lambda:cangukho(ListMeal,CheckboxMeal))
        ui_1.chalua_2.stateChanged.connect(lambda:chalua(ListMeal,CheckboxMeal))
        ui_1.ganheoxao_2.stateChanged.connect(lambda:ganheoxao(ListMeal,CheckboxMeal))
        ui_1.goikhobo_2.stateChanged.connect(lambda:goikhobo(ListMeal,CheckboxMeal))
        ui_1.goitom_2.stateChanged.connect(lambda:goitom(ListMeal,CheckboxMeal))
        ui_1.khoquaxaotrung_2.stateChanged.connect(lambda:khoquaxaotrung(ListMeal,CheckboxMeal))
        ui_1.lapxuongchien_2.stateChanged.connect(lambda:lapxuongchien(ListMeal,CheckboxMeal))
        ui_1.mucxaothapcam_2.stateChanged.connect(lambda:mucxaothapcam(ListMeal,CheckboxMeal))
        ui_1.boxaomang_2.stateChanged.connect(lambda:boxaomang(ListMeal,CheckboxMeal))
        ui_1.boxaonam_2.stateChanged.connect(lambda:boxaonam(ListMeal,CheckboxMeal))
        ui_1.thitkhotrung_2.stateChanged.connect(lambda:thitkhotrung(ListMeal,CheckboxMeal))
        ui_1.bunrieu_2.stateChanged.connect(lambda:bunrieu(ListMeal,CheckboxMeal))
        ui_1.bunbohue_2.stateChanged.connect(lambda:bunbohue(ListMeal,CheckboxMeal))
        ui_1.bunthitnuong_2.stateChanged.connect(lambda:bunthitnuong(ListMeal,CheckboxMeal))
        ui_1.bunxao_2.stateChanged.connect(lambda:bunxao(ListMeal,CheckboxMeal))
        ui_1.canhkhoqua_2.stateChanged.connect(lambda:canhkhoqua(ListMeal,CheckboxMeal))
        ui_1.chaolong_2.stateChanged.connect(lambda:chaolong(ListMeal,CheckboxMeal))
        ui_1.bo_2.stateChanged.connect(lambda:bo(ListMeal,CheckboxMeal))
        ui_1.chuoi_2.stateChanged.connect(lambda:chuoi(ListMeal,CheckboxMeal))
        ui_1.thom_2.stateChanged.connect(lambda:thom(ListMeal,CheckboxMeal))
        ui_1.xoai_2.stateChanged.connect(lambda:xoai(ListMeal,CheckboxMeal))
        ui_1.saurieng_2.stateChanged.connect(lambda:saurieng(ListMeal,CheckboxMeal))
        ui_1.mangcut_2.stateChanged.connect(lambda:mangcut(ListMeal,CheckboxMeal))
        ui_1.coc_2.stateChanged.connect(lambda:coc(ListMeal,CheckboxMeal))
        ui_1.nho_2.stateChanged.connect(lambda:nho(ListMeal,CheckboxMeal))
        ui_1.duahau_2.stateChanged.connect(lambda:duahau(ListMeal,CheckboxMeal))
        ui_1.buoi_2.stateChanged.connect(lambda:buoi(ListMeal,CheckboxMeal))
        ui_1.khoailang_2.stateChanged.connect(lambda:khoailang(ListMeal,CheckboxMeal))
        ui_1.le_2.stateChanged.connect(lambda:le(ListMeal,CheckboxMeal))
        ui_1.bapluoc_2.stateChanged.connect(lambda:bapluoc(ListMeal,CheckboxMeal))
        ui_1.khoaitay_2.stateChanged.connect(lambda:khoaitay(ListMeal,CheckboxMeal))
        ui_1.dauphong_2.stateChanged.connect(lambda:dauphong(ListMeal,CheckboxMeal))
        ui_1.dudu_2.stateChanged.connect(lambda:dudu(ListMeal,CheckboxMeal))
        ui_1.sori_2.stateChanged.connect(lambda:sori(ListMeal,CheckboxMeal))
        ui_1.cam_2.stateChanged.connect(lambda:cam(ListMeal,CheckboxMeal))
        ui_1.oi_2.stateChanged.connect(lambda:oi(ListMeal,CheckboxMeal))
        ui_1.thanhlong_2.stateChanged.connect(lambda:thanhlong(ListMeal,CheckboxMeal))
        ui_1.chebap_2.stateChanged.connect(lambda:chebap(ListMeal,CheckboxMeal))
        ui_1.chechuoi_2.stateChanged.connect(lambda:chechuoi(ListMeal,CheckboxMeal))
        ui_1.chedauden_2.stateChanged.connect(lambda:chedauden(ListMeal,CheckboxMeal))
        ui_1.chedauxanh_2.stateChanged.connect(lambda:chedauxanh(ListMeal,CheckboxMeal))
        ui_1.chenep_2.stateChanged.connect(lambda:chenep(ListMeal,CheckboxMeal))
        ui_1.chetroinuoc_2.stateChanged.connect(lambda:chetroinuoc(ListMeal,CheckboxMeal))
        ui_1.xoibap_2.stateChanged.connect(lambda:xoibap(ListMeal,CheckboxMeal))
        ui_1.xoidauden_2.stateChanged.connect(lambda:xoidauden(ListMeal,CheckboxMeal))
        ui_1.xoidauphong_2.stateChanged.connect(lambda:xoidauphong(ListMeal,CheckboxMeal))
        ui_1.xoigac_2.stateChanged.connect(lambda:xoigac(ListMeal,CheckboxMeal))
        ui_1.cafe_2.stateChanged.connect(lambda:cafe(ListMeal,CheckboxMeal))
        ui_1.nuocam_2.stateChanged.connect(lambda:nuocam(ListMeal,CheckboxMeal))
        ui_1.nuocchanh_2.stateChanged.connect(lambda:nuocchanh(ListMeal,CheckboxMeal))
        ui_1.nuocmia_2.stateChanged.connect(lambda:nuocmia(ListMeal,CheckboxMeal))
        ui_1.nuocrauma_2.stateChanged.connect(lambda:nuocrauma(ListMeal,CheckboxMeal))
        ui_1.suachua_2.stateChanged.connect(lambda:suachua(ListMeal,CheckboxMeal))
        ui_1.trungcut_2.stateChanged.connect(lambda:trungcut(ListMeal,CheckboxMeal))
        ui_1.trungga_2.stateChanged.connect(lambda:trungga(ListMeal,CheckboxMeal))
        ui_1.trungvit_2.stateChanged.connect(lambda:trungvit(ListMeal,CheckboxMeal))

def SaveMealBreakFast():
    global FOOD, ListMeal, CheckboxMeal,CaloBreakFast,TocalCalo,user
    ListMealDB = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal.txt",
        "w")
    CheckboxDB = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox.txt",
        "w")
    CaloBreakFast = str(ui_1.label_12.text())
        # ListMeal
    for d in range(len(ListMeal)):
        ListMealDB.writelines(ListMeal[d] + '\n')
        # Checkbox
    for e in range(len(CheckboxMeal)):
        CheckboxDB.writelines(str(CheckboxMeal[e]) + '\n')
    db.reference('/').child(str(user)).child('ToTalCaloBreakFast').set(int(TocalCalo))


class MealSelectWindowForLunch:
    def __init__(self):
        global window,ui_1, CheckboxMealLunch, ListMeal,CaloLunch,TocalCalo
        window = QtWidgets.QMainWindow()
        ui_1 = MealSelectLunch.Ui_MainWindow()
        ui_1.setupUi(window)
        window.show()
        TocalCaloLunch = db.reference(str(user)).child('ToTalCaloLunch').get()
        #Display Calo For Lunch
        ui_1.label_12.setText(str(TocalCaloLunch))
        TocalCalo = TocalCaloLunch
        # display meal to listview
        ui_1.listWidget_4.clear()
        ui_1.listWidget_4.addItems(ListMealLunch)

        # Display checkbox
        ui_1.gaxaot_2.setChecked(CheckboxMealLunch[0])
        ui_1.gakho_2.setChecked(CheckboxMealLunch[1])
        ui_1.mucxao_2.setChecked(CheckboxMealLunch[2])
        ui_1.suongnuong_2.setChecked(CheckboxMealLunch[3])
        ui_1.suongram_2.setChecked(CheckboxMealLunch[4])
        ui_1.thitheoquay_2.setChecked(CheckboxMealLunch[5])
        ui_1.thitboxao_2.setChecked(CheckboxMealLunch[6])
        ui_1.thitkhotieu_2.setChecked(CheckboxMealLunch[7])
        ui_1.camoikho_2.setChecked(CheckboxMealLunch[8])
        ui_1.cari_2.setChecked(CheckboxMealLunch[9])
        ui_1.bobia_2.setChecked(CheckboxMealLunch[10])
        ui_1.cabacmachien_2.setChecked(CheckboxMealLunch[11])
        ui_1.cabacmakho_2.setChecked(CheckboxMealLunch[12])
        ui_1.cangukho_2.setChecked(CheckboxMealLunch[13])
        ui_1.chalua_2.setChecked(CheckboxMealLunch[14])
        ui_1.ganheoxao_2.setChecked(CheckboxMealLunch[15])
        ui_1.goikhobo_2.setChecked(CheckboxMealLunch[16])
        ui_1.goitom_2.setChecked(CheckboxMealLunch[17])
        ui_1.khoquaxaotrung_2.setChecked(CheckboxMealLunch[18])
        ui_1.lapxuongchien_2.setChecked(CheckboxMealLunch[19])
        ui_1.mucxaothapcam_2.setChecked(CheckboxMealLunch[20])
        ui_1.boxaomang_2.setChecked(CheckboxMealLunch[21])
        ui_1.boxaonam_2.setChecked(CheckboxMealLunch[22])
        ui_1.thitkhotrung_2.setChecked(CheckboxMealLunch[23])
        ui_1.bunrieu_2.setChecked(CheckboxMealLunch[24])
        ui_1.bunbohue_2.setChecked(CheckboxMealLunch[25])
        ui_1.bunthitnuong_2.setChecked(CheckboxMealLunch[26])
        ui_1.bunxao_2.setChecked(CheckboxMealLunch[27])
        ui_1.canhkhoqua_2.setChecked(CheckboxMealLunch[28])
        ui_1.chaolong_2.setChecked(CheckboxMealLunch[29])
        ui_1.bo_2.setChecked(CheckboxMealLunch[31])
        ui_1.chuoi_2.setChecked(CheckboxMealLunch[32])
        ui_1.thom_2.setChecked(CheckboxMealLunch[33])
        ui_1.xoai_2.setChecked(CheckboxMealLunch[34])
        ui_1.saurieng_2.setChecked(CheckboxMealLunch[35])
        ui_1.mangcut_2.setChecked(CheckboxMealLunch[36])
        ui_1.coc_2.setChecked(CheckboxMealLunch[37])
        ui_1.nho_2.setChecked(CheckboxMealLunch[38])
        ui_1.duahau_2.setChecked(CheckboxMealLunch[39])
        ui_1.buoi_2.setChecked(CheckboxMealLunch[40])
        ui_1.khoailang_2.setChecked(CheckboxMealLunch[41])
        ui_1.le_2.setChecked(CheckboxMealLunch[42])
        ui_1.bapluoc_2.setChecked(CheckboxMealLunch[43])
        ui_1.khoaitay_2.setChecked(CheckboxMealLunch[44])
        ui_1.dauphong_2.setChecked(CheckboxMealLunch[45])
        ui_1.dudu_2.setChecked(CheckboxMealLunch[46])
        ui_1.sori_2.setChecked(CheckboxMealLunch[47])
        ui_1.cam_2.setChecked(CheckboxMealLunch[48])
        ui_1.oi_2.setChecked(CheckboxMealLunch[49])
        ui_1.thanhlong_2.setChecked(CheckboxMealLunch[50])
        ui_1.chebap_2.setChecked(CheckboxMealLunch[51])
        ui_1.chechuoi_2.setChecked(CheckboxMealLunch[52])
        ui_1.chedauden_2.setChecked(CheckboxMealLunch[53])
        ui_1.chedauxanh_2.setChecked(CheckboxMealLunch[54])
        ui_1.chenep_2.setChecked(CheckboxMealLunch[55])
        ui_1.chetroinuoc_2.setChecked(CheckboxMealLunch[56])
        ui_1.xoibap_2.setChecked(CheckboxMealLunch[57])
        ui_1.xoidauden_2.setChecked(CheckboxMealLunch[58])
        ui_1.xoidauphong_2.setChecked(CheckboxMealLunch[59])
        ui_1.xoigac_2.setChecked(CheckboxMealLunch[60])
        ui_1.cafe_2.setChecked(CheckboxMealLunch[61])
        ui_1.nuocam_2.setChecked(CheckboxMealLunch[62])
        ui_1.nuocchanh_2.setChecked(CheckboxMealLunch[63])
        ui_1.nuocmia_2.setChecked(CheckboxMealLunch[64])
        ui_1.nuocrauma_2.setChecked(CheckboxMealLunch[65])
        ui_1.suachua_2.setChecked(CheckboxMealLunch[66])
        ui_1.trungcut_2.setChecked(CheckboxMealLunch[67])
        ui_1.trungga_2.setChecked(CheckboxMealLunch[68])
        ui_1.trungvit_2.setChecked(CheckboxMealLunch[69])

        ui_1.Save.clicked.connect(SaveMealLunch)
        # ui_1.Save.setEnabled(False)

        # if checkbox change state will call function
        ui_1.gaxaot_2.stateChanged.connect(lambda:gaxaot(ListMealLunch,CheckboxMealLunch))
        ui_1.gakho_2.stateChanged.connect(lambda:gakho(ListMealLunch,CheckboxMealLunch))
        ui_1.mucxao_2.stateChanged.connect(lambda:mucxao(ListMealLunch,CheckboxMealLunch))
        ui_1.suongnuong_2.stateChanged.connect(lambda:suongnuong(ListMealLunch,CheckboxMealLunch))
        ui_1.suongram_2.stateChanged.connect(lambda:suongram(ListMealLunch,CheckboxMealLunch))
        ui_1.thitheoquay_2.stateChanged.connect(lambda:thitheoquay(ListMealLunch,CheckboxMealLunch))
        ui_1.thitboxao_2.stateChanged.connect(lambda:thitboxao(ListMealLunch,CheckboxMealLunch))
        ui_1.thitkhotieu_2.stateChanged.connect(lambda:thitkhotieu(ListMealLunch,CheckboxMealLunch))
        ui_1.camoikho_2.stateChanged.connect(lambda:camoikho(ListMealLunch,CheckboxMealLunch))
        ui_1.cari_2.stateChanged.connect(lambda:cari(ListMealLunch,CheckboxMealLunch))
        ui_1.bobia_2.stateChanged.connect(lambda:bobia(ListMealLunch,CheckboxMealLunch))
        ui_1.cabacmachien_2.stateChanged.connect(lambda:cabacmachien(ListMealLunch,CheckboxMealLunch))
        ui_1.cabacmakho_2.stateChanged.connect(lambda:cabacmakho(ListMealLunch,CheckboxMealLunch))
        ui_1.cangukho_2.stateChanged.connect(lambda:cangukho(ListMealLunch,CheckboxMealLunch))
        ui_1.chalua_2.stateChanged.connect(lambda:chalua(ListMealLunch,CheckboxMealLunch))
        ui_1.ganheoxao_2.stateChanged.connect(lambda:ganheoxao(ListMealLunch,CheckboxMealLunch))
        ui_1.goikhobo_2.stateChanged.connect(lambda:goikhobo(ListMealLunch,CheckboxMealLunch))
        ui_1.goitom_2.stateChanged.connect(lambda:goitom(ListMealLunch,CheckboxMealLunch))
        ui_1.khoquaxaotrung_2.stateChanged.connect(lambda:khoquaxaotrung(ListMealLunch,CheckboxMealLunch))
        ui_1.lapxuongchien_2.stateChanged.connect(lambda:lapxuongchien(ListMealLunch,CheckboxMealLunch))
        ui_1.mucxaothapcam_2.stateChanged.connect(lambda:mucxaothapcam(ListMealLunch,CheckboxMealLunch))
        ui_1.boxaomang_2.stateChanged.connect(lambda:boxaomang(ListMealLunch,CheckboxMealLunch))
        ui_1.boxaonam_2.stateChanged.connect(lambda:boxaonam(ListMealLunch,CheckboxMealLunch))
        ui_1.thitkhotrung_2.stateChanged.connect(lambda:thitkhotrung(ListMealLunch,CheckboxMealLunch))
        ui_1.bunrieu_2.stateChanged.connect(lambda:bunrieu(ListMealLunch,CheckboxMealLunch))
        ui_1.bunbohue_2.stateChanged.connect(lambda:bunbohue(ListMealLunch,CheckboxMealLunch))
        ui_1.bunthitnuong_2.stateChanged.connect(lambda:bunthitnuong(ListMealLunch,CheckboxMealLunch))
        ui_1.bunxao_2.stateChanged.connect(lambda:bunxao(ListMealLunch,CheckboxMealLunch))
        ui_1.canhkhoqua_2.stateChanged.connect(lambda:canhkhoqua(ListMealLunch,CheckboxMealLunch))
        ui_1.chaolong_2.stateChanged.connect(lambda:chaolong(ListMealLunch,CheckboxMealLunch))
        ui_1.bo_2.stateChanged.connect(lambda:bo(ListMealLunch,CheckboxMealLunch))
        ui_1.chuoi_2.stateChanged.connect(lambda:chuoi(ListMealLunch,CheckboxMealLunch))
        ui_1.thom_2.stateChanged.connect(lambda:thom(ListMealLunch,CheckboxMealLunch))
        ui_1.xoai_2.stateChanged.connect(lambda:xoai(ListMealLunch,CheckboxMealLunch))
        ui_1.saurieng_2.stateChanged.connect(lambda:saurieng(ListMealLunch,CheckboxMealLunch))
        ui_1.mangcut_2.stateChanged.connect(lambda:mangcut(ListMealLunch,CheckboxMealLunch))
        ui_1.coc_2.stateChanged.connect(lambda:coc(ListMealLunch,CheckboxMealLunch))
        ui_1.nho_2.stateChanged.connect(lambda:nho(ListMealLunch,CheckboxMealLunch))
        ui_1.duahau_2.stateChanged.connect(lambda:duahau(ListMealLunch,CheckboxMealLunch))
        ui_1.buoi_2.stateChanged.connect(lambda:buoi(ListMealLunch,CheckboxMealLunch))
        ui_1.khoailang_2.stateChanged.connect(lambda:khoailang(ListMealLunch,CheckboxMealLunch))
        ui_1.le_2.stateChanged.connect(lambda:le(ListMealLunch,CheckboxMealLunch))
        ui_1.bapluoc_2.stateChanged.connect(lambda:bapluoc(ListMealLunch,CheckboxMealLunch))
        ui_1.khoaitay_2.stateChanged.connect(lambda:khoaitay(ListMealLunch,CheckboxMealLunch))
        ui_1.dauphong_2.stateChanged.connect(lambda:dauphong(ListMealLunch,CheckboxMealLunch))
        ui_1.dudu_2.stateChanged.connect(lambda:dudu(ListMealLunch,CheckboxMealLunch))
        ui_1.sori_2.stateChanged.connect(lambda:sori(ListMealLunch,CheckboxMealLunch))
        ui_1.cam_2.stateChanged.connect(lambda:cam(ListMealLunch,CheckboxMealLunch))
        ui_1.oi_2.stateChanged.connect(lambda:oi(ListMealLunch,CheckboxMealLunch))
        ui_1.thanhlong_2.stateChanged.connect(lambda:thanhlong(ListMealLunch,CheckboxMealLunch))
        ui_1.chebap_2.stateChanged.connect(lambda:chebap(ListMealLunch,CheckboxMealLunch))
        ui_1.chechuoi_2.stateChanged.connect(lambda:chechuoi(ListMealLunch,CheckboxMealLunch))
        ui_1.chedauden_2.stateChanged.connect(lambda:chedauden(ListMealLunch,CheckboxMealLunch))
        ui_1.chedauxanh_2.stateChanged.connect(lambda:chedauxanh(ListMealLunch,CheckboxMealLunch))
        ui_1.chenep_2.stateChanged.connect(lambda:chenep(ListMealLunch,CheckboxMealLunch))
        ui_1.chetroinuoc_2.stateChanged.connect(lambda:chetroinuoc(ListMealLunch,CheckboxMealLunch))
        ui_1.xoibap_2.stateChanged.connect(lambda:xoibap(ListMealLunch,CheckboxMealLunch))
        ui_1.xoidauden_2.stateChanged.connect(lambda:xoidauden(ListMealLunch,CheckboxMealLunch))
        ui_1.xoidauphong_2.stateChanged.connect(lambda:xoidauphong(ListMealLunch,CheckboxMealLunch))
        ui_1.xoigac_2.stateChanged.connect(lambda:xoigac(ListMealLunch,CheckboxMealLunch))
        ui_1.cafe_2.stateChanged.connect(lambda:cafe(ListMealLunch,CheckboxMealLunch))
        ui_1.nuocam_2.stateChanged.connect(lambda:nuocam(ListMealLunch,CheckboxMealLunch))
        ui_1.nuocchanh_2.stateChanged.connect(lambda:nuocchanh(ListMealLunch,CheckboxMealLunch))
        ui_1.nuocmia_2.stateChanged.connect(lambda:nuocmia(ListMealLunch,CheckboxMealLunch))
        ui_1.nuocrauma_2.stateChanged.connect(lambda:nuocrauma(ListMealLunch,CheckboxMealLunch))
        ui_1.suachua_2.stateChanged.connect(lambda:suachua(ListMealLunch,CheckboxMealLunch))
        ui_1.trungcut_2.stateChanged.connect(lambda:trungcut(ListMealLunch,CheckboxMealLunch))
        ui_1.trungga_2.stateChanged.connect(lambda:trungga(ListMealLunch,CheckboxMealLunch))
        ui_1.trungvit_2.stateChanged.connect(lambda:trungvit(ListMealLunch,CheckboxMealLunch))

def SaveMealLunch():
        global FOOD, FRUIT, OTHER, ListMeal, CheckboxMeal,CaloLunch,TocalCaloLunch
        ListMealDB = open(
            r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal_Lunch.txt",
            "w")
        CheckboxDB = open(
            r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox_Lunch.txt",
            "w")
        CaloLunch = ui_1.label_12.text()
        #ListView
        for d in range(len(ListMealLunch)):
            ListMealDB.writelines(ListMealLunch[d] + '\n')
        # Checkbox
        for e in range(len(CheckboxMeal)):
            CheckboxDB.writelines(str(CheckboxMealLunch[e]) + '\n')
        db.reference('/').child(str(user)).child('ToTalCaloLunch').set(TocalCalo)

class MealSelectWindowForDinner:
    def __init__(self):
        global window,ui_1, CheckboxMealDinner, ListMealDinner,CaloDinner,TocalCaloDinner,TocalCalo
        window = QtWidgets.QMainWindow()
        ui_1 = MealSelectDinner.Ui_MainWindow()
        ui_1.setupUi(window)
        window.show()

        TocalCaloDinner = db.reference(str(user)).child('ToTalCaloDinner').get()
        #Display Calo For breakfase
        ui_1.label_12.setText(str(TocalCaloDinner))
        TocalCalo = TocalCaloDinner
        # display meal to listview
        ui_1.listWidget_4.clear()
        ui_1.listWidget_4.addItems(ListMealDinner)

        # Display checkbox
        ui_1.gaxaot_2.setChecked(CheckboxMealDinner[0])
        ui_1.gakho_2.setChecked(CheckboxMealDinner[1])
        ui_1.mucxao_2.setChecked(CheckboxMealDinner[2])
        ui_1.suongnuong_2.setChecked(CheckboxMealDinner[3])
        ui_1.suongram_2.setChecked(CheckboxMealDinner[4])
        ui_1.thitheoquay_2.setChecked(CheckboxMealDinner[5])
        ui_1.thitboxao_2.setChecked(CheckboxMealDinner[6])
        ui_1.thitkhotieu_2.setChecked(CheckboxMealDinner[7])
        ui_1.camoikho_2.setChecked(CheckboxMealDinner[8])
        ui_1.cari_2.setChecked(CheckboxMealDinner[9])
        ui_1.bobia_2.setChecked(CheckboxMealDinner[10])
        ui_1.cabacmachien_2.setChecked(CheckboxMealDinner[11])
        ui_1.cabacmakho_2.setChecked(CheckboxMealDinner[12])
        ui_1.cangukho_2.setChecked(CheckboxMealDinner[13])
        ui_1.chalua_2.setChecked(CheckboxMealDinner[14])
        ui_1.ganheoxao_2.setChecked(CheckboxMealDinner[15])
        ui_1.goikhobo_2.setChecked(CheckboxMealDinner[16])
        ui_1.goitom_2.setChecked(CheckboxMealDinner[17])
        ui_1.khoquaxaotrung_2.setChecked(CheckboxMealDinner[18])
        ui_1.lapxuongchien_2.setChecked(CheckboxMealDinner[19])
        ui_1.mucxaothapcam_2.setChecked(CheckboxMealDinner[20])
        ui_1.boxaomang_2.setChecked(CheckboxMealDinner[21])
        ui_1.boxaonam_2.setChecked(CheckboxMealDinner[22])
        ui_1.thitkhotrung_2.setChecked(CheckboxMealDinner[23])
        ui_1.bunrieu_2.setChecked(CheckboxMealDinner[24])
        ui_1.bunbohue_2.setChecked(CheckboxMealDinner[25])
        ui_1.bunthitnuong_2.setChecked(CheckboxMealDinner[26])
        ui_1.bunxao_2.setChecked(CheckboxMealDinner[27])
        ui_1.canhkhoqua_2.setChecked(CheckboxMealDinner[28])
        ui_1.chaolong_2.setChecked(CheckboxMealDinner[29])
        ui_1.bo_2.setChecked(CheckboxMealDinner[31])
        ui_1.chuoi_2.setChecked(CheckboxMealDinner[32])
        ui_1.thom_2.setChecked(CheckboxMealDinner[33])
        ui_1.xoai_2.setChecked(CheckboxMealDinner[34])
        ui_1.saurieng_2.setChecked(CheckboxMealDinner[35])
        ui_1.mangcut_2.setChecked(CheckboxMealDinner[36])
        ui_1.coc_2.setChecked(CheckboxMealDinner[37])
        ui_1.nho_2.setChecked(CheckboxMealDinner[38])
        ui_1.duahau_2.setChecked(CheckboxMealDinner[39])
        ui_1.buoi_2.setChecked(CheckboxMealDinner[40])
        ui_1.khoailang_2.setChecked(CheckboxMealDinner[41])
        ui_1.le_2.setChecked(CheckboxMealDinner[42])
        ui_1.bapluoc_2.setChecked(CheckboxMealDinner[43])
        ui_1.khoaitay_2.setChecked(CheckboxMealDinner[44])
        ui_1.dauphong_2.setChecked(CheckboxMealDinner[45])
        ui_1.dudu_2.setChecked(CheckboxMealDinner[46])
        ui_1.sori_2.setChecked(CheckboxMealDinner[47])
        ui_1.cam_2.setChecked(CheckboxMealDinner[48])
        ui_1.oi_2.setChecked(CheckboxMealDinner[49])
        ui_1.thanhlong_2.setChecked(CheckboxMealDinner[50])
        ui_1.chebap_2.setChecked(CheckboxMealDinner[51])
        ui_1.chechuoi_2.setChecked(CheckboxMealDinner[52])
        ui_1.chedauden_2.setChecked(CheckboxMealDinner[53])
        ui_1.chedauxanh_2.setChecked(CheckboxMealDinner[54])
        ui_1.chenep_2.setChecked(CheckboxMealDinner[55])
        ui_1.chetroinuoc_2.setChecked(CheckboxMealDinner[56])
        ui_1.xoibap_2.setChecked(CheckboxMealDinner[57])
        ui_1.xoidauden_2.setChecked(CheckboxMealDinner[58])
        ui_1.xoidauphong_2.setChecked(CheckboxMealDinner[59])
        ui_1.xoigac_2.setChecked(CheckboxMealDinner[60])
        ui_1.cafe_2.setChecked(CheckboxMealDinner[61])
        ui_1.nuocam_2.setChecked(CheckboxMealDinner[62])
        ui_1.nuocchanh_2.setChecked(CheckboxMealDinner[63])
        ui_1.nuocmia_2.setChecked(CheckboxMealDinner[64])
        ui_1.nuocrauma_2.setChecked(CheckboxMealDinner[65])
        ui_1.suachua_2.setChecked(CheckboxMealDinner[66])
        ui_1.trungcut_2.setChecked(CheckboxMealDinner[67])
        ui_1.trungga_2.setChecked(CheckboxMealDinner[68])
        ui_1.trungvit_2.setChecked(CheckboxMealDinner[69])

        ui_1.Save.clicked.connect(SaveMealDinner)
        # ui_1.Save.setEnabled(False)

        # if checkbox change state will call function
        ui_1.gaxaot_2.stateChanged.connect(lambda:gaxaot(ListMealDinner,CheckboxMealDinner))
        ui_1.gakho_2.stateChanged.connect(lambda:gakho(ListMealDinner,CheckboxMealDinner))
        ui_1.mucxao_2.stateChanged.connect(lambda:mucxao(ListMealDinner,CheckboxMealDinner))
        ui_1.suongnuong_2.stateChanged.connect(lambda:suongnuong(ListMealDinner,CheckboxMealDinner))
        ui_1.suongram_2.stateChanged.connect(lambda:suongram(ListMealDinner,CheckboxMealDinner))
        ui_1.thitheoquay_2.stateChanged.connect(lambda:thitheoquay(ListMealDinner,CheckboxMealDinner))
        ui_1.thitboxao_2.stateChanged.connect(lambda:thitboxao(ListMealDinner,CheckboxMealDinner))
        ui_1.thitkhotieu_2.stateChanged.connect(lambda:thitkhotieu(ListMealDinner,CheckboxMealDinner))
        ui_1.camoikho_2.stateChanged.connect(lambda:camoikho(ListMealDinner,CheckboxMealDinner))
        ui_1.cari_2.stateChanged.connect(lambda:cari(ListMealDinner,CheckboxMealDinner))
        ui_1.bobia_2.stateChanged.connect(lambda:bobia(ListMealDinner,CheckboxMealDinner))
        ui_1.cabacmachien_2.stateChanged.connect(lambda:cabacmachien(ListMealDinner,CheckboxMealDinner))
        ui_1.cabacmakho_2.stateChanged.connect(lambda:cabacmakho(ListMealDinner,CheckboxMealDinner))
        ui_1.cangukho_2.stateChanged.connect(lambda:cangukho(ListMealDinner,CheckboxMealDinner))
        ui_1.chalua_2.stateChanged.connect(lambda:chalua(ListMealDinner,CheckboxMealDinner))
        ui_1.ganheoxao_2.stateChanged.connect(lambda:ganheoxao(ListMealDinner,CheckboxMealDinner))
        ui_1.goikhobo_2.stateChanged.connect(lambda:goikhobo(ListMealDinner,CheckboxMealDinner))
        ui_1.goitom_2.stateChanged.connect(lambda:goitom(ListMealDinner,CheckboxMealDinner))
        ui_1.khoquaxaotrung_2.stateChanged.connect(lambda:khoquaxaotrung(ListMealDinner,CheckboxMealDinner))
        ui_1.lapxuongchien_2.stateChanged.connect(lambda:lapxuongchien(ListMealDinner,CheckboxMealDinner))
        ui_1.mucxaothapcam_2.stateChanged.connect(lambda:mucxaothapcam(ListMealDinner,CheckboxMealDinner))
        ui_1.boxaomang_2.stateChanged.connect(lambda:boxaomang(ListMealDinner,CheckboxMealDinner))
        ui_1.boxaonam_2.stateChanged.connect(lambda:boxaonam(ListMealDinner,CheckboxMealDinner))
        ui_1.thitkhotrung_2.stateChanged.connect(lambda:thitkhotrung(ListMealDinner,CheckboxMealDinner))
        ui_1.bunrieu_2.stateChanged.connect(lambda:bunrieu(ListMealDinner,CheckboxMealDinner))
        ui_1.bunbohue_2.stateChanged.connect(lambda:bunbohue(ListMealDinner,CheckboxMealDinner))
        ui_1.bunthitnuong_2.stateChanged.connect(lambda:bunthitnuong(ListMealDinner,CheckboxMealDinner))
        ui_1.bunxao_2.stateChanged.connect(lambda:bunxao(ListMealDinner,CheckboxMealDinner))
        ui_1.canhkhoqua_2.stateChanged.connect(lambda:canhkhoqua(ListMealDinner,CheckboxMealDinner))
        ui_1.chaolong_2.stateChanged.connect(lambda:chaolong(ListMealDinner,CheckboxMealDinner))
        ui_1.bo_2.stateChanged.connect(lambda:bo(ListMealDinner,CheckboxMealDinner))
        ui_1.chuoi_2.stateChanged.connect(lambda:chuoi(ListMealDinner,CheckboxMealDinner))
        ui_1.thom_2.stateChanged.connect(lambda:thom(ListMealDinner,CheckboxMealDinner))
        ui_1.xoai_2.stateChanged.connect(lambda:xoai(ListMealDinner,CheckboxMealDinner))
        ui_1.saurieng_2.stateChanged.connect(lambda:saurieng(ListMealDinner,CheckboxMealDinner))
        ui_1.mangcut_2.stateChanged.connect(lambda:mangcut(ListMealDinner,CheckboxMealDinner))
        ui_1.coc_2.stateChanged.connect(lambda:coc(ListMealDinner,CheckboxMealDinner))
        ui_1.nho_2.stateChanged.connect(lambda:nho(ListMealDinner,CheckboxMealDinner))
        ui_1.duahau_2.stateChanged.connect(lambda:duahau(ListMealDinner,CheckboxMealDinner))
        ui_1.buoi_2.stateChanged.connect(lambda:buoi(ListMealDinner,CheckboxMealDinner))
        ui_1.khoailang_2.stateChanged.connect(lambda:khoailang(ListMealDinner,CheckboxMealDinner))
        ui_1.le_2.stateChanged.connect(lambda:le(ListMealDinner,CheckboxMealDinner))
        ui_1.bapluoc_2.stateChanged.connect(lambda:bapluoc(ListMealDinner,CheckboxMealDinner))
        ui_1.khoaitay_2.stateChanged.connect(lambda:khoaitay(ListMealDinner,CheckboxMealDinner))
        ui_1.dauphong_2.stateChanged.connect(lambda:dauphong(ListMealDinner,CheckboxMealDinner))
        ui_1.dudu_2.stateChanged.connect(lambda:dudu(ListMealDinner,CheckboxMealDinner))
        ui_1.sori_2.stateChanged.connect(lambda:sori(ListMealDinner,CheckboxMealDinner))
        ui_1.cam_2.stateChanged.connect(lambda:cam(ListMealDinner,CheckboxMealDinner))
        ui_1.oi_2.stateChanged.connect(lambda:oi(ListMealDinner,CheckboxMealDinner))
        ui_1.thanhlong_2.stateChanged.connect(lambda:thanhlong(ListMealDinner,CheckboxMealDinner))
        ui_1.chebap_2.stateChanged.connect(lambda:chebap(ListMealDinner,CheckboxMealDinner))
        ui_1.chechuoi_2.stateChanged.connect(lambda:chechuoi(ListMealDinner,CheckboxMealDinner))
        ui_1.chedauden_2.stateChanged.connect(lambda:chedauden(ListMealDinner,CheckboxMealDinner))
        ui_1.chedauxanh_2.stateChanged.connect(lambda:chedauxanh(ListMealDinner,CheckboxMealDinner))
        ui_1.chenep_2.stateChanged.connect(lambda:chenep(ListMealDinner,CheckboxMealDinner))
        ui_1.chetroinuoc_2.stateChanged.connect(lambda:chetroinuoc(ListMealDinner,CheckboxMealDinner))
        ui_1.xoibap_2.stateChanged.connect(lambda:xoibap(ListMealDinner,CheckboxMealDinner))
        ui_1.xoidauden_2.stateChanged.connect(lambda:xoidauden(ListMealDinner,CheckboxMealDinner))
        ui_1.xoidauphong_2.stateChanged.connect(lambda:xoidauphong(ListMealDinner,CheckboxMealDinner))
        ui_1.xoigac_2.stateChanged.connect(lambda:xoigac(ListMealDinner,CheckboxMealDinner))
        ui_1.cafe_2.stateChanged.connect(lambda:cafe(ListMealDinner,CheckboxMealDinner))
        ui_1.nuocam_2.stateChanged.connect(lambda:nuocam(ListMealDinner,CheckboxMealDinner))
        ui_1.nuocchanh_2.stateChanged.connect(lambda:nuocchanh(ListMealDinner,CheckboxMealDinner))
        ui_1.nuocmia_2.stateChanged.connect(lambda:nuocmia(ListMealDinner,CheckboxMealDinner))
        ui_1.nuocrauma_2.stateChanged.connect(lambda:nuocrauma(ListMealDinner,CheckboxMealDinner))
        ui_1.suachua_2.stateChanged.connect(lambda:suachua(ListMealDinner,CheckboxMealDinner))
        ui_1.trungcut_2.stateChanged.connect(lambda:trungcut(ListMealDinner,CheckboxMealDinner))
        ui_1.trungga_2.stateChanged.connect(lambda:trungga(ListMealDinner,CheckboxMealDinner))
        ui_1.trungvit_2.stateChanged.connect(lambda:trungvit(ListMealDinner,CheckboxMealDinner))

def SaveMealDinner():
    global ListMeal, CheckboxMeal,CaloDinner
    ListMealDB = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\ListMeal_Dinner.txt",
        "w")
    CheckboxDB = open(
        r"C:\Users\TEMP\Downloads\DATN\pyqt5-full-app-tutorial-for-beginners-main\database\Checkbox_Dinner.txt",
        "w")
    CaloDinner = str(ui_1.label_12.text())
    for d in range(len(ListMealDinner)):
        ListMealDB.writelines(ListMealDinner[d] + '\n')
        #     # Checkbix
    for e in range(len(CheckboxMeal)):
        CheckboxDB.writelines(str(CheckboxMealDinner[e]) + '\n')
    db.reference('/').child(str(user)).child('ToTalCaloDinner').set(TocalCalo)

def gaxaot(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,ListMeal,ListMealDinner,checkboxDinner,ListMealLunch,checkboxLunch
    if ui_1.gaxaot_2.isChecked() == True:
        TocalCalo += 270
        # FOOD.append('gaxaot')
        ListOfMeal.append('gaxaot')
        CheckBoxForMeal[0] = True
    else:
        TocalCalo -= 270
        # FOOD.remove('gaxaot')
        ListOfMeal.remove('gaxaot')
        CheckBoxForMeal[0] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)

def gakho(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD,Index
    if ui_1.gakho_2.isChecked() == True:
        TocalCalo += 300
        # FOOD.append('gakho')
        ListOfMeal.append('gakho')
        CheckBoxForMeal[1] = True
    else:
        TocalCalo -= 300
        # FOOD.remove('gakho')
        ListOfMeal.remove('gakho')
        CheckBoxForMeal[1] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def mucxao(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.mucxao_2.isChecked() == True:
        TocalCalo += 180
        # FOOD.append('mucxao')
        ListOfMeal.append('mucxao')
        CheckBoxForMeal[2] = True
    else:
        TocalCalo -= 180
        # FOOD.remove('mucxao')
        ListMeal.remove('mucxao')
        CheckBoxForMeal[2] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def suongnuong(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.suongnuong_2.isChecked() == True:
        TocalCalo += 110
        # FOOD.append('suongnuong')
        ListOfMeal.append('suongnuong')
        CheckBoxForMeal[3] = True
    else:
        TocalCalo -= 110
        FOOD.remove('suongnuong')
        # ListMeal.remove('suongnuong')
        CheckBoxForMeal[3] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def suongram(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.suongram_2.isChecked() == True:
        TocalCalo += 150
        # FOOD.append('suongram')
        ListOfMeal.append('suongram')
        CheckBoxForMeal[4] = True
    else:
        TocalCalo -= 150
        # FOOD.remove('suongram')
        ListMeal.remove('suongram')
        CheckBoxForMeal[4] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def thitheoquay(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.thitheoquay_2.isChecked() == True:
        TocalCalo += 145
        # FOOD.append('thitheoquay')
        ListOfMeal.append('thitheoquay')
        CheckBoxForMeal[5] = True
    else:
        TocalCalo -= 145
        # FOOD.remove('thitheoquay')
        ListOfMeal.remove('thitheoquay')
        CheckBoxForMeal[5] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def thitboxao(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.thitboxao_2.isChecked() == True:
        TocalCalo += 200
        # FOOD.append('thitboxao')
        ListOfMeal.append('thitboxao')
        CheckBoxForMeal[6] = True
    else:
        TocalCalo -= 200
        # FOOD.remove('thitboxao')
        ListOfMeal.remove('thitboxao')
        CheckBoxForMeal[6] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def thitkhotieu(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.thitkhotieu_2.isChecked() == True:
        TocalCalo += 200
        # FOOD.append('thitkhotieu')
        ListOfMeal.append('thitkhotieu')
        CheckBoxForMeal[7] = True
    else:
        TocalCalo -= 200
        # FOOD.remove('thitkhotieu')
        ListOfMeal.remove('thitkhotieu')
        CheckBoxForMeal[7] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def camoikho(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.camoikho_2.isChecked() == True:
        TocalCalo += 105
        # FOOD.append('camoikho')
        ListOfMeal.append('camoikho')
        CheckBoxForMeal[8] = True
    else:
        TocalCalo -= 105
        # FOOD.remove('camoikho')
        ListOfMeal.remove('camoikho')
        CheckBoxForMeal[8] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def cari(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.cari_2.isChecked() == True:
        TocalCalo += 278
        # FOOD.append('cari')
        ListOfMeal.append('cari')
        CheckBoxForMeal[9] = True
    else:
        TocalCalo -= 278
        # FOOD.remove('cari')
        ListOfMeal.remove('cari')
        CheckBoxForMeal[9] = True
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def bobia(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.bobia_2.isChecked() == True:
        TocalCalo += 100
        # FOOD.append('bobia')
        ListOfMeal.append('bobia')
        CheckBoxForMeal[10] = True
    else:
        TocalCalo -= 100
        # FOOD.remove('bobia')
        ListOfMeal.remove('bobia')
        CheckBoxForMeal[10] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def cabacmachien(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.cabacmachien_2.isChecked() == True:
        TocalCalo += 135
        # FOOD.append('cabacmachien')
        ListOfMeal.append('cabacmachien')
        CheckBoxForMeal[11] = True
    else:
        TocalCalo -= 135
        # FOOD.remove('cabacmachien')
        ListOfMeal.remove('cabacmachien')
        CheckBoxForMeal[11] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def cabacmakho(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.cabacmakho_2.isChecked() == True:
        TocalCalo += 167
        # FOOD.append('cabacmakho')
        ListOfMeal.append('cabacmakho')
        CheckBoxForMeal[12] = True
    else:
        TocalCalo -= 167
        # FOOD.remove('cabacmakho')
        ListOfMeal.remove('cabacmakho')
        CheckBoxForMeal[12] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def cangukho(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.cangukho_2.isChecked() == True:
        TocalCalo += 122
        # FOOD.append('cangukho')
        ListOfMeal.append('cangukho')
        CheckBoxForMeal[13] = True
    else:
        TocalCalo -= 122
        # FOOD.remove('cangukho')
        ListOfMeal.remove('cangukho')
        CheckBoxForMeal[13] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def chalua(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.chalua_2.isChecked() == True:
        TocalCalo += 100
        # FOOD.append('chalua')
        ListOfMeal.append('chalua')
        CheckBoxForMeal[14] = True
    else:
        TocalCalo -= 100
        # FOOD.remove('chalua')
        ListOfMeal.remove('chalua')
        CheckBoxForMeal[14] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def ganheoxao(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.ganheoxao_2.isChecked() == True:
        TocalCalo += 200
        # FOOD.append('ganheoxao')
        ListOfMeal.append('ganheoxao')
        CheckBoxForMeal[15] = True
    else:
        TocalCalo -= 200
        # FOOD.remove('ganheoxao')
        ListOfMeal.remove('ganheoxao')
        CheckBoxForMeal[15] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def goikhobo(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.goikhobo_2.isChecked() == True:
        TocalCalo += 268
        # FOOD.append('goikhobo')
        ListOfMeal.append('goikhobo')
        CheckBoxForMeal[16] = True
    else:
        TocalCalo -= 268
        # FOOD.remove('goikhobo')
        ListOfMeal.remove('goikhobo')
        CheckBoxForMeal[16] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def goitom(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.goitom_2.isChecked() == True:
        TocalCalo += 147
        # FOOD.append('goitom')
        ListOfMeal.append('goitom')
        CheckBoxForMeal[17] = True
    else:
        TocalCalo -= 147
        # FOOD.remove('goitom')
        ListOfMeal.remove('goitom')
        CheckBoxForMeal[17] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def khoquaxaotrung(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.khoquaxaotrung_2.isChecked() == True:
        TocalCalo += 115
        # FOOD.append('khoquaxaotrung')
        ListOfMeal.append('khoquaxaotrung')
        CheckBoxForMeal[18] = True
    else:
        TocalCalo -= 115
        # FOOD.remove('khoquaxaotrung')
        ListOfMeal.remove('khoquaxaotrung')
        CheckBoxForMeal[18] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def lapxuongchien(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.lapxuongchien_2.isChecked() == True:
        TocalCalo += 300
        # FOOD.append('lapxuongchien')
        ListOfMeal.append('lapxuongchien')
        CheckBoxForMeal[19] = True
    else:
        TocalCalo -= 300
        # FOOD.remove('lapxuongchien')
        ListOfMeal.remove('lapxuongchien')
        CheckBoxForMeal[19] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def mucxaothapcam(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.mucxaothapcam_2.isChecked() == True:
        TocalCalo += 135
        # FOOD.append('mucxaothapcam')
        ListOfMeal.append('mucxaothapcam')
        CheckBoxForMeal[20] = True
    else:
        TocalCalo -= 135
        # FOOD.remove('mucxaothapcam')
        ListOfMeal.remove('mucxaothapcam')
        CheckBoxForMeal[20] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def boxaomang(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.boxaomang_2.isChecked() == True:
        TocalCalo += 105
        # FOOD.append('boxaomang')
        ListOfMeal.append('boxaomang')
        CheckBoxForMeal[21] = True
    else:
        TocalCalo -= 105
        # FOOD.remove('boxaomang')
        ListOfMeal.remove('boxaomang')
        CheckBoxForMeal[21] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def boxaonam(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.boxaonam_2.isChecked() == True:
        TocalCalo += 150
        # FOOD.append('boxaonam')
        ListOfMeal.append('boxaonam')
        CheckBoxForMeal[22] = True
    else:
        TocalCalo -= 150
        # FOOD.remove('boxaonam')
        ListOfMeal.remove('boxaonam')
        CheckBoxForMeal[22] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def thitkhotrung(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.thitkhotrung_2.isChecked() == True:
        TocalCalo += 315
        # FOOD.append('thitkhotrung')
        ListOfMeal.append('thitkhotrung')
        CheckBoxForMeal[23] = True
    else:
        TocalCalo -= 315
        # FOOD.remove('thitkhotrung')
        ListOfMeal.remove('thitkhotrung')
        CheckBoxForMeal[23] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def bunrieu(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.bunrieu_2.isChecked() == True:
        TocalCalo += 482
        # FOOD.append('bunrieu')
        ListOfMeal.append('bunrieu')
        CheckBoxForMeal[24] = True
    else:
        TocalCalo -= 482
        # FOOD.remove('bunrieu')
        ListOfMeal.remove('bunrieu')
        CheckBoxForMeal[24] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def bunbohue(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.bunbohue_2.isChecked() == True:
        TocalCalo += 479
        # FOOD.append('bunbohue')
        ListOfMeal.append('bunbohue')
        CheckBoxForMeal[25] = True
    else:
        TocalCalo -= 479
        # FOOD.remove('bunbohue')
        ListOfMeal.remove('bunbohue')
        CheckBoxForMeal[25] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def bunthitnuong(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.bunthitnuong_2.isChecked() == True:
        TocalCalo += 451
        # FOOD.append('bunthitnuong')
        ListOfMeal.append('bunthitnuong')
        CheckBoxForMeal[26] = True
    else:
        TocalCalo -= 451
        # FOOD.remove('bunthitnuong')
        ListOfMeal.remove('bunthitnuong')
        CheckBoxForMeal[26] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def bunxao(ListOfMeal,CheckBoxForMeal):
    global TocalCalo
    if ui_1.bunxao_2.isChecked() == True:
        TocalCalo += 570
        # FOOD.append('bunxao')
        ListOfMeal.append('bunxao')
        CheckBoxForMeal[27] = True
    else:
        TocalCalo -= 570
        # FOOD.remove('bunxao')
        ListOfMeal.remove('bunxao')
        CheckBoxForMeal[27] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def canhkhoqua(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.canhkhoqua_2.isChecked() == True:
        TocalCalo += 88
        # FOOD.append('canhkhoqua')
        ListOfMeal.append('canhkhoqua')
        CheckBoxForMeal[28] = True
    else:
        TocalCalo -= 479
        # FOOD.remove('canhkhoqua')
        ListOfMeal.remove('canhkhoqua')
        CheckBoxForMeal[28] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def chaolong(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FOOD
    if ui_1.chaolong_2.isChecked() == True:
        TocalCalo += 412
        # FOOD.append('chaolong')
        ListOfMeal.append('chaolong')
        CheckBoxForMeal[29] = True
    else:
        TocalCalo -= 412
        # FOOD.remove('chaolong')
        ListOfMeal.remove('chaolong')
        CheckBoxForMeal[29] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)

    ############################### Fruist######################
def bo(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.bo_2.isChecked() == True:
        TocalCalo += 184
        # FRUIT.append('bo')
        ListOfMeal.append('bo')
        CheckBoxForMeal[31] = True
    else:
        TocalCalo -= 184
        # FRUIT.remove('bo')
        ListOfMeal.remove('bo')
        CheckBoxForMeal[31] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def chuoi(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.chuoi_2.isChecked() == True:
        TocalCalo += 35
        # FRUIT.append('chuoi')
        ListOfMeal.append('chuoi')
        CheckBoxForMeal[32] = True
    else:
        TocalCalo -= 35
        # FRUIT.append('chuoi')
        ListOfMeal.append('chuoi')
        CheckBoxForMeal[32] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def thom(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.thom_2.isChecked() == True:
        TocalCalo += 17
        # FRUIT.append('thom')
        ListOfMeal.append('thom')
        CheckBoxForMeal[33] = True
    else:
        TocalCalo -= 17
        # FRUIT.remove('thom')
        ListOfMeal.remove('thom')
        CheckBoxForMeal[33] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def xoai(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.xoai_2.isChecked() == True:
        TocalCalo += 179
        # FRUIT.append('xoai')
        ListOfMeal.append('xoai')
        CheckBoxForMeal[34] = True
    else:
        TocalCalo -= 179
        # FRUIT.remove('xoai')
        ListOfMeal.remove('xoai')
        CheckBoxForMeal[34] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def saurieng(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.saurieng_2.isChecked() == True:
        TocalCalo += 28
        # FRUIT.append('saurieng')
        ListOfMeal.append('saurieng')
        CheckBoxForMeal[35] = True
    else:
        TocalCalo -= 28
        # FRUIT.remove('saurieng')
        ListOfMeal.remove('saurieng')
        CheckBoxForMeal[35] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def mangcut(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.mangcut_2.isChecked() == True:
        TocalCalo += 13
        # FRUIT.append('mangcut')
        ListOfMeal.append('mangcut')
        CheckBoxForMeal[36] = True
    else:
        TocalCalo -= 13
        # FRUIT.remove('mangcut')
        ListOfMeal.remove('mangcut')
        CheckBoxForMeal[36] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def coc(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.coc_2.isChecked() == True:
        TocalCalo += 34
        # FRUIT.append('coc')
        ListOfMeal.append('coc')
        CheckBoxForMeal[37] = True
    else:
        TocalCalo -= 34
        # FRUIT.remove('coc')
        ListOfMeal.remove('coc')
        CheckBoxForMeal[37] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def nho(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.nho_2.isChecked() == True:
        TocalCalo += 68
        # FRUIT.append('nho')
        ListOfMeal.append('nho')
        CheckBoxForMeal[38] = True
    else:
        TocalCalo -= 68
        # FRUIT.remove('nho')
        ListOfMeal.remove('nho')
        CheckBoxForMeal[38] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def duahau(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.duahau_2.isChecked() == True:
        TocalCalo += 21
        # FRUIT.append('duahau')
        ListOfMeal.append('duahau')
        CheckBoxForMeal[39] = True
    else:
        TocalCalo -= 21
        # FRUIT.remove('duahau')
        ListOfMeal.remove('duahau')
        CheckBoxForMeal[39] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def buoi(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.buoi_2.isChecked() == True:
        TocalCalo += 8
        # FRUIT.append('buoi')
        ListOfMeal.append('buoi')
        CheckBoxForMeal[40] = True
    else:
        TocalCalo -= 8
        # FRUIT.remove('buoi')
        ListOfMeal.remove('buoi')
        CheckBoxForMeal[40] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def khoailang(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.khoailang_2.isChecked() == True:
        TocalCalo += 131
        # FRUIT.append('khoailang')
        ListOfMeal.append('khoailang')
        CheckBoxForMeal[41] = True
    else:
        TocalCalo -= 131
        # FRUIT.remove('khoailang')
        ListOfMeal.remove('khoailang')
        CheckBoxForMeal[41] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def le(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.le_2.isChecked() == True:
        TocalCalo += 91
        # FRUIT.append('le')
        ListOfMeal.append('le')
        CheckBoxForMeal[42] = True
    else:
        TocalCalo -= 91
        # FRUIT.remove('le')
        ListOfMeal.remove('le')
        CheckBoxForMeal[42] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def bapluoc(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.bapluoc_2.isChecked() == True:
        TocalCalo += 192
        # FRUIT.append('bapluoc')
        ListOfMeal.append('bapluoc')
        CheckBoxForMeal[43] = True
    else:
        TocalCalo -= 192
        # FRUIT.remove('bapluoc')
        ListOfMeal.remove('bapluoc')
        CheckBoxForMeal[43] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def khoaitay(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.khoaitay_2.isChecked() == True:
        TocalCalo += 131
        # FRUIT.append('khoaitay')
        ListOfMeal.append('khoaitay')
        CheckBoxForMeal[44] = True
    else:
        TocalCalo -= 131
        # FRUIT.remove('khoaitay')
        ListOfMeal.remove('khoaitay')
        CheckBoxForMeal[44] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def dauphong(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.dauphong_2.isChecked() == True:
        TocalCalo += 395
        # FRUIT.append('dauphong')
        ListOfMeal.append('dauphong')
        CheckBoxForMeal[45] = True
    else:
        TocalCalo -= 395
        # FRUIT.remove('dauphong')
        ListOfMeal.remove('dauphong')
        CheckBoxForMeal[45] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def dudu(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.dudu_2.isChecked() == True:
        TocalCalo += 125
        # FRUIT.append('dudu')
        ListOfMeal.append('dudu')
        CheckBoxForMeal[46] = True
    else:
        TocalCalo -= 125
        # FRUIT.remove('dudu')
        ListOfMeal.remove('dudu')
        CheckBoxForMeal[46] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def sori(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.sori_2.isChecked() == True:
        TocalCalo += 14
        # FRUIT.append('sori')
        ListOfMeal.append('sori')
        CheckBoxForMeal[47] = True
    else:
        TocalCalo -= 14
        # FRUIT.remove('sori')
        ListOfMeal.remove('sori')
        CheckBoxForMeal[47] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def cam(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.cam_2.isChecked() == True:
        TocalCalo += 68
        # FRUIT.append('cam')
        ListOfMeal.append('cam')
        CheckBoxForMeal[48] = True
    else:
        TocalCalo -= 68
        # FRUIT.remove('cam')
        ListOfMeal.remove('cam')
        CheckBoxForMeal[48] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def oi(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.oi_2.isChecked() == True:
        TocalCalo += 53
        # FRUIT.append('oi')
        ListOfMeal.append('oi')
        CheckBoxForMeal[49] = True
    else:
        TocalCalo -= 53
        # FRUIT.remove('oi')
        ListOfMeal.remove('oi')
        CheckBoxForMeal[49] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def thanhlong(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,FRUIT
    if ui_1.thanhlong_2.isChecked() == True:
        TocalCalo += 225
        # FRUIT.append('thanhlong')
        ListOfMeal.append('thanhlong')
        CheckBoxForMeal[50] = True
    else:
        TocalCalo -= 225
        # FRUIT.remove('thanhlong')
        ListOfMeal.remove('thanhlong')
        CheckBoxForMeal[50] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
###########################Orther################
def chebap(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.chebap_2.isChecked() == True:
        TocalCalo += 325
        ListOfMeal.append('chebap')
        # OTHER.append('chebap')
        CheckBoxForMeal[51] = True
    else:
        TocalCalo -= 325
        ListOfMeal.remove('chebap')
        # OTHER.remove('chebap')
        CheckBoxForMeal[51] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def chechuoi(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.chechuoi_2.isChecked() == True:
        TocalCalo += 332
        ListOfMeal.append('chechuoi')
        # OTHER.append('chechuoi')
        CheckBoxForMeal[52] = True
    else:
        TocalCalo -= 332
        ListOfMeal.remove('chechuoi')
        # OTHER.remove('chechuoi')
        CheckBoxForMeal[52] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def chedauden(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.chedauden_2.isChecked() == True:
        TocalCalo += 419
        ListOfMeal.append('chedauden')
        # OTHER.append('chedauden')
        CheckBoxForMeal[53] = True
    else:
        TocalCalo -= 419
        ListOfMeal.remove('chedauden')
        # OTHER.remove('chedauden')
        CheckBoxForMeal[53] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def chedauxanh(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.chedauxanh_2.isChecked() == True:
        TocalCalo += 359
        ListOfMeal.append('chedauxanh')
        # OTHER.append('chedauxanh')
        CheckBoxForMeal[54] = True
    else:
        TocalCalo -= 359
        ListOfMeal.remove('chedauxanh')
        # OTHER.remove('chedauxanh')
        CheckBoxForMeal[54] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def chenep(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.chenep_2.isChecked() == True:
        TocalCalo += 420
        ListOfMeal.append('chenep')
        # OTHER.append('chenep')
        CheckBoxForMeal[55] = True
    else:
        TocalCalo -= 420
        ListOfMeal.remove('chenep')
        # OTHER.remove('chenep')
        CheckBoxForMeal[55] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def chetroinuoc(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.chetroinuoc_2.isChecked() == True:
        TocalCalo += 513
        ListOfMeal.append('chetroinuoc')
        # OTHER.append('chetroinuoc')
        CheckBoxForMeal[56] = True
    else:
        TocalCalo -= 513
        ListOfMeal.remove('chetroinuoc')
        # OTHER.remove('chetroinuoc')
        CheckBoxForMeal[56] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def xoibap(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.xoibap_2.isChecked() == True:
        TocalCalo += 332
        ListOfMeal.append('xoibap')
        # OTHER.append('xoibap')
        CheckBoxForMeal[57] = True
    else:
        TocalCalo -= 332
        ListOfMeal.remove('xoibap')
        # OTHER.remove('xoibap')
        CheckBoxForMeal[57] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def xoidauden(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.xoidauden_2.isChecked() == True:
        TocalCalo += 550
        ListOfMeal.append('xoidauden')
        # OTHER.append('xoidauden')
        CheckBoxForMeal[58] = True
    else:
        TocalCalo -= 550
        ListOfMeal.remove('xoidauden')
        # OTHER.remove('xoidauden')
        CheckBoxForMeal[58] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def xoidauphong(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.xoidauphong_2.isChecked() == True:
        TocalCalo += 650
        ListOfMeal.append('xoidauphong')
        # OTHER.append('xoidauphong')
        CheckBoxForMeal[59] = True
    else:
        TocalCalo -= 650
        ListOfMeal.remove('xoidauphong')
        # OTHER.remove('xoidauphong')
        CheckBoxForMeal[59] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def xoigac(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.xoigac_2.isChecked() == True:
        TocalCalo += 590
        ListOfMeal.append('xoigac')
        # OTHER.append('xoigac')
        CheckBoxForMeal[60] = True
    else:
        TocalCalo -= 590
        ListOfMeal.remove('xoigac')
        # OTHER.remove('xoigac')
        CheckBoxForMeal[60] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def cafe(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.cafe_2.isChecked() == True:
        TocalCalo += 40
        ListOfMeal.append('cafe')
        # OTHER.append('cafe')
        CheckBoxForMeal[61] = True
    else:
        TocalCalo -= 40
        ListOfMeal.remove('cafe')
        # OTHER.remove('cafe')
        CheckBoxForMeal[61] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def nuocam(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.nuocam_2.isChecked() == True:
        TocalCalo += 226
        ListOfMeal.append('nuocam')
        # OTHER.append('nuocam')
        CheckBoxForMeal[62] = True
    else:
        TocalCalo -= 226
        ListOfMeal.remove('nuocam')
        # OTHER.remove('nuocam')
        CheckBoxForMeal[62] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def nuocchanh(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.nuocchanh_2.isChecked() == True:
        TocalCalo += 150
        ListOfMeal.append('nuocchanh')
        # OTHER.append('nuocchanh')
        CheckBoxForMeal[63] = True
    else:
        TocalCalo -= 150
        ListOfMeal.remove('nuocchanh')
        # OTHER.remove('nuocchanh')
        CheckBoxForMeal[63] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def nuocmia(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.nuocmia_2.isChecked() == True:
        TocalCalo += 100
        ListOfMeal.append('nuocmia')
        # OTHER.append('nuocmia')
        CheckBoxForMeal[64] = True
    else:
        TocalCalo -= 100
        ListOfMeal.remove('nuocmia')
        # OTHER.remove('nuocmia')
        CheckBoxForMeal[64] = True
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def nuocrauma(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.nuocrauma_2.isChecked() == True:
        TocalCalo += 174
        ListOfMeal.append('nuocrauma')
        # OTHER.append('nuocrauma')
        CheckBoxForMeal[65] = True
    else:
        TocalCalo -= 174
        ListOfMeal.remove('nuocrauma')
        # OTHER.remove('nuocrauma')
        CheckBoxForMeal[65] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def suachua(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.suachua_2.isChecked() == True:
        TocalCalo += 150
        ListOfMeal.append('suachua')
        # OTHER.append('suachua')
        CheckBoxForMeal[66] = True
    else:
        TocalCalo -= 150
        ListOfMeal.remove('suachua')
        # OTHER.remove('suachua')
        CheckBoxForMeal[66] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def trungcut(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.trungcut_2.isChecked() == True:
        TocalCalo += 17
        ListOfMeal.append('trungcut')
        # OTHER.append('trungcut')
        CheckBoxForMeal[67] = True
    else:
        TocalCalo -= 17
        ListOfMeal.remove('trungcut')
        # OTHER.remove('trungcut')
        CheckBoxForMeal[67] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def trungga(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.trungga_2.isChecked() == True:
        TocalCalo += 58
        ListOfMeal.append('trungga')
        # OTHER.append('trungga')
        CheckBoxForMeal[68] = True
    else:
        ui_1.trungga_2.isChecked() == False
        TocalCalo -= 58
        ListOfMeal.remove('trungga')
        # OTHER.remove('trungga')
        CheckBoxForMeal[68] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)
def trungvit(ListOfMeal,CheckBoxForMeal):
    global TocalCalo,OTHER
    if ui_1.trungvit_2.isChecked() == True:
        TocalCalo += 70
        ListOfMeal.append('trungvit')
        # OTHER.append('trungvit')
        CheckBoxForMeal[69] = True
    else:
        TocalCalo -= 70
        ListOfMeal.remove('trungvit')
        # OTHER.remove('trungvit')
        CheckBoxForMeal[69] = False
    ui_1.label_12.setText(str(TocalCalo))
    ui_1.listWidget_4.clear()
    ui_1.listWidget_4.addItems(ListOfMeal)


def SupportFunction():
    chat_client.FirstScreen(Name)

class MainWindowSceen(QMainWindow):
    def __init__(self):
        global TocalCalo, TocalCaloDinner, TocalCaloLunch
        QMainWindow.__init__(self)
        MainWindow.setFixedSize(1201, 708)
        self.ui = MainMenu.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.ui.TimeTable.clicked.connect(TimeTableFunction)
        self.ui.Gym.clicked.connect(GymFunction)
        self.ui.Yoga.clicked.connect(YogaFunction)
        self.ui.Meal.clicked.connect(MealFunction)
        self.ui.Profile.clicked.connect(UpdateProfile)
        self.ui.Chat.clicked.connect(SupportFunction)
        self.ui.label_3.setText(str(CaloNeed))
        self.ui.label_6.setText(str(int(TocalCaloDinner) + int(TocalCaloLunch) + int(TocalCaloBreakFast)))


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
            # t = threading.Thread(target=main)
            # t.start()

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
    tt.giayGym = 0
    # giay_tt = False
    cp = 1
    if (z == 0):
        func = 0
    elif (z == 1):
        func = 1
    elif (z == 2):
        func = 2
    elif (z == 3):
        func = 3
    elif (z == 4):
        func = 4
    elif (z == 5):
        func = 5
    elif (z == 6):
        func = 6
    elif (z == 7):
        func = 7
    elif(z == 8):
        func = 8
    else:
        func = 9
    if (running == False):
        t = threading.Thread(target=main)
        t.start()
    winsound.PlaySound('NhacGym1.WAV', winsound.SND_ASYNC)


def count_task_yoga(y):  # z la chuc nang duoc quy dinh trong Yoga
    global cp, giay_tt, func_yoga,timer
    # playS("sound\\Button_1_down.wav", 0)
    # playS("sound\\
    cp = 0
    yp.init(0)
    time.sleep(0.1)
    yp.init(1)
    cp = 2
    if (y == 1):
        func_yoga = 1
    elif (y == 2):
        func_yoga = 2
    elif (y == 3):
        func_yoga = 3
    elif (y == 4):
        func_yoga = 4
    elif (y == 5):
        func_yoga = 5
    elif (y == 6):
        func_yoga = 6
    else:
        func_yoga = 7
    if (running == False):
        t = threading.Thread(target=main)
        t.start()
    # winsound.PlaySound('NhacGym1.WAV', winsound.SND_ASYNC)

def hienhinhyoga(a):
        # hien thi anh len khung information
        image_path = "image-Yoga\\" + a  # path to your image file
        image_profile = QtGui.QImage(image_path)  # QImage object
        image_profile = image_profile.scaled(231, 211)  # To scale image for example and keep its Aspect Ration
        ui.information_yoga.setPixmap(QtGui.QPixmap.fromImage(image_profile))

def hienhinh(a, b, per):
    if (per <= 20):
        # hien thi anh len khung information
        image_path = "hinh\\" + a  # path to your image file
        image_profile = QtGui.QImage(image_path)  # QImage object
        image_profile = image_profile.scaled(231, 211)  # To scale image for example and keep its Aspect Ration
        ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))



    elif (per >= 90):
        # label_Image = QtGui.QLabel(frame)
        image_path = "hinh\\" + b  # path to your image file
        image_profile = QtGui.QImage(image_path)  # QImage object
        image_profile = image_profile.scaled(261, 241)  # To scale image for example and keep its Aspect Ration
        ui.information.setPixmap(QtGui.QPixmap.fromImage(image_profile))

# def h_playS(a, b):  # b la cho phep chay vong lap    #0 la 1 lan, 1 la nhieu lan
#     # AM THANH
#     # playsound.playsound(a)
#     winsound.PlaySound(a, winsound.SND_LOOP + (winsound.SND_ASYNC & b))
#
#
# def playS(a, b):
#     s = threading.Thread(target=h_playS, args=(a, b))
#     s.start()
#
#
# def h_playS1(a):  # b la cho phep chay vong lap    #0 la 1 lan, 1 la nhieu la
# 	# AM THANH
# 	playsound.playsound(a)


# def playS1(a):
#         s = threading.Thread(target=h_playS1, args=(a,))
#         s.start()




############################################################################
#######  CHUONG TRINH CHINH
############################################################################
def main():
    global img, ui, rep, func, flagRight, check, dem, yoga_hinh, phut_tt,func_yoga,CaloNeed,toast,progress_val,running
    bc.count = 0
    running = True
    while True:
        if cp == 1:
            # playS("sound\\Button_1_down.wav", 0)
            img, per, rep = bc.run(700, 491, func)
            # hien thi hinh anh len khung view label
            image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            ui.view.setPixmap(QtGui.QPixmap.fromImage(image))

            # hien thi dem thoi gian
            ui.timeLabel.setText(str(int(tt.phut / 10)) + str(int(tt.phut % 10)) + ":" + str(int(tt.giayGym / 10)) + str(int(tt.giayGym % 10)))
            ui.lcdNumber.display(rep)
            if func == 4:
                hienhinh("dumbbell_shoulder-1", "dumbbell_shoulder-2", per)
                # barbel crul
            if func == 2:
                # right arm
                hienhinh("tay-tadon -2.jpg", "tay-tadon-1.jpg", per)
            elif func == 0:
                # left arm
                hienhinh("tay-tadon -2.jpg", "tay-tadon-1.jpg", per)
                #  Leg raise
            elif func == 9:
                # abs
                hienhinh("leg-raise-1.jpg", "leg-raise-2.jpg", per)

            elif func == 5:
                # squat
                hienhinh("swat-1.jpg", "swat-2.jpg", per)
            elif func == 1:
                # pushup hit dat
                hienhinh("hit-dat-1.jpg", "hit-dat-2.jpg", per)
                # Skull crusher (taysau +ghế)
            elif func == 6:
                # tay trái
                hienhinh("tay-sau-voi-ghe.jpg", "tay-sau-voi-ghe-2.jpg", per)
            elif func == 7:
                # tay phãi
                hienhinh("tay-sau-voi-ghe.jpg", "tay-sau-voi-ghe-2.jpg", per)
                # Crunch gập bụng
            elif func == 8:
                hienhinh("gap-bung-1.jpg", "gap-bung-2.jpg", per)
                # Dumbbell flyes (ngực trước với tạ đơn)
            elif func == 3:
                hienhinh("nguctruoc-1.jpg", "nguctruoc-2.jpg", per)


        if cp == 2:
            # playS("sound\\Button_1_down.wav", 0)
            img, check, dem, z = yp.run(700, 491, func_yoga)
            # # hien thi hinh anh len khung view label
            image = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            ui.view_yoga.setPixmap(QtGui.QPixmap.fromImage(image))
            # hien thi thoi gian len widget

            if z == 1:
                hienhinhyoga("pose-chien-binh.jpg")
            # Pose Tree
            elif (z == 2):
                hienhinhyoga("pose-tree.jpg")
            # Pose Triangle
            elif (z == 3):
                hienhinhyoga("pose-tamgiac.jpg")
            # Plank ( khuỵu tay)
            elif z == 5:
                hienhinhyoga("blank-khuyu-tay.jpg")
            # Plank ( chống thẳng tay)
            elif z == 4:
                hienhinhyoga("blank-thang-tay.jpg")
            # Pose Boat
            elif z == 6:
                hienhinhyoga("BOAT-pose.png")
            elif z == 7:
                hienhinhyoga("cobra-pose.jpg")
            #     #HoanhThanh
            # elif (z == 8):
            #     #Phat Am thanh Hoan Thanh
            #     winsound.PlaySound('abcd', winsound.SND_ALIAS)
            #     comboboxFuntionYoga()
            ui.widget.rpb_setValue(tt.giay)
            if (tt.giay == max_value):
                winsound.PlaySound('abcd', winsound.SND_ALIAS)
                tt.giay = 0

if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    splashscreen = SplashScreen()
    MainWindow = QtWidgets.QMainWindow()
    tt.init()
    toast = ToastNotifier()

try:
    sys.exit(app1.exec_())
except:
    print("Exiting")

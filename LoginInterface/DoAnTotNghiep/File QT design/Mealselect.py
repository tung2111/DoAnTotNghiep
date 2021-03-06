# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MealSelect.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 551)
        MainWindow.setStyleSheet("background-color:rgb(118, 118, 118);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 15, 20, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color : rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setMaximumSize(QtCore.QSize(241, 16777215))
        self.listWidget_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.listWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_2.setStyleSheet("background-color:rgb(0, 255, 127);\n"
"border-radius:20px;")
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget_2.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget_2.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget_2.setProperty("isWrapping", False)
        self.listWidget_2.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget_2.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_2.setModelColumn(0)
        self.listWidget_2.setUniformItemSizes(False)
        self.listWidget_2.setWordWrap(False)
        self.listWidget_2.setSelectionRectVisible(False)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_5.addWidget(self.listWidget_2)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(-10, 0, 400, 51))
        self.label_3.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color : rgb(255, 85, 0);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(230, 74, 41, 16))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color : rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color : rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_5)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 601, 518))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_2.setStyleSheet("background-color:rgb(255, 181, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gaxaot = QtWidgets.QCheckBox(self.frame_2)
        self.gaxaot.setObjectName("gaxaot")
        self.verticalLayout_2.addWidget(self.gaxaot)
        self.gakho = QtWidgets.QCheckBox(self.frame_2)
        self.gakho.setObjectName("gakho")
        self.verticalLayout_2.addWidget(self.gakho)
        self.mucxao = QtWidgets.QCheckBox(self.frame_2)
        self.mucxao.setObjectName("mucxao")
        self.verticalLayout_2.addWidget(self.mucxao)
        self.suongnuong = QtWidgets.QCheckBox(self.frame_2)
        self.suongnuong.setObjectName("suongnuong")
        self.verticalLayout_2.addWidget(self.suongnuong)
        self.suongram = QtWidgets.QCheckBox(self.frame_2)
        self.suongram.setObjectName("suongram")
        self.verticalLayout_2.addWidget(self.suongram)
        self.thitheoquay = QtWidgets.QCheckBox(self.frame_2)
        self.thitheoquay.setObjectName("thitheoquay")
        self.verticalLayout_2.addWidget(self.thitheoquay)
        self.thitboxao = QtWidgets.QCheckBox(self.frame_2)
        self.thitboxao.setObjectName("thitboxao")
        self.verticalLayout_2.addWidget(self.thitboxao)
        self.thitkhotieu = QtWidgets.QCheckBox(self.frame_2)
        self.thitkhotieu.setObjectName("thitkhotieu")
        self.verticalLayout_2.addWidget(self.thitkhotieu)
        self.camoikho = QtWidgets.QCheckBox(self.frame_2)
        self.camoikho.setObjectName("camoikho")
        self.verticalLayout_2.addWidget(self.camoikho)
        self.cari = QtWidgets.QCheckBox(self.frame_2)
        self.cari.setObjectName("cari")
        self.verticalLayout_2.addWidget(self.cari)
        self.bobia = QtWidgets.QCheckBox(self.frame_2)
        self.bobia.setObjectName("bobia")
        self.verticalLayout_2.addWidget(self.bobia)
        self.cabacmachien = QtWidgets.QCheckBox(self.frame_2)
        self.cabacmachien.setObjectName("cabacmachien")
        self.verticalLayout_2.addWidget(self.cabacmachien)
        self.cabacmakho = QtWidgets.QCheckBox(self.frame_2)
        self.cabacmakho.setObjectName("cabacmakho")
        self.verticalLayout_2.addWidget(self.cabacmakho)
        self.cangukho = QtWidgets.QCheckBox(self.frame_2)
        self.cangukho.setObjectName("cangukho")
        self.verticalLayout_2.addWidget(self.cangukho)
        self.chalua = QtWidgets.QCheckBox(self.frame_2)
        self.chalua.setObjectName("chalua")
        self.verticalLayout_2.addWidget(self.chalua)
        self.ganheoxao = QtWidgets.QCheckBox(self.frame_2)
        self.ganheoxao.setObjectName("ganheoxao")
        self.verticalLayout_2.addWidget(self.ganheoxao)
        self.goikhobo = QtWidgets.QCheckBox(self.frame_2)
        self.goikhobo.setObjectName("goikhobo")
        self.verticalLayout_2.addWidget(self.goikhobo)
        self.goitom = QtWidgets.QCheckBox(self.frame_2)
        self.goitom.setObjectName("goitom")
        self.verticalLayout_2.addWidget(self.goitom)
        self.khoquaxaotrung = QtWidgets.QCheckBox(self.frame_2)
        self.khoquaxaotrung.setObjectName("khoquaxaotrung")
        self.verticalLayout_2.addWidget(self.khoquaxaotrung)
        self.lapxuongchien = QtWidgets.QCheckBox(self.frame_2)
        self.lapxuongchien.setObjectName("lapxuongchien")
        self.verticalLayout_2.addWidget(self.lapxuongchien)
        self.mucxaothapcam = QtWidgets.QCheckBox(self.frame_2)
        self.mucxaothapcam.setObjectName("mucxaothapcam")
        self.verticalLayout_2.addWidget(self.mucxaothapcam)
        self.boxaomang = QtWidgets.QCheckBox(self.frame_2)
        self.boxaomang.setObjectName("boxaomang")
        self.verticalLayout_2.addWidget(self.boxaomang)
        self.boxaonam = QtWidgets.QCheckBox(self.frame_2)
        self.boxaonam.setObjectName("boxaonam")
        self.verticalLayout_2.addWidget(self.boxaonam)
        self.thitkhotrung = QtWidgets.QCheckBox(self.frame_2)
        self.thitkhotrung.setObjectName("thitkhotrung")
        self.verticalLayout_2.addWidget(self.thitkhotrung)
        self.bunrieu = QtWidgets.QCheckBox(self.frame_2)
        self.bunrieu.setObjectName("bunrieu")
        self.verticalLayout_2.addWidget(self.bunrieu)
        self.bunbohue = QtWidgets.QCheckBox(self.frame_2)
        self.bunbohue.setObjectName("bunbohue")
        self.verticalLayout_2.addWidget(self.bunbohue)
        self.bunthitnuong = QtWidgets.QCheckBox(self.frame_2)
        self.bunthitnuong.setObjectName("bunthitnuong")
        self.verticalLayout_2.addWidget(self.bunthitnuong)
        self.bunxao = QtWidgets.QCheckBox(self.frame_2)
        self.bunxao.setObjectName("bunxao")
        self.verticalLayout_2.addWidget(self.bunxao)
        self.canhkhoqua = QtWidgets.QCheckBox(self.frame_2)
        self.canhkhoqua.setObjectName("canhkhoqua")
        self.verticalLayout_2.addWidget(self.canhkhoqua)
        self.chaolong = QtWidgets.QCheckBox(self.frame_2)
        self.chaolong.setObjectName("chaolong")
        self.verticalLayout_2.addWidget(self.chaolong)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setStyleSheet("background-color:rgb(255, 181, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bo = QtWidgets.QCheckBox(self.frame_3)
        self.bo.setObjectName("bo")
        self.verticalLayout_4.addWidget(self.bo)
        self.chuoi = QtWidgets.QCheckBox(self.frame_3)
        self.chuoi.setObjectName("chuoi")
        self.verticalLayout_4.addWidget(self.chuoi)
        self.thom = QtWidgets.QCheckBox(self.frame_3)
        self.thom.setObjectName("thom")
        self.verticalLayout_4.addWidget(self.thom)
        self.xoai = QtWidgets.QCheckBox(self.frame_3)
        self.xoai.setObjectName("xoai")
        self.verticalLayout_4.addWidget(self.xoai)
        self.saurieng = QtWidgets.QCheckBox(self.frame_3)
        self.saurieng.setObjectName("saurieng")
        self.verticalLayout_4.addWidget(self.saurieng)
        self.mangcut = QtWidgets.QCheckBox(self.frame_3)
        self.mangcut.setObjectName("mangcut")
        self.verticalLayout_4.addWidget(self.mangcut)
        self.coc = QtWidgets.QCheckBox(self.frame_3)
        self.coc.setObjectName("coc")
        self.verticalLayout_4.addWidget(self.coc)
        self.nho = QtWidgets.QCheckBox(self.frame_3)
        self.nho.setObjectName("nho")
        self.verticalLayout_4.addWidget(self.nho)
        self.duahau = QtWidgets.QCheckBox(self.frame_3)
        self.duahau.setObjectName("duahau")
        self.verticalLayout_4.addWidget(self.duahau)
        self.buoi = QtWidgets.QCheckBox(self.frame_3)
        self.buoi.setObjectName("buoi")
        self.verticalLayout_4.addWidget(self.buoi)
        self.khoailang = QtWidgets.QCheckBox(self.frame_3)
        self.khoailang.setObjectName("khoailang")
        self.verticalLayout_4.addWidget(self.khoailang)
        self.le = QtWidgets.QCheckBox(self.frame_3)
        self.le.setObjectName("le")
        self.verticalLayout_4.addWidget(self.le)
        self.bapluoc = QtWidgets.QCheckBox(self.frame_3)
        self.bapluoc.setObjectName("bapluoc")
        self.verticalLayout_4.addWidget(self.bapluoc)
        self.khoaitay = QtWidgets.QCheckBox(self.frame_3)
        self.khoaitay.setObjectName("khoaitay")
        self.verticalLayout_4.addWidget(self.khoaitay)
        self.dauphong = QtWidgets.QCheckBox(self.frame_3)
        self.dauphong.setObjectName("dauphong")
        self.verticalLayout_4.addWidget(self.dauphong)
        self.dudu = QtWidgets.QCheckBox(self.frame_3)
        self.dudu.setObjectName("dudu")
        self.verticalLayout_4.addWidget(self.dudu)
        self.sori = QtWidgets.QCheckBox(self.frame_3)
        self.sori.setObjectName("sori")
        self.verticalLayout_4.addWidget(self.sori)
        self.cam = QtWidgets.QCheckBox(self.frame_3)
        self.cam.setObjectName("cam")
        self.verticalLayout_4.addWidget(self.cam)
        self.oi = QtWidgets.QCheckBox(self.frame_3)
        self.oi.setObjectName("oi")
        self.verticalLayout_4.addWidget(self.oi)
        self.thanhlong = QtWidgets.QCheckBox(self.frame_3)
        self.thanhlong.setObjectName("thanhlong")
        self.verticalLayout_4.addWidget(self.thanhlong)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setStyleSheet("background-color:rgb(255, 181, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.chebap = QtWidgets.QCheckBox(self.frame)
        self.chebap.setObjectName("chebap")
        self.verticalLayout_3.addWidget(self.chebap)
        self.chechuoi = QtWidgets.QCheckBox(self.frame)
        self.chechuoi.setObjectName("chechuoi")
        self.verticalLayout_3.addWidget(self.chechuoi)
        self.chedauden = QtWidgets.QCheckBox(self.frame)
        self.chedauden.setObjectName("chedauden")
        self.verticalLayout_3.addWidget(self.chedauden)
        self.chedauxanh = QtWidgets.QCheckBox(self.frame)
        self.chedauxanh.setObjectName("chedauxanh")
        self.verticalLayout_3.addWidget(self.chedauxanh)
        self.chenep = QtWidgets.QCheckBox(self.frame)
        self.chenep.setObjectName("chenep")
        self.verticalLayout_3.addWidget(self.chenep)
        self.chetroinuoc = QtWidgets.QCheckBox(self.frame)
        self.chetroinuoc.setObjectName("chetroinuoc")
        self.verticalLayout_3.addWidget(self.chetroinuoc)
        self.xoibap = QtWidgets.QCheckBox(self.frame)
        self.xoibap.setObjectName("xoibap")
        self.verticalLayout_3.addWidget(self.xoibap)
        self.xoidauden = QtWidgets.QCheckBox(self.frame)
        self.xoidauden.setObjectName("xoidauden")
        self.verticalLayout_3.addWidget(self.xoidauden)
        self.xoidauphong = QtWidgets.QCheckBox(self.frame)
        self.xoidauphong.setObjectName("xoidauphong")
        self.verticalLayout_3.addWidget(self.xoidauphong)
        self.xoigac = QtWidgets.QCheckBox(self.frame)
        self.xoigac.setObjectName("xoigac")
        self.verticalLayout_3.addWidget(self.xoigac)
        self.cafe = QtWidgets.QCheckBox(self.frame)
        self.cafe.setObjectName("cafe")
        self.verticalLayout_3.addWidget(self.cafe)
        self.nuocam = QtWidgets.QCheckBox(self.frame)
        self.nuocam.setObjectName("nuocam")
        self.verticalLayout_3.addWidget(self.nuocam)
        self.nuocchanh = QtWidgets.QCheckBox(self.frame)
        self.nuocchanh.setObjectName("nuocchanh")
        self.verticalLayout_3.addWidget(self.nuocchanh)
        self.nuocmia = QtWidgets.QCheckBox(self.frame)
        self.nuocmia.setObjectName("nuocmia")
        self.verticalLayout_3.addWidget(self.nuocmia)
        self.nuocrauma = QtWidgets.QCheckBox(self.frame)
        self.nuocrauma.setObjectName("nuocrauma")
        self.verticalLayout_3.addWidget(self.nuocrauma)
        self.suachua = QtWidgets.QCheckBox(self.frame)
        self.suachua.setObjectName("suachua")
        self.verticalLayout_3.addWidget(self.suachua)
        self.trungcut = QtWidgets.QCheckBox(self.frame)
        self.trungcut.setObjectName("trungcut")
        self.verticalLayout_3.addWidget(self.trungcut)
        self.trungga = QtWidgets.QCheckBox(self.frame)
        self.trungga.setObjectName("trungga")
        self.verticalLayout_3.addWidget(self.trungga)
        self.trungvit = QtWidgets.QCheckBox(self.frame)
        self.trungvit.setObjectName("trungvit")
        self.verticalLayout_3.addWidget(self.trungvit)
        self.banhbonglan = QtWidgets.QCheckBox(self.frame)
        self.banhbonglan.setObjectName("banhbonglan")
        self.verticalLayout_3.addWidget(self.banhbonglan)
        self.horizontalLayout.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setMaximumSize(QtCore.QSize(80, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Save.setFont(font)
        self.Save.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Save.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(0, 255, 255);\n"
"")
        self.Save.setObjectName("Save")
        self.verticalLayout.addWidget(self.Save)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Please select meal"))
        self.label_3.setText(_translate("MainWindow", "ToTal"))
        self.label_4.setText(_translate("MainWindow", "0.0"))
        self.label_6.setText(_translate("MainWindow", "(CALO)"))
        self.label_7.setText(_translate("MainWindow", "FOODS"))
        self.label_2.setText(_translate("MainWindow", "FRUITS"))
        self.label.setText(_translate("MainWindow", "OTHER"))
        self.gaxaot.setText(_translate("MainWindow", "G?? x??? ???t (270 Calo)"))
        self.gakho.setText(_translate("MainWindow", "G?? kho (300 Calo)"))
        self.mucxao.setText(_translate("MainWindow", "M???c x??o (180 Calo)"))
        self.suongnuong.setText(_translate("MainWindow", "S?????n n?????ng (110 Calo)"))
        self.suongram.setText(_translate("MainWindow", "S?????n ram (150 Calo)"))
        self.thitheoquay.setText(_translate("MainWindow", "Th???t heo quay (145 Calo)"))
        self.thitboxao.setText(_translate("MainWindow", "Th???t b?? x??o (200 Calo)"))
        self.thitkhotieu.setText(_translate("MainWindow", "Th???t kho ti??u (200 Calo)"))
        self.camoikho.setText(_translate("MainWindow", "C?? m??i kho (105 Calo)"))
        self.cari.setText(_translate("MainWindow", "C?? ri (278 Calo)"))
        self.bobia.setText(_translate("MainWindow", "B?? b??a (100 Calo)"))
        self.cabacmachien.setText(_translate("MainWindow", "C?? b???c m?? chi??n (135 Calo)"))
        self.cabacmakho.setText(_translate("MainWindow", "C?? b???c m?? kho (167 Calo)"))
        self.cangukho.setText(_translate("MainWindow", "C?? ng??? kho (122 Calo)"))
        self.chalua.setText(_translate("MainWindow", "Ch??? l???a (100 Calo)"))
        self.ganheoxao.setText(_translate("MainWindow", "Gan heo x??o (200 Calo)"))
        self.goikhobo.setText(_translate("MainWindow", "G???i kh?? b?? (268 Calo)"))
        self.goitom.setText(_translate("MainWindow", "G???i t??m (147 Calo)"))
        self.khoquaxaotrung.setText(_translate("MainWindow", "Kh??? qua x??o tr???ng (115 Calo)"))
        self.lapxuongchien.setText(_translate("MainWindow", "L???p x?????ng chi??n (300 Calo)"))
        self.mucxaothapcam.setText(_translate("MainWindow", "M???c x??o th???p c???m (135 Calo)"))
        self.boxaomang.setText(_translate("MainWindow", "B?? x??o m??ng (105 Calo)"))
        self.boxaonam.setText(_translate("MainWindow", "B?? x??o n???m (150 Calo)"))
        self.thitkhotrung.setText(_translate("MainWindow", "Th???t kho tr???ng (315 Calo)"))
        self.bunrieu.setText(_translate("MainWindow", "B??n ri??u (482 Calo)"))
        self.bunbohue.setText(_translate("MainWindow", "B??n b?? hu??? (479 Calo)"))
        self.bunthitnuong.setText(_translate("MainWindow", "B??n th???t n?????ng (451 Calo)"))
        self.bunxao.setText(_translate("MainWindow", "B??n x??o (570 Calo)"))
        self.canhkhoqua.setText(_translate("MainWindow", "Canh kh??? qua (88 Calo)"))
        self.chaolong.setText(_translate("MainWindow", "Ch??o l??ng (412 Calo)"))
        self.bo.setText(_translate("MainWindow", "B?? (184 Calo)"))
        self.chuoi.setText(_translate("MainWindow", "Chu???i (35 Calo)"))
        self.thom.setText(_translate("MainWindow", "Th??m (17 Calo)"))
        self.xoai.setText(_translate("MainWindow", "Xo??i (179 Calo)"))
        self.saurieng.setText(_translate("MainWindow", "S???u ri??ng (28 Calo)"))
        self.mangcut.setText(_translate("MainWindow", "M??ng c???t (13 Calo)"))
        self.coc.setText(_translate("MainWindow", "C??c (34 Calo)"))
        self.nho.setText(_translate("MainWindow", "Nho (68 Calo)"))
        self.duahau.setText(_translate("MainWindow", "D??a H???u (21 Calo)"))
        self.buoi.setText(_translate("MainWindow", "B?????i (8 Calo)"))
        self.khoailang.setText(_translate("MainWindow", "Khoai lang (131 Calo)"))
        self.le.setText(_translate("MainWindow", "L?? (91 Calo)"))
        self.bapluoc.setText(_translate("MainWindow", "B???p lu???c (192 Calo)"))
        self.khoaitay.setText(_translate("MainWindow", "Khoai t??y (131 Calo)"))
        self.dauphong.setText(_translate("MainWindow", "?????u ph???ng (395 Calo)"))
        self.dudu.setText(_translate("MainWindow", "??u ????? (125 Calo)"))
        self.sori.setText(_translate("MainWindow", "S?? ri (14 Calo)"))
        self.cam.setText(_translate("MainWindow", "Cam (68 Calo)"))
        self.oi.setText(_translate("MainWindow", "???i (53 Calo)"))
        self.thanhlong.setText(_translate("MainWindow", "Thanh long (255 Calo)"))
        self.chebap.setText(_translate("MainWindow", "Ch?? b???p (325 Calo)"))
        self.chechuoi.setText(_translate("MainWindow", "Ch?? chu???i (332 Calo)"))
        self.chedauden.setText(_translate("MainWindow", "Ch?? ?????u ??en (419 Calo)"))
        self.chedauxanh.setText(_translate("MainWindow", "Ch?? ?????u xanh (359 Calo)"))
        self.chenep.setText(_translate("MainWindow", "Ch?? n???p (420 Calo)"))
        self.chetroinuoc.setText(_translate("MainWindow", "Ch?? tr??i n?????c (513 Calo)"))
        self.xoibap.setText(_translate("MainWindow", "x??i b???p (322 calo)"))
        self.xoidauden.setText(_translate("MainWindow", "X??i ?????u ??en (550 Calo)"))
        self.xoidauphong.setText(_translate("MainWindow", "X??i ?????u ph???ng (650 Calo)"))
        self.xoigac.setText(_translate("MainWindow", "X??i g???c (590 Calo)"))
        self.cafe.setText(_translate("MainWindow", "Cafe (40 Calo)"))
        self.nuocam.setText(_translate("MainWindow", "N?????c cam (226 calo)"))
        self.nuocchanh.setText(_translate("MainWindow", "N?????c chanh (150 Calo)"))
        self.nuocmia.setText(_translate("MainWindow", "N?????c m??a (100 Calo)"))
        self.nuocrauma.setText(_translate("MainWindow", "N?????c rau m?? (174 Calo)"))
        self.suachua.setText(_translate("MainWindow", "S???a chua (150 Calo)"))
        self.trungcut.setText(_translate("MainWindow", "Tr???ng c??t (17 Calo)"))
        self.trungga.setText(_translate("MainWindow", "Tr???ng g?? (58 Calo)"))
        self.trungvit.setText(_translate("MainWindow", "Tr???ng v???t (70 Calo)"))
        self.banhbonglan.setText(_translate("MainWindow", "B??nh b??ng lan (100 Calo)"))
        self.Save.setText(_translate("MainWindow", "DONE"))

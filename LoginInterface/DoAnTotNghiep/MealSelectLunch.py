# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MealSelectLunch.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 660, 551))
        self.label.setStyleSheet("border-image: url(:/MENU/Lunch_Wallpaper.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 660, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_14 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("rgb(255, 148, 254)")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("color :rgb(85, 38, 82);\n"
"font: 75 18pt \"rgb(255, 148, 254)\";")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.listWidget_4 = QtWidgets.QListWidget(self.frame)
        self.listWidget_4.setMaximumSize(QtCore.QSize(241, 16777215))
        self.listWidget_4.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.listWidget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_4.setStyleSheet("background-color:rgb(0, 255, 127);\n"
"border-radius:20px;")
        self.listWidget_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listWidget_4.setTextElideMode(QtCore.Qt.ElideNone)
        self.listWidget_4.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget_4.setProperty("isWrapping", False)
        self.listWidget_4.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget_4.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_4.setModelColumn(0)
        self.listWidget_4.setUniformItemSizes(False)
        self.listWidget_4.setWordWrap(False)
        self.listWidget_4.setSelectionRectVisible(False)
        self.listWidget_4.setObjectName("listWidget_4")
        self.horizontalLayout_7.addWidget(self.listWidget_4)
        self.frame_10 = QtWidgets.QFrame(self.frame)
        self.frame_10.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_11 = QtWidgets.QLabel(self.frame_10)
        self.label_11.setGeometry(QtCore.QRect(-1, 0, 391, 51))
        self.label_11.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color : rgb(255, 85, 0);\n"
"border-radius: 10px;\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_10)
        self.label_12.setGeometry(QtCore.QRect(120, 80, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_10)
        self.label_13.setGeometry(QtCore.QRect(310, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.frame_10)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setStyleSheet("background-color:transparent;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 621, 518))
        self.scrollAreaWidgetContents_2.setStyleSheet("background-color:transparent;")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_7.setStyleSheet("background-color:rgb(255, 181, 255);\n"
"border-raidus: 20px;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gaxaot_2 = QtWidgets.QCheckBox(self.frame_7)
        self.gaxaot_2.setObjectName("gaxaot_2")
        self.verticalLayout_5.addWidget(self.gaxaot_2)
        self.gakho_2 = QtWidgets.QCheckBox(self.frame_7)
        self.gakho_2.setObjectName("gakho_2")
        self.verticalLayout_5.addWidget(self.gakho_2)
        self.mucxao_2 = QtWidgets.QCheckBox(self.frame_7)
        self.mucxao_2.setObjectName("mucxao_2")
        self.verticalLayout_5.addWidget(self.mucxao_2)
        self.suongnuong_2 = QtWidgets.QCheckBox(self.frame_7)
        self.suongnuong_2.setObjectName("suongnuong_2")
        self.verticalLayout_5.addWidget(self.suongnuong_2)
        self.suongram_2 = QtWidgets.QCheckBox(self.frame_7)
        self.suongram_2.setObjectName("suongram_2")
        self.verticalLayout_5.addWidget(self.suongram_2)
        self.thitheoquay_2 = QtWidgets.QCheckBox(self.frame_7)
        self.thitheoquay_2.setObjectName("thitheoquay_2")
        self.verticalLayout_5.addWidget(self.thitheoquay_2)
        self.thitboxao_2 = QtWidgets.QCheckBox(self.frame_7)
        self.thitboxao_2.setObjectName("thitboxao_2")
        self.verticalLayout_5.addWidget(self.thitboxao_2)
        self.thitkhotieu_2 = QtWidgets.QCheckBox(self.frame_7)
        self.thitkhotieu_2.setObjectName("thitkhotieu_2")
        self.verticalLayout_5.addWidget(self.thitkhotieu_2)
        self.camoikho_2 = QtWidgets.QCheckBox(self.frame_7)
        self.camoikho_2.setObjectName("camoikho_2")
        self.verticalLayout_5.addWidget(self.camoikho_2)
        self.cari_2 = QtWidgets.QCheckBox(self.frame_7)
        self.cari_2.setObjectName("cari_2")
        self.verticalLayout_5.addWidget(self.cari_2)
        self.bobia_2 = QtWidgets.QCheckBox(self.frame_7)
        self.bobia_2.setObjectName("bobia_2")
        self.verticalLayout_5.addWidget(self.bobia_2)
        self.cabacmachien_2 = QtWidgets.QCheckBox(self.frame_7)
        self.cabacmachien_2.setObjectName("cabacmachien_2")
        self.verticalLayout_5.addWidget(self.cabacmachien_2)
        self.cabacmakho_2 = QtWidgets.QCheckBox(self.frame_7)
        self.cabacmakho_2.setObjectName("cabacmakho_2")
        self.verticalLayout_5.addWidget(self.cabacmakho_2)
        self.cangukho_2 = QtWidgets.QCheckBox(self.frame_7)
        self.cangukho_2.setObjectName("cangukho_2")
        self.verticalLayout_5.addWidget(self.cangukho_2)
        self.chalua_2 = QtWidgets.QCheckBox(self.frame_7)
        self.chalua_2.setObjectName("chalua_2")
        self.verticalLayout_5.addWidget(self.chalua_2)
        self.ganheoxao_2 = QtWidgets.QCheckBox(self.frame_7)
        self.ganheoxao_2.setObjectName("ganheoxao_2")
        self.verticalLayout_5.addWidget(self.ganheoxao_2)
        self.goikhobo_2 = QtWidgets.QCheckBox(self.frame_7)
        self.goikhobo_2.setObjectName("goikhobo_2")
        self.verticalLayout_5.addWidget(self.goikhobo_2)
        self.goitom_2 = QtWidgets.QCheckBox(self.frame_7)
        self.goitom_2.setObjectName("goitom_2")
        self.verticalLayout_5.addWidget(self.goitom_2)
        self.khoquaxaotrung_2 = QtWidgets.QCheckBox(self.frame_7)
        self.khoquaxaotrung_2.setObjectName("khoquaxaotrung_2")
        self.verticalLayout_5.addWidget(self.khoquaxaotrung_2)
        self.lapxuongchien_2 = QtWidgets.QCheckBox(self.frame_7)
        self.lapxuongchien_2.setObjectName("lapxuongchien_2")
        self.verticalLayout_5.addWidget(self.lapxuongchien_2)
        self.mucxaothapcam_2 = QtWidgets.QCheckBox(self.frame_7)
        self.mucxaothapcam_2.setObjectName("mucxaothapcam_2")
        self.verticalLayout_5.addWidget(self.mucxaothapcam_2)
        self.boxaomang_2 = QtWidgets.QCheckBox(self.frame_7)
        self.boxaomang_2.setObjectName("boxaomang_2")
        self.verticalLayout_5.addWidget(self.boxaomang_2)
        self.boxaonam_2 = QtWidgets.QCheckBox(self.frame_7)
        self.boxaonam_2.setObjectName("boxaonam_2")
        self.verticalLayout_5.addWidget(self.boxaonam_2)
        self.thitkhotrung_2 = QtWidgets.QCheckBox(self.frame_7)
        self.thitkhotrung_2.setObjectName("thitkhotrung_2")
        self.verticalLayout_5.addWidget(self.thitkhotrung_2)
        self.bunrieu_2 = QtWidgets.QCheckBox(self.frame_7)
        self.bunrieu_2.setObjectName("bunrieu_2")
        self.verticalLayout_5.addWidget(self.bunrieu_2)
        self.bunbohue_2 = QtWidgets.QCheckBox(self.frame_7)
        self.bunbohue_2.setObjectName("bunbohue_2")
        self.verticalLayout_5.addWidget(self.bunbohue_2)
        self.bunthitnuong_2 = QtWidgets.QCheckBox(self.frame_7)
        self.bunthitnuong_2.setObjectName("bunthitnuong_2")
        self.verticalLayout_5.addWidget(self.bunthitnuong_2)
        self.bunxao_2 = QtWidgets.QCheckBox(self.frame_7)
        self.bunxao_2.setObjectName("bunxao_2")
        self.verticalLayout_5.addWidget(self.bunxao_2)
        self.canhkhoqua_2 = QtWidgets.QCheckBox(self.frame_7)
        self.canhkhoqua_2.setObjectName("canhkhoqua_2")
        self.verticalLayout_5.addWidget(self.canhkhoqua_2)
        self.chaolong_2 = QtWidgets.QCheckBox(self.frame_7)
        self.chaolong_2.setObjectName("chaolong_2")
        self.verticalLayout_5.addWidget(self.chaolong_2)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_8.setStyleSheet("background-color:rgb(255, 181, 255);\n"
"border-raidus: 10px;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.bo_2 = QtWidgets.QCheckBox(self.frame_8)
        self.bo_2.setObjectName("bo_2")
        self.verticalLayout_6.addWidget(self.bo_2)
        self.chuoi_2 = QtWidgets.QCheckBox(self.frame_8)
        self.chuoi_2.setObjectName("chuoi_2")
        self.verticalLayout_6.addWidget(self.chuoi_2)
        self.thom_2 = QtWidgets.QCheckBox(self.frame_8)
        self.thom_2.setObjectName("thom_2")
        self.verticalLayout_6.addWidget(self.thom_2)
        self.xoai_2 = QtWidgets.QCheckBox(self.frame_8)
        self.xoai_2.setObjectName("xoai_2")
        self.verticalLayout_6.addWidget(self.xoai_2)
        self.saurieng_2 = QtWidgets.QCheckBox(self.frame_8)
        self.saurieng_2.setObjectName("saurieng_2")
        self.verticalLayout_6.addWidget(self.saurieng_2)
        self.mangcut_2 = QtWidgets.QCheckBox(self.frame_8)
        self.mangcut_2.setObjectName("mangcut_2")
        self.verticalLayout_6.addWidget(self.mangcut_2)
        self.coc_2 = QtWidgets.QCheckBox(self.frame_8)
        self.coc_2.setObjectName("coc_2")
        self.verticalLayout_6.addWidget(self.coc_2)
        self.nho_2 = QtWidgets.QCheckBox(self.frame_8)
        self.nho_2.setObjectName("nho_2")
        self.verticalLayout_6.addWidget(self.nho_2)
        self.duahau_2 = QtWidgets.QCheckBox(self.frame_8)
        self.duahau_2.setObjectName("duahau_2")
        self.verticalLayout_6.addWidget(self.duahau_2)
        self.buoi_2 = QtWidgets.QCheckBox(self.frame_8)
        self.buoi_2.setObjectName("buoi_2")
        self.verticalLayout_6.addWidget(self.buoi_2)
        self.khoailang_2 = QtWidgets.QCheckBox(self.frame_8)
        self.khoailang_2.setObjectName("khoailang_2")
        self.verticalLayout_6.addWidget(self.khoailang_2)
        self.le_2 = QtWidgets.QCheckBox(self.frame_8)
        self.le_2.setObjectName("le_2")
        self.verticalLayout_6.addWidget(self.le_2)
        self.bapluoc_2 = QtWidgets.QCheckBox(self.frame_8)
        self.bapluoc_2.setObjectName("bapluoc_2")
        self.verticalLayout_6.addWidget(self.bapluoc_2)
        self.khoaitay_2 = QtWidgets.QCheckBox(self.frame_8)
        self.khoaitay_2.setObjectName("khoaitay_2")
        self.verticalLayout_6.addWidget(self.khoaitay_2)
        self.dauphong_2 = QtWidgets.QCheckBox(self.frame_8)
        self.dauphong_2.setObjectName("dauphong_2")
        self.verticalLayout_6.addWidget(self.dauphong_2)
        self.dudu_2 = QtWidgets.QCheckBox(self.frame_8)
        self.dudu_2.setObjectName("dudu_2")
        self.verticalLayout_6.addWidget(self.dudu_2)
        self.sori_2 = QtWidgets.QCheckBox(self.frame_8)
        self.sori_2.setObjectName("sori_2")
        self.verticalLayout_6.addWidget(self.sori_2)
        self.cam_2 = QtWidgets.QCheckBox(self.frame_8)
        self.cam_2.setObjectName("cam_2")
        self.verticalLayout_6.addWidget(self.cam_2)
        self.oi_2 = QtWidgets.QCheckBox(self.frame_8)
        self.oi_2.setObjectName("oi_2")
        self.verticalLayout_6.addWidget(self.oi_2)
        self.thanhlong_2 = QtWidgets.QCheckBox(self.frame_8)
        self.thanhlong_2.setObjectName("thanhlong_2")
        self.verticalLayout_6.addWidget(self.thanhlong_2)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_9.setStyleSheet("background-color:rgb(255, 181, 255);\n"
"")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chebap_2 = QtWidgets.QCheckBox(self.frame_9)
        self.chebap_2.setObjectName("chebap_2")
        self.verticalLayout_7.addWidget(self.chebap_2)
        self.chechuoi_2 = QtWidgets.QCheckBox(self.frame_9)
        self.chechuoi_2.setObjectName("chechuoi_2")
        self.verticalLayout_7.addWidget(self.chechuoi_2)
        self.chedauden_2 = QtWidgets.QCheckBox(self.frame_9)
        self.chedauden_2.setObjectName("chedauden_2")
        self.verticalLayout_7.addWidget(self.chedauden_2)
        self.chedauxanh_2 = QtWidgets.QCheckBox(self.frame_9)
        self.chedauxanh_2.setObjectName("chedauxanh_2")
        self.verticalLayout_7.addWidget(self.chedauxanh_2)
        self.chenep_2 = QtWidgets.QCheckBox(self.frame_9)
        self.chenep_2.setObjectName("chenep_2")
        self.verticalLayout_7.addWidget(self.chenep_2)
        self.chetroinuoc_2 = QtWidgets.QCheckBox(self.frame_9)
        self.chetroinuoc_2.setObjectName("chetroinuoc_2")
        self.verticalLayout_7.addWidget(self.chetroinuoc_2)
        self.xoibap_2 = QtWidgets.QCheckBox(self.frame_9)
        self.xoibap_2.setObjectName("xoibap_2")
        self.verticalLayout_7.addWidget(self.xoibap_2)
        self.xoidauden_2 = QtWidgets.QCheckBox(self.frame_9)
        self.xoidauden_2.setObjectName("xoidauden_2")
        self.verticalLayout_7.addWidget(self.xoidauden_2)
        self.xoidauphong_2 = QtWidgets.QCheckBox(self.frame_9)
        self.xoidauphong_2.setObjectName("xoidauphong_2")
        self.verticalLayout_7.addWidget(self.xoidauphong_2)
        self.xoigac_2 = QtWidgets.QCheckBox(self.frame_9)
        self.xoigac_2.setObjectName("xoigac_2")
        self.verticalLayout_7.addWidget(self.xoigac_2)
        self.cafe_2 = QtWidgets.QCheckBox(self.frame_9)
        self.cafe_2.setObjectName("cafe_2")
        self.verticalLayout_7.addWidget(self.cafe_2)
        self.nuocam_2 = QtWidgets.QCheckBox(self.frame_9)
        self.nuocam_2.setObjectName("nuocam_2")
        self.verticalLayout_7.addWidget(self.nuocam_2)
        self.nuocchanh_2 = QtWidgets.QCheckBox(self.frame_9)
        self.nuocchanh_2.setObjectName("nuocchanh_2")
        self.verticalLayout_7.addWidget(self.nuocchanh_2)
        self.nuocmia_2 = QtWidgets.QCheckBox(self.frame_9)
        self.nuocmia_2.setObjectName("nuocmia_2")
        self.verticalLayout_7.addWidget(self.nuocmia_2)
        self.nuocrauma_2 = QtWidgets.QCheckBox(self.frame_9)
        self.nuocrauma_2.setObjectName("nuocrauma_2")
        self.verticalLayout_7.addWidget(self.nuocrauma_2)
        self.suachua_2 = QtWidgets.QCheckBox(self.frame_9)
        self.suachua_2.setObjectName("suachua_2")
        self.verticalLayout_7.addWidget(self.suachua_2)
        self.trungcut_2 = QtWidgets.QCheckBox(self.frame_9)
        self.trungcut_2.setObjectName("trungcut_2")
        self.verticalLayout_7.addWidget(self.trungcut_2)
        self.trungga_2 = QtWidgets.QCheckBox(self.frame_9)
        self.trungga_2.setObjectName("trungga_2")
        self.verticalLayout_7.addWidget(self.trungga_2)
        self.trungvit_2 = QtWidgets.QCheckBox(self.frame_9)
        self.trungvit_2.setObjectName("trungvit_2")
        self.verticalLayout_7.addWidget(self.trungvit_2)
        self.banhbonglan_2 = QtWidgets.QCheckBox(self.frame_9)
        self.banhbonglan_2.setObjectName("banhbonglan_2")
        self.verticalLayout_7.addWidget(self.banhbonglan_2)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.Save = QtWidgets.QPushButton(self.frame)
        self.Save.setMaximumSize(QtCore.QSize(80, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Save.setFont(font)
        self.Save.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Save.setStyleSheet("\n"
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
        self.label_14.setText(_translate("MainWindow", "LUNCH"))
        self.label_11.setText(_translate("MainWindow", "ToTal"))
        self.label_12.setText(_translate("MainWindow", "0.0"))
        self.label_13.setText(_translate("MainWindow", "(CALO)"))
        self.gaxaot_2.setText(_translate("MainWindow", "Gà xả ớt (270 Calo)"))
        self.gakho_2.setText(_translate("MainWindow", "Gà kho (300 Calo)"))
        self.mucxao_2.setText(_translate("MainWindow", "Mực xào (180 Calo)"))
        self.suongnuong_2.setText(_translate("MainWindow", "Sườn nướng (110 Calo)"))
        self.suongram_2.setText(_translate("MainWindow", "Sườn ram (150 Calo)"))
        self.thitheoquay_2.setText(_translate("MainWindow", "Thịt heo quay (145 Calo)"))
        self.thitboxao_2.setText(_translate("MainWindow", "Thịt bò xào (200 Calo)"))
        self.thitkhotieu_2.setText(_translate("MainWindow", "Thịt kho tiêu (200 Calo)"))
        self.camoikho_2.setText(_translate("MainWindow", "Cá mòi kho (105 Calo)"))
        self.cari_2.setText(_translate("MainWindow", "Cà ri (278 Calo)"))
        self.bobia_2.setText(_translate("MainWindow", "Bò bía (100 Calo)"))
        self.cabacmachien_2.setText(_translate("MainWindow", "Cá bạc má chiên (135 Calo)"))
        self.cabacmakho_2.setText(_translate("MainWindow", "Cá bạc má kho (167 Calo)"))
        self.cangukho_2.setText(_translate("MainWindow", "Cá ngừ kho (122 Calo)"))
        self.chalua_2.setText(_translate("MainWindow", "Chả lụa (100 Calo)"))
        self.ganheoxao_2.setText(_translate("MainWindow", "Gan heo xào (200 Calo)"))
        self.goikhobo_2.setText(_translate("MainWindow", "Gỏi khô bò (268 Calo)"))
        self.goitom_2.setText(_translate("MainWindow", "Gỏi tôm (147 Calo)"))
        self.khoquaxaotrung_2.setText(_translate("MainWindow", "Khổ qua xào trứng (115 Calo)"))
        self.lapxuongchien_2.setText(_translate("MainWindow", "Lạp xưởng chiên (300 Calo)"))
        self.mucxaothapcam_2.setText(_translate("MainWindow", "Mực xào thập cẩm (135 Calo)"))
        self.boxaomang_2.setText(_translate("MainWindow", "Bò xào măng (105 Calo)"))
        self.boxaonam_2.setText(_translate("MainWindow", "Bò xào nấm (150 Calo)"))
        self.thitkhotrung_2.setText(_translate("MainWindow", "Thịt kho trứng (315 Calo)"))
        self.bunrieu_2.setText(_translate("MainWindow", "Bún riêu (482 Calo)"))
        self.bunbohue_2.setText(_translate("MainWindow", "Bún bò huế (479 Calo)"))
        self.bunthitnuong_2.setText(_translate("MainWindow", "Bún thịt nướng (451 Calo)"))
        self.bunxao_2.setText(_translate("MainWindow", "Bún xào (570 Calo)"))
        self.canhkhoqua_2.setText(_translate("MainWindow", "Canh khổ qua (88 Calo)"))
        self.chaolong_2.setText(_translate("MainWindow", "Cháo lòng (412 Calo)"))
        self.bo_2.setText(_translate("MainWindow", "Bơ (184 Calo)"))
        self.chuoi_2.setText(_translate("MainWindow", "Chuối (35 Calo)"))
        self.thom_2.setText(_translate("MainWindow", "Thơm (17 Calo)"))
        self.xoai_2.setText(_translate("MainWindow", "Xoài (179 Calo)"))
        self.saurieng_2.setText(_translate("MainWindow", "Sầu riêng (28 Calo)"))
        self.mangcut_2.setText(_translate("MainWindow", "Măng cụt (13 Calo)"))
        self.coc_2.setText(_translate("MainWindow", "Cóc (34 Calo)"))
        self.nho_2.setText(_translate("MainWindow", "Nho (68 Calo)"))
        self.duahau_2.setText(_translate("MainWindow", "Dưa Hấu (21 Calo)"))
        self.buoi_2.setText(_translate("MainWindow", "Bưởi (8 Calo)"))
        self.khoailang_2.setText(_translate("MainWindow", "Khoai lang (131 Calo)"))
        self.le_2.setText(_translate("MainWindow", "Lê (91 Calo)"))
        self.bapluoc_2.setText(_translate("MainWindow", "Bắp luộc (192 Calo)"))
        self.khoaitay_2.setText(_translate("MainWindow", "Khoai tây (131 Calo)"))
        self.dauphong_2.setText(_translate("MainWindow", "Đậu phộng (395 Calo)"))
        self.dudu_2.setText(_translate("MainWindow", "Đu đủ (125 Calo)"))
        self.sori_2.setText(_translate("MainWindow", "Sơ ri (14 Calo)"))
        self.cam_2.setText(_translate("MainWindow", "Cam (68 Calo)"))
        self.oi_2.setText(_translate("MainWindow", "Ổi (53 Calo)"))
        self.thanhlong_2.setText(_translate("MainWindow", "Thanh long (255 Calo)"))
        self.chebap_2.setText(_translate("MainWindow", "Chè bắp (325 Calo)"))
        self.chechuoi_2.setText(_translate("MainWindow", "Chè chuối (332 Calo)"))
        self.chedauden_2.setText(_translate("MainWindow", "Chè đậu đen (419 Calo)"))
        self.chedauxanh_2.setText(_translate("MainWindow", "Chè đậu xanh (359 Calo)"))
        self.chenep_2.setText(_translate("MainWindow", "Chè nếp (420 Calo)"))
        self.chetroinuoc_2.setText(_translate("MainWindow", "Chè trôi nước (513 Calo)"))
        self.xoibap_2.setText(_translate("MainWindow", "xôi bắp (322 calo)"))
        self.xoidauden_2.setText(_translate("MainWindow", "Xôi đậu đen (550 Calo)"))
        self.xoidauphong_2.setText(_translate("MainWindow", "Xôi đậu phộng (650 Calo)"))
        self.xoigac_2.setText(_translate("MainWindow", "Xôi gấc (590 Calo)"))
        self.cafe_2.setText(_translate("MainWindow", "Cafe (40 Calo)"))
        self.nuocam_2.setText(_translate("MainWindow", "Nước cam (226 calo)"))
        self.nuocchanh_2.setText(_translate("MainWindow", "Nước chanh (150 Calo)"))
        self.nuocmia_2.setText(_translate("MainWindow", "Nước mía (100 Calo)"))
        self.nuocrauma_2.setText(_translate("MainWindow", "Nước rau má (174 Calo)"))
        self.suachua_2.setText(_translate("MainWindow", "Sữa chua (150 Calo)"))
        self.trungcut_2.setText(_translate("MainWindow", "Trứng cút (17 Calo)"))
        self.trungga_2.setText(_translate("MainWindow", "Trứng gà (58 Calo)"))
        self.trungvit_2.setText(_translate("MainWindow", "Trứng vịt (70 Calo)"))
        self.banhbonglan_2.setText(_translate("MainWindow", "Bánh bông lan (100 Calo)"))
        self.Save.setText(_translate("MainWindow", "DONE"))
import MENU_rc

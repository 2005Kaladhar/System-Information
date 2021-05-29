# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'systemFramezXiVwW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 604)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.CentralFrameBase = QFrame(self.centralwidget)
        self.CentralFrameBase.setObjectName(u"CentralFrameBase")
        self.CentralFrameBase.setStyleSheet(u"border-image: url(:/newPrefix/phtoreduced.jpg);")
        self.CentralFrameBase.setFrameShape(QFrame.StyledPanel)
        self.CentralFrameBase.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.CentralFrameBase)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TitleBar_2 = QFrame(self.CentralFrameBase)
        self.TitleBar_2.setObjectName(u"TitleBar_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar_2.sizePolicy().hasHeightForWidth())
        self.TitleBar_2.setSizePolicy(sizePolicy)
        self.TitleBar_2.setMinimumSize(QSize(0, 0))
        self.TitleBar_2.setMaximumSize(QSize(16777215, 30))
        self.TitleBar_2.setStyleSheet(u"QFrame{\n"
"\n"
"	border-image:none;\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 198), stop:1 rgba(0, 0, 0, 194));\n"
"\n"
"\n"
"}")
        self.TitleBar_2.setFrameShape(QFrame.StyledPanel)
        self.TitleBar_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.TitleBar_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.TitleBar_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setCursor(QCursor(Qt.SizeAllCursor))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.TitleBar_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 25))
        self.frame_3.setMaximumSize(QSize(100, 16777215))
        self.frame_3.setStyleSheet(u"border-image:none;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 0, 0, 0)
        self.Minimizebtn = QPushButton(self.frame_3)
        self.Minimizebtn.setObjectName(u"Minimizebtn")
        sizePolicy1.setHeightForWidth(self.Minimizebtn.sizePolicy().hasHeightForWidth())
        self.Minimizebtn.setSizePolicy(sizePolicy1)
        self.Minimizebtn.setMaximumSize(QSize(15, 15))
        self.Minimizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Minimizebtn)

        self.Maximizebtn = QPushButton(self.frame_3)
        self.Maximizebtn.setObjectName(u"Maximizebtn")
        sizePolicy1.setHeightForWidth(self.Maximizebtn.sizePolicy().hasHeightForWidth())
        self.Maximizebtn.setSizePolicy(sizePolicy1)
        self.Maximizebtn.setMaximumSize(QSize(15, 15))
        self.Maximizebtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 170, 0);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(85, 170, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.Maximizebtn)

        self.CloseButton = QPushButton(self.frame_3)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy1.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy1)
        self.CloseButton.setMaximumSize(QSize(15, 15))
        self.CloseButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(235, 0, 16);\n"
"border-radius:7px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.CloseButton)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.TitleBar_2, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.CentralFrameBase)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_2 = QHBoxLayout(self.page)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainContentFrame = QFrame(self.page)
        self.MainContentFrame.setObjectName(u"MainContentFrame")
        self.MainContentFrame.setStyleSheet(u"QFrame{\n"
"border-image:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 70), stop:1 rgba(0, 0, 0, 70));\n"
"}")
        self.MainContentFrame.setFrameShape(QFrame.StyledPanel)
        self.MainContentFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.MainContentFrame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(6)
        self.NetworkAndDisk = QFrame(self.MainContentFrame)
        self.NetworkAndDisk.setObjectName(u"NetworkAndDisk")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.NetworkAndDisk.sizePolicy().hasHeightForWidth())
        self.NetworkAndDisk.setSizePolicy(sizePolicy2)
        self.NetworkAndDisk.setMinimumSize(QSize(232, 286))
        self.NetworkAndDisk.setFrameShape(QFrame.StyledPanel)
        self.NetworkAndDisk.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.NetworkAndDisk)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.NetworketcFrame = QFrame(self.NetworkAndDisk)
        self.NetworketcFrame.setObjectName(u"NetworketcFrame")
        self.NetworketcFrame.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"border-radius:10px;\n"
"}")
        self.NetworketcFrame.setFrameShape(QFrame.StyledPanel)
        self.NetworketcFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.NetworketcFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 1, -1, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, -1, -1, -1)
        self.frame_7 = QFrame(self.NetworketcFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QFrame{\n"
"border-radius:10px;\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.downloadSpeed = QLabel(self.frame_7)
        self.downloadSpeed.setObjectName(u"downloadSpeed")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.downloadSpeed.sizePolicy().hasHeightForWidth())
        self.downloadSpeed.setSizePolicy(sizePolicy3)
        self.downloadSpeed.setMinimumSize(QSize(205, 0))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(11)
        self.downloadSpeed.setFont(font)
        self.downloadSpeed.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}")
        self.downloadSpeed.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.downloadSpeed)


        self.gridLayout_5.addWidget(self.frame_7, 5, 0, 1, 1)

        self.label_3 = QLabel(self.NetworketcFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 1)

        self.frame_5 = QFrame(self.NetworketcFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"}")

        self.horizontalLayout_20.addWidget(self.label_8)

        self.internetSpeed = QPushButton(self.frame_5)
        self.internetSpeed.setObjectName(u"internetSpeed")
        sizePolicy1.setHeightForWidth(self.internetSpeed.sizePolicy().hasHeightForWidth())
        self.internetSpeed.setSizePolicy(sizePolicy1)
        self.internetSpeed.setMinimumSize(QSize(41, 41))
        self.internetSpeed.setStyleSheet(u"QPushButton{\n"
"\n"
"border-radius:15px;\n"
"	border-image: url(:/newPrefix/internetSpee.png);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"\n"
"	border-image: url(:/newPrefix/internetSpee2.png);\n"
"\n"
"}")

        self.horizontalLayout_20.addWidget(self.internetSpeed)


        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.NetworketcFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"border-radius:10px;\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.UploadSpeed = QLabel(self.frame_6)
        self.UploadSpeed.setObjectName(u"UploadSpeed")
        sizePolicy3.setHeightForWidth(self.UploadSpeed.sizePolicy().hasHeightForWidth())
        self.UploadSpeed.setSizePolicy(sizePolicy3)
        self.UploadSpeed.setMinimumSize(QSize(201, 0))
        self.UploadSpeed.setFont(font)
        self.UploadSpeed.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255, 255, 0);\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}")
        self.UploadSpeed.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.UploadSpeed)


        self.gridLayout_5.addWidget(self.frame_6, 3, 0, 1, 1)

        self.label_2 = QLabel(self.NetworketcFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(78, 0))
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)

        self.sampleprogressBar = QProgressBar(self.NetworketcFrame)
        self.sampleprogressBar.setObjectName(u"sampleprogressBar")
        sizePolicy1.setHeightForWidth(self.sampleprogressBar.sizePolicy().hasHeightForWidth())
        self.sampleprogressBar.setSizePolicy(sizePolicy1)
        self.sampleprogressBar.setStyleSheet(u"QProgressBar{\n"
"border-image:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"\n"
"}")
        self.sampleprogressBar.setValue(24)

        self.gridLayout_5.addWidget(self.sampleprogressBar, 1, 0, 1, 1)


        self.horizontalLayout_12.addLayout(self.gridLayout_5)


        self.verticalLayout.addWidget(self.NetworketcFrame)

        self.NetworketcFrame_2 = QFrame(self.NetworkAndDisk)
        self.NetworketcFrame_2.setObjectName(u"NetworketcFrame_2")
        self.NetworketcFrame_2.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"\n"
"border-radius:10px;\n"
"}")
        self.NetworketcFrame_2.setFrameShape(QFrame.StyledPanel)
        self.NetworketcFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.NetworketcFrame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, -1, -1, -1)
        self.label_4 = QLabel(self.NetworketcFrame_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"}")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.NetworketcFrame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.gridLayout_6.addWidget(self.label_5, 1, 0, 1, 1)

        self.cdrivebar = QProgressBar(self.NetworketcFrame_2)
        self.cdrivebar.setObjectName(u"cdrivebar")
        sizePolicy2.setHeightForWidth(self.cdrivebar.sizePolicy().hasHeightForWidth())
        self.cdrivebar.setSizePolicy(sizePolicy2)
        self.cdrivebar.setMinimumSize(QSize(0, 25))
        self.cdrivebar.setStyleSheet(u"QProgressBar{\n"
"border-image:none;\n"
"border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"	text-align:right;\n"
"	background-color: rgb(16, 16, 16);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"margin:4px;\n"
"border-radius:5px;\n"
"	background-color: rgb(255, 255, 0);\n"
"	background-color: rgb(255, 170, 0);\n"
"\n"
"\n"
"}")
        self.cdrivebar.setMaximum(90)
        self.cdrivebar.setValue(1)
        self.cdrivebar.setAlignment(Qt.AlignCenter)
        self.cdrivebar.setOrientation(Qt.Horizontal)
        self.cdrivebar.setInvertedAppearance(False)
        self.cdrivebar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_6.addWidget(self.cdrivebar, 2, 0, 1, 1)

        self.label_6 = QLabel(self.NetworketcFrame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.label_6, 3, 0, 1, 1)

        self.ddrivebar = QProgressBar(self.NetworketcFrame_2)
        self.ddrivebar.setObjectName(u"ddrivebar")
        sizePolicy2.setHeightForWidth(self.ddrivebar.sizePolicy().hasHeightForWidth())
        self.ddrivebar.setSizePolicy(sizePolicy2)
        self.ddrivebar.setMinimumSize(QSize(0, 25))
        self.ddrivebar.setStyleSheet(u"QProgressBar{\n"
"border-image:none;\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"	text-align:right;\n"
"	background-color: rgb(16, 16, 16);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"margin:4px;\n"
"border-radius:5px;\n"
"	background-color: rgb(255, 255, 0);\n"
"	background-color: rgb(255, 170, 0);\n"
"\n"
"}")
        self.ddrivebar.setMaximum(90)
        self.ddrivebar.setValue(1)
        self.ddrivebar.setAlignment(Qt.AlignCenter)
        self.ddrivebar.setOrientation(Qt.Horizontal)
        self.ddrivebar.setInvertedAppearance(False)
        self.ddrivebar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_6.addWidget(self.ddrivebar, 4, 0, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_6)


        self.verticalLayout.addWidget(self.NetworketcFrame_2)


        self.gridLayout_7.addWidget(self.NetworkAndDisk, 0, 0, 1, 1)

        self.PaddinFrame = QFrame(self.MainContentFrame)
        self.PaddinFrame.setObjectName(u"PaddinFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.PaddinFrame.sizePolicy().hasHeightForWidth())
        self.PaddinFrame.setSizePolicy(sizePolicy6)
        self.PaddinFrame.setMinimumSize(QSize(551, 0))
        self.PaddinFrame.setStyleSheet(u"background-color: rgb(76, 76, 76);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.PaddinFrame.setFrameShape(QFrame.StyledPanel)
        self.PaddinFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.PaddinFrame)
        self.horizontalLayout_14.setSpacing(2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 0, 5, 5)
        self.frame_4 = QFrame(self.PaddinFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(44)
        self.gridLayout_8.setVerticalSpacing(17)
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(0, 46))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"border-radius:20px;\n"
"\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(0, 36))
        font1 = QFont()
        font1.setFamily(u"Californian FB")
        font1.setPointSize(30)
        font1.setItalic(False)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_7)


        self.gridLayout_8.addWidget(self.frame_8, 0, 0, 1, 3)

        self.systeminformationframe = QFrame(self.frame_4)
        self.systeminformationframe.setObjectName(u"systeminformationframe")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.systeminformationframe.sizePolicy().hasHeightForWidth())
        self.systeminformationframe.setSizePolicy(sizePolicy7)
        self.systeminformationframe.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 70), stop:1 rgba(0, 0, 0, 70));\n"
"border-radius:10px;")
        self.systeminformationframe.setFrameShape(QFrame.StyledPanel)
        self.systeminformationframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.systeminformationframe)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.systemInformationHeading = QLabel(self.systeminformationframe)
        self.systemInformationHeading.setObjectName(u"systemInformationHeading")
        sizePolicy.setHeightForWidth(self.systemInformationHeading.sizePolicy().hasHeightForWidth())
        self.systemInformationHeading.setSizePolicy(sizePolicy)
        self.systemInformationHeading.setMinimumSize(QSize(249, 34))
        self.systemInformationHeading.setStyleSheet(u"QLabel{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.523, y1:1, x2:0.523, y2:0, stop:0 rgba(0, 48, 59, 61), stop:1 rgba(0, 93, 115, 203));\n"
"\n"
"}")
        self.systemInformationHeading.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.systemInformationHeading, 0, 0, 1, 1)

        self.systemInformation = QTextEdit(self.systeminformationframe)
        self.systemInformation.setObjectName(u"systemInformation")
        font2 = QFont()
        font2.setFamily(u"Lucida Fax")
        font2.setPointSize(12)
        self.systemInformation.setFont(font2)
        self.systemInformation.setStyleSheet(u"QTextEdit{\n"
"border-radius:10px;\n"
"border-image:none;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 131), stop:1 rgba(0, 0, 0, 128));\n"
"\n"
"}")
        self.systemInformation.setFrameShape(QFrame.Box)
        self.systemInformation.setFrameShadow(QFrame.Raised)
        self.systemInformation.setLineWidth(13)
        self.systemInformation.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.systemInformation.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.systemInformation.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.systemInformation.setReadOnly(True)

        self.gridLayout_9.addWidget(self.systemInformation, 1, 0, 1, 1)


        self.horizontalLayout_19.addLayout(self.gridLayout_9)


        self.gridLayout_8.addWidget(self.systeminformationframe, 1, 0, 1, 1)

        self.IconFrame = QFrame(self.frame_4)
        self.IconFrame.setObjectName(u"IconFrame")
        sizePolicy1.setHeightForWidth(self.IconFrame.sizePolicy().hasHeightForWidth())
        self.IconFrame.setSizePolicy(sizePolicy1)
        self.IconFrame.setMinimumSize(QSize(190, 190))
        self.IconFrame.setStyleSheet(u"border-image: url(:/newPrefix/Alienware Invader Icon 03.ico);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.IconFrame.setFrameShape(QFrame.StyledPanel)
        self.IconFrame.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.IconFrame, 1, 1, 1, 2)


        self.horizontalLayout_16.addLayout(self.gridLayout_8)


        self.horizontalLayout_14.addWidget(self.frame_4)


        self.gridLayout_7.addWidget(self.PaddinFrame, 0, 1, 1, 1)

        self.ProgressFrame = QFrame(self.MainContentFrame)
        self.ProgressFrame.setObjectName(u"ProgressFrame")
        sizePolicy.setHeightForWidth(self.ProgressFrame.sizePolicy().hasHeightForWidth())
        self.ProgressFrame.setSizePolicy(sizePolicy)
        self.ProgressFrame.setMinimumSize(QSize(790, 265))
        self.ProgressFrame.setStyleSheet(u"border-image:NOne;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.ProgressFrame.setFrameShape(QFrame.StyledPanel)
        self.ProgressFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.ProgressFrame)
        self.horizontalLayout_11.setSpacing(37)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, -1, 14, -1)
        self.CPU = QFrame(self.ProgressFrame)
        self.CPU.setObjectName(u"CPU")
        sizePolicy1.setHeightForWidth(self.CPU.sizePolicy().hasHeightForWidth())
        self.CPU.setSizePolicy(sizePolicy1)
        self.CPU.setMinimumSize(QSize(248, 248))
        self.CPU.setStyleSheet(u"QFrame{\n"
"border-radius: 124px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.249 rgba(31, 244, 75, 239), stop:0.25 rgba(0, 0, 0, 89));\n"
"}")
        self.CPU.setFrameShape(QFrame.NoFrame)
        self.CPU.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.CPU)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(7, 7, 7, 7)
        self.TitleFrame = QFrame(self.CPU)
        self.TitleFrame.setObjectName(u"TitleFrame")
        self.TitleFrame.setStyleSheet(u"QFrame{\n"
"border-radius:117px;\n"
"	\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.491525 rgba(93, 93, 93, 255), stop:0.80226 rgba(73, 73, 73, 255), stop:0.949153 rgba(45, 45, 45, 255), stop:0.988701 rgba(0, 0, 0, 255));\n"
"\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.0603015 rgba(48, 48, 107, 255), stop:0.959799 rgba(29, 29, 76, 255), stop:1 rgba(0, 0, 75, 255));\n"
"}")
        self.TitleFrame.setFrameShape(QFrame.StyledPanel)
        self.TitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.TitleFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(25, 48, 21, 26)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(11, -1, -1, -1)
        self.loadingLabel = QLabel(self.TitleFrame)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(213, 213, 213);\n"
"\n"
"}")

        self.gridLayout_2.addWidget(self.loadingLabel, 1, 0, 1, 1)

        self.CPUpercent = QLabel(self.TitleFrame)
        self.CPUpercent.setObjectName(u"CPUpercent")
        self.CPUpercent.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(244, 244, 244);\n"
"}")

        self.gridLayout_2.addWidget(self.CPUpercent, 0, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_2)


        self.horizontalLayout_4.addWidget(self.TitleFrame)


        self.horizontalLayout_11.addWidget(self.CPU)

        self.RAM = QFrame(self.ProgressFrame)
        self.RAM.setObjectName(u"RAM")
        sizePolicy1.setHeightForWidth(self.RAM.sizePolicy().hasHeightForWidth())
        self.RAM.setSizePolicy(sizePolicy1)
        self.RAM.setMinimumSize(QSize(248, 248))
        self.RAM.setStyleSheet(u"QFrame{\n"
"border-radius: 124px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.249 rgba(31, 244, 75, 239), stop:0.25 rgba(0, 0, 0, 89));\n"
"}")
        self.RAM.setFrameShape(QFrame.NoFrame)
        self.RAM.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.RAM)
        self.horizontalLayout_7.setSpacing(7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(7, 7, 7, 7)
        self.TitleFrame_2 = QFrame(self.RAM)
        self.TitleFrame_2.setObjectName(u"TitleFrame_2")
        self.TitleFrame_2.setStyleSheet(u"QFrame{\n"
"border-radius:117px;\n"
"	\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.491525 rgba(93, 93, 93, 255), stop:0.80226 rgba(73, 73, 73, 255), stop:0.949153 rgba(45, 45, 45, 255), stop:0.988701 rgba(0, 0, 0, 255));\n"
"\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.0603015 rgba(48, 48, 107, 255), stop:0.959799 rgba(29, 29, 76, 255), stop:1 rgba(0, 0, 75, 255));\n"
"}")
        self.TitleFrame_2.setFrameShape(QFrame.StyledPanel)
        self.TitleFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.TitleFrame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(25, 48, 21, 26)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(11, -1, -1, -1)
        self.loadingLabel_2 = QLabel(self.TitleFrame_2)
        self.loadingLabel_2.setObjectName(u"loadingLabel_2")
        self.loadingLabel_2.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(213, 213, 213);\n"
"\n"
"}")

        self.gridLayout_3.addWidget(self.loadingLabel_2, 1, 0, 1, 1)

        self.RAMpercent = QLabel(self.TitleFrame_2)
        self.RAMpercent.setObjectName(u"RAMpercent")
        self.RAMpercent.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(244, 244, 244);\n"
"}")

        self.gridLayout_3.addWidget(self.RAMpercent, 0, 0, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_3)


        self.horizontalLayout_7.addWidget(self.TitleFrame_2)


        self.horizontalLayout_11.addWidget(self.RAM)

        self.SWAP = QFrame(self.ProgressFrame)
        self.SWAP.setObjectName(u"SWAP")
        sizePolicy1.setHeightForWidth(self.SWAP.sizePolicy().hasHeightForWidth())
        self.SWAP.setSizePolicy(sizePolicy1)
        self.SWAP.setMinimumSize(QSize(248, 248))
        self.SWAP.setStyleSheet(u"QFrame{\n"
"border-radius: 124px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.249 rgba(31, 244, 75, 239), stop:0.25 rgba(0, 0, 0, 89));\n"
"}")
        self.SWAP.setFrameShape(QFrame.NoFrame)
        self.SWAP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.SWAP)
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(7, 7, 7, 7)
        self.TitleFrame_3 = QFrame(self.SWAP)
        self.TitleFrame_3.setObjectName(u"TitleFrame_3")
        self.TitleFrame_3.setStyleSheet(u"QFrame{\n"
"border-radius:117px;\n"
"	\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.491525 rgba(93, 93, 93, 255), stop:0.80226 rgba(73, 73, 73, 255), stop:0.949153 rgba(45, 45, 45, 255), stop:0.988701 rgba(0, 0, 0, 255));\n"
"\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.0603015 rgba(48, 48, 107, 255), stop:0.959799 rgba(29, 29, 76, 255), stop:1 rgba(0, 0, 75, 255));\n"
"}")
        self.TitleFrame_3.setFrameShape(QFrame.StyledPanel)
        self.TitleFrame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.TitleFrame_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(25, 48, 21, 26)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(11, -1, -1, -1)
        self.loadingLabel_3 = QLabel(self.TitleFrame_3)
        self.loadingLabel_3.setObjectName(u"loadingLabel_3")
        self.loadingLabel_3.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(213, 213, 213);\n"
"\n"
"}")

        self.gridLayout_4.addWidget(self.loadingLabel_3, 1, 0, 1, 1)

        self.SwapPercent = QLabel(self.TitleFrame_3)
        self.SwapPercent.setObjectName(u"SwapPercent")
        self.SwapPercent.setStyleSheet(u"QLabel{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"	color: rgb(244, 244, 244);\n"
"}")

        self.gridLayout_4.addWidget(self.SwapPercent, 0, 0, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_4)


        self.horizontalLayout_9.addWidget(self.TitleFrame_3)


        self.horizontalLayout_11.addWidget(self.SWAP)


        self.gridLayout_7.addWidget(self.ProgressFrame, 1, 0, 1, 2)


        self.horizontalLayout_15.addLayout(self.gridLayout_7)


        self.horizontalLayout_2.addWidget(self.MainContentFrame)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.horizontalLayout_22.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.CentralFrameBase)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.Minimizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Minimizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.Maximizebtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Maximize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Maximizebtn.setText("")
#if QT_CONFIG(tooltip)
        self.CloseButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Close</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.CloseButton.setText("")
        self.downloadSpeed.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Upload</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Network</span></p></body></html>", None))
        self.internetSpeed.setText("")
        self.UploadSpeed.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Download</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Disk Usage</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">C:/</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">E:/</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">Machine Processes...</span></p><p align=\"center\"><span style=\" vertical-align:super;\"><br/></span><span style=\" font-size:36pt; font-weight:600; vertical-align:super;\">&quot; </span><span style=\" font-size:36pt; vertical-align:super;\">Do What You Can, With What You Have, And Where You Are</span><span style=\" font-size:36pt; font-weight:600; vertical-align:super;\">&quot;</span></p></body></html>", None))
        self.systemInformationHeading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">System Information</span></p></body></html>", None))
        self.systemInformation.setDocumentTitle(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.systemInformation.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><title>System Information</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Fax'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">Platform</span><span style=\" font-size:10pt;\">        - Windows 10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">Version</span><span style=\" font-size:10pt;\"> 	      - systemversion</span></p>\n"
"<p style=\" margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">Architecture</span><span style=\" font-size:10pt;\">  - architecture</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">Processor</span><span style=\" font-size:10pt;\">       - processor</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">HostName</span><span style=\" font-size:10pt;\">      - hostname</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:1"
                        "0pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">Ip Address </span><span style=\" font-size:10pt;\">    - ipadd</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">RAM (total) </span><span style=\" font-size:10pt;\">    - ram</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">MAC Add.</span><span style=\" font-size:10pt;\">       - mcaddress </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">.</span><span style=\" font-size:10pt; text-decoration: underline;\">PC Name  </span><span style=\" font-size:1"
                        "0pt;\">      - nodename</span></p></body></html>", None))
        self.loadingLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">CPU Usage</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">%</span></p></body></html>", None))
        self.CPUpercent.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">25</span><span style=\" font-size:24pt; font-weight:600; vertical-align:super;\">%</span></p></body></html>", None))
        self.loadingLabel_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">RAM Used</span><span style=\" font-size:11pt; font-weight:600; vertical-align:super;\">%</span></p></body></html>", None))
        self.RAMpercent.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">25</span><span style=\" font-size:24pt; font-weight:600; vertical-align:super;\">%</span></p></body></html>", None))
        self.loadingLabel_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">SWAP Used</span><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">%</span></p></body></html>", None))
        self.SwapPercent.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">25</span><span style=\" font-size:24pt; font-weight:600; vertical-align:super;\">%</span></p></body></html>", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(373, 425)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_userName = QLabel(self.centralwidget)
        self.label_userName.setObjectName(u"label_userName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_userName.sizePolicy().hasHeightForWidth())
        self.label_userName.setSizePolicy(sizePolicy1)
        self.label_userName.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_userName.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_userName)

        self.lineEdit_userName = QLineEdit(self.centralwidget)
        self.lineEdit_userName.setObjectName(u"lineEdit_userName")
        self.lineEdit_userName.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_userName.sizePolicy().hasHeightForWidth())
        self.lineEdit_userName.setSizePolicy(sizePolicy2)
        self.lineEdit_userName.setMinimumSize(QSize(0, 30))
        self.lineEdit_userName.setFont(font)
        self.lineEdit_userName.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_userName.setAutoFillBackground(False)
        self.lineEdit_userName.setFrame(False)
        self.lineEdit_userName.setEchoMode(QLineEdit.Normal)
        self.lineEdit_userName.setAlignment(Qt.AlignCenter)
        self.lineEdit_userName.setClearButtonEnabled(False)

        self.horizontalLayout_3.addWidget(self.lineEdit_userName)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(0, 150))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(1)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_fileCnt = QLabel(self.frame)
        self.label_fileCnt.setObjectName(u"label_fileCnt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_fileCnt.sizePolicy().hasHeightForWidth())
        self.label_fileCnt.setSizePolicy(sizePolicy3)
        self.label_fileCnt.setFont(font)
        self.label_fileCnt.setTextFormat(Qt.PlainText)
        self.label_fileCnt.setAlignment(Qt.AlignCenter)
        self.label_fileCnt.setWordWrap(False)
        self.label_fileCnt.setMargin(0)

        self.verticalLayout_4.addWidget(self.label_fileCnt)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_loadFile = QPushButton(self.frame)
        self.pushButton_loadFile.setObjectName(u"pushButton_loadFile")
        sizePolicy2.setHeightForWidth(self.pushButton_loadFile.sizePolicy().hasHeightForWidth())
        self.pushButton_loadFile.setSizePolicy(sizePolicy2)
        self.pushButton_loadFile.setMinimumSize(QSize(0, 50))
        self.pushButton_loadFile.setFont(font)
        self.pushButton_loadFile.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_loadFile)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_local = QRadioButton(self.centralwidget)
        self.radioButton_local.setObjectName(u"radioButton_local")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.radioButton_local.sizePolicy().hasHeightForWidth())
        self.radioButton_local.setSizePolicy(sizePolicy4)
        self.radioButton_local.setMinimumSize(QSize(0, 50))
        self.radioButton_local.setFont(font)
        self.radioButton_local.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_local)

        self.radioButton_cloud = QRadioButton(self.centralwidget)
        self.radioButton_cloud.setObjectName(u"radioButton_cloud")
        sizePolicy4.setHeightForWidth(self.radioButton_cloud.sizePolicy().hasHeightForWidth())
        self.radioButton_cloud.setSizePolicy(sizePolicy4)
        self.radioButton_cloud.setMinimumSize(QSize(0, 50))
        self.radioButton_cloud.setFont(font)
        self.radioButton_cloud.setChecked(False)

        self.horizontalLayout.addWidget(self.radioButton_cloud)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(10)
        self.tabWidget.setFont(font2)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_default = QWidget()
        self.tab_default.setObjectName(u"tab_default")
        self.gridLayout_2 = QGridLayout(self.tab_default)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.tab_default)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_default, "")
        self.tab_ecloud = QWidget()
        self.tab_ecloud.setObjectName(u"tab_ecloud")
        self.tabWidget.addTab(self.tab_ecloud, "")

        self.gridLayout_3.addWidget(self.tabWidget, 3, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy5)
        self.pushButton_start.setMinimumSize(QSize(0, 50))
        self.pushButton_start.setFont(font)

        self.gridLayout.addWidget(self.pushButton_start, 0, 0, 1, 1)

        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy2.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy2)
        self.pushButton_clear.setMinimumSize(QSize(0, 50))
        self.pushButton_clear.setFont(font)

        self.gridLayout.addWidget(self.pushButton_clear, 0, 1, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy5.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy5)
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.pushButton_start.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7968\u636e\u5c0f\u5de5\u5177", None))
        self.label_userName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">\u8fd9\u7968\u636e\u662f\u8c01\u7684\u54c8(\u5fc5\u586b)\uff1a*</span></p></body></html>", None))
        self.lineEdit_userName.setInputMask("")
        self.lineEdit_userName.setText("")
        self.lineEdit_userName.setPlaceholderText("")
        self.label_fileCnt.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u9700\u8981\u5904\u7406\u7684\u6587\u4ef6\u6570\u4e3a\uff1a0\u4e2a", None))
        self.pushButton_loadFile.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u6dfb\u52a0\u6587\u4ef6", None))
        self.radioButton_local.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u8bc6\u522b", None))
        self.radioButton_cloud.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u7aef\u8bc6\u522b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u4f7f\u7528\u521b\u65b0\u4e2d\u5fc3\u670d\u52a1\u5668", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_default), QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u670d\u52a1\u5668", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ecloud), QCoreApplication.translate("MainWindow", u"\u79fb\u52a8\u4e91OCR", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5904\u7406", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6587\u4ef6", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1203, 805)
        self.gridLayout_3 = QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit_name = QLineEdit(Dialog)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_name)

        self.listWidget_files = QListWidget(Dialog)
        self.listWidget_files.setObjectName(u"listWidget_files")

        self.verticalLayout_3.addWidget(self.listWidget_files)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.radioButton_local = QRadioButton(Dialog)
        self.radioButton_local.setObjectName(u"radioButton_local")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_local.sizePolicy().hasHeightForWidth())
        self.radioButton_local.setSizePolicy(sizePolicy)
        self.radioButton_local.setMinimumSize(QSize(0, 50))
        self.radioButton_local.setFont(font)
        self.radioButton_local.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_local, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.radioButton_cloud = QRadioButton(Dialog)
        self.radioButton_cloud.setObjectName(u"radioButton_cloud")
        sizePolicy.setHeightForWidth(self.radioButton_cloud.sizePolicy().hasHeightForWidth())
        self.radioButton_cloud.setSizePolicy(sizePolicy)
        self.radioButton_cloud.setMinimumSize(QSize(0, 50))
        self.radioButton_cloud.setFont(font)
        self.radioButton_cloud.setChecked(False)

        self.gridLayout.addWidget(self.radioButton_cloud, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(10)
        self.tabWidget.setFont(font1)
        self.tab_default = QWidget()
        self.tab_default.setObjectName(u"tab_default")
        self.gridLayout_2 = QGridLayout(self.tab_default)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.tab_default)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_default, "")
        self.tab_ecloud = QWidget()
        self.tab_ecloud.setObjectName(u"tab_ecloud")
        self.tabWidget.addTab(self.tab_ecloud, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.pushButton_export = QPushButton(Dialog)
        self.pushButton_export.setObjectName(u"pushButton_export")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_export.sizePolicy().hasHeightForWidth())
        self.pushButton_export.setSizePolicy(sizePolicy1)
        self.pushButton_export.setMinimumSize(QSize(0, 66))
        self.pushButton_export.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_export)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_loadFile = QPushButton(Dialog)
        self.pushButton_loadFile.setObjectName(u"pushButton_loadFile")
        sizePolicy1.setHeightForWidth(self.pushButton_loadFile.sizePolicy().hasHeightForWidth())
        self.pushButton_loadFile.setSizePolicy(sizePolicy1)
        self.pushButton_loadFile.setMinimumSize(QSize(0, 66))
        self.pushButton_loadFile.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_loadFile)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_start = QPushButton(Dialog)
        self.pushButton_start.setObjectName(u"pushButton_start")
        sizePolicy1.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy1)
        self.pushButton_start.setMinimumSize(QSize(0, 66))
        self.pushButton_start.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_start)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_reset = QPushButton(Dialog)
        self.pushButton_reset.setObjectName(u"pushButton_reset")
        sizePolicy1.setHeightForWidth(self.pushButton_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_reset.setSizePolicy(sizePolicy1)
        self.pushButton_reset.setMinimumSize(QSize(0, 30))
        self.pushButton_reset.setFont(font)

        self.verticalLayout_2.addWidget(self.pushButton_reset)

        self.pushButton_exit = QPushButton(Dialog)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        self.pushButton_exit.setMinimumSize(QSize(0, 30))
        self.pushButton_exit.setFont(font)

        self.verticalLayout_2.addWidget(self.pushButton_exit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)


        self.retranslateUi(Dialog)
        self.pushButton_exit.clicked.connect(Dialog.close)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_start.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lineEdit_name.setText(QCoreApplication.translate("Dialog", u"\u6b64\u5904\u8f93\u5165\u59d3\u540d", None))
        self.radioButton_local.setText(QCoreApplication.translate("Dialog", u"\u672c\u5730\u8bc6\u522b", None))
        self.radioButton_cloud.setText(QCoreApplication.translate("Dialog", u"\u4e91\u7aef\u8bc6\u522b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u9ed8\u8ba4\u4f7f\u7528\u521b\u65b0\u4e2d\u5fc3\u670d\u52a1\u5668", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_default), QCoreApplication.translate("Dialog", u"\u9ed8\u8ba4\u670d\u52a1\u5668", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ecloud), QCoreApplication.translate("Dialog", u"\u79fb\u52a8\u4e91OCR", None))
        self.pushButton_export.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u51faexcel", None))
        self.pushButton_loadFile.setText(QCoreApplication.translate("Dialog", u"\u52a0\u8f7d\u6587\u4ef6", None))
        self.pushButton_start.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb", None))
        self.pushButton_reset.setText(QCoreApplication.translate("Dialog", u"\u91cd\u7f6e", None))
        self.pushButton_exit.setText(QCoreApplication.translate("Dialog", u"\u9000\u51fa", None))
    # retranslateUi


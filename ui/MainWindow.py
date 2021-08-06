'''
Author: mukangt
Date: 2021-07-13 17:45:15
LastEditors: mukangt
LastEditTime: 2021-08-06 16:03:32
Description: 
'''

from PySide6 import QtCore, QtWidgets, QtGui
import os

# from .Ui_Dialog import Ui_Dialog
from .Ui_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    # initialize signals
    sigFileUpdated = QtCore.Signal(list)
    sigFileNumChanged = QtCore.Signal(int)
    sigUserNameChanged = QtCore.Signal(str)
    sigProgressBarChanged = QtCore.Signal(int)
    sigStartClicked = QtCore.Signal(dict)

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('票据报销小工具')

        # saving filenames & invoice info
        # self.fileInfo = {'dirname': '', 'files': {}}

        self.initUI()

        self.bindSigSlot()

    def initUI(self):

        # reading init data from my.ini
        appDir = QtCore.QCoreApplication.applicationDirPath()
        iniPath = os.path.join(appDir, 'my.ini')
        self.settings = QtCore.QSettings(iniPath, QtCore.QSettings.IniFormat)
        self.settings.beginGroup('MAIN')
        self.userName = self.settings.value('UserName', '').__str__()
        self.settings.endGroup()

        # initialize user name input line
        if self.userName == '':
            self.ui.lineEdit_userName.setPlaceholderText('请输入姓名')
            self.ui.lineEdit_userName.setStyleSheet(
                "QLineEdit{border:1px solid rgb(255, 0, 0);}")
        else:
            self.ui.lineEdit_userName.setText(self.userName)
            self.ui.lineEdit_userName.setStyleSheet(
                "QLineEdit{border:1px solid rgb(0, 0, 0);}")

        # reset progress bar
        self.ui.progressBar.setValue(0)

        # initialize radio button
        self.radioButtonGroup = QtWidgets.QButtonGroup(self)
        self.radioButtonGroup.addButton(self.ui.radioButton_local, 0)
        self.radioButtonGroup.addButton(self.ui.radioButton_cloud, 1)
        self.ui.radioButton_local.setChecked(True)

        # initialize tab widget
        self.ui.tabWidget.setEnabled(False)
        self.ui.tabWidget.setCurrentIndex(0)

        # remove ocr choice
        self.ui.radioButton_local.hide()
        self.ui.radioButton_cloud.hide()
        self.ui.tabWidget.hide()

        # resize windows
        self.setFixedSize(400, 300)

    # def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
    #     print(self.geometry().width(), self.geometry().height())
    #     super().resizeEvent(event)

    def bindSigSlot(self):

        # radio button & tab widget
        self.radioButtonGroup.idClicked.connect(self.slotSetEnabledTabWidget)

        # load files
        self.ui.pushButton_loadFile.clicked.connect(self.slotLoadFile)

        # start process
        self.ui.pushButton_start.clicked.connect(self.slotStart)

        # clear process
        self.ui.pushButton_clear.clicked.connect(self.slotClear)

        # file number change
        self.sigFileNumChanged.connect(self.slotLabelFileCntUpdate)

        # progress bar change
        self.sigProgressBarChanged.connect(self.slotProgressBarUpdate)

        # loaded files updated
        self.sigFileUpdated.connect(self.slotFileUpdate)

        # user name changed
        self.sigUserNameChanged.connect(self.slotUserNameSettings)

    @QtCore.Slot(str)
    def slotUserNameSettings(self, username: str) -> None:
        self.settings.beginGroup('MAIN')
        self.settings.setValue('UserName', username)
        self.settings.endGroup()

    @QtCore.Slot(int)
    def slotProgressBarUpdate(self, value: int) -> None:
        self.ui.progressBar.setValue(value)

    @QtCore.Slot(int)
    def slotLabelFileCntUpdate(self, num: int) -> None:
        self.ui.label_fileCnt.setText('当前需要处理的文件数为：{}个'.format(num))

    @QtCore.Slot(int)
    def slotSetEnabledTabWidget(self, id: int):
        if id == 0:
            self.ui.tabWidget.setEnabled(False)
        elif id == 1:
            self.ui.tabWidget.setEnabled(True)

    @QtCore.Slot()
    def slotLoadFile(self):
        filenames, okay = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            '选择需要处理的票据（一个或多个）',
            '.',
            'PDF Files(*.pdf)',
        )

        if not okay:
            return

        # self.fileInfo['dirname'] = os.path.dirname(filenames[0])
        # self.fileInfo['files'] = {filename: {} for filename in filenames}
        self.sigFileUpdated.emit(filenames)

    @QtCore.Slot(list)
    def slotFileUpdate(self, filenames):
        self.sigFileNumChanged.emit(len(filenames))
        self.sigProgressBarChanged.emit(0)

    @QtCore.Slot()
    def slotClear(self):
        self.sigFileUpdated.emit([])

    @QtCore.Slot()
    def slotStart(self):

        if not self.isValidUserName():
            return

        # if len(self.fileInfo) <= 0:
        #     return

        # self.ui.progressBar.setMaximum(len(self.fileInfo['files']))

        ocrMethodId = 0

        if self.radioButtonGroup.checkedId() == 0:
            args = None
            ocrMethodId = 0
        else:
            ind = self.ui.tabWidget.currentIndex()
            if ind == 0:
                args = None
            elif ind == 1:
                args = None
            ocrMethodId = ind + 1

        self.sigStartClicked.emit({'ocrMethodId': ocrMethodId, 'args': None})

    def isValidUserName(self):
        userName = self.ui.lineEdit_userName.text().strip()
        if len(userName) == 0:
            # self.userName = ''
            self.ui.lineEdit_userName.setStyleSheet(
                "QLineEdit{border:1px solid rgb(255, 0, 0);}")
            return False
        else:
            self.ui.lineEdit_userName.setStyleSheet(
                "QLineEdit{border:1px solid rgb(0, 0, 0);}")
            if userName != self.userName:
                self.sigUserNameChanged.emit(userName)
            return True

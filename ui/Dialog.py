'''
Author: mukangt
Date: 2021-07-13 17:45:15
LastEditors: mukangt
LastEditTime: 2021-07-15 18:46:41
Description: 
'''
import os
import shutil
from collections import defaultdict

import pandas as pd
from PyQt5 import QtCore, QtWidgets

from .listItem import ListItem
from .ocr import *
from .Ui_Dialog import Ui_Dialog


class Dialog(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle('票据报销小工具')

        # saving filenames & invoice info
        self.fileInfo = defaultdict(dict)
        self.fileDir = ''

        self.initUI()

        self.initOcrMethod()

        self.connectSigSlot()

    def initUI(self):
        # reset progress bar
        self.ui.progressBar.setValue(0)

        # disable reset button
        self.ui.pushButton_reset.setVisible(False)

        # initialize radio button
        self.radioButtonGroup = QtWidgets.QButtonGroup(self)
        self.radioButtonGroup.addButton(self.ui.radioButton_local, 0)
        self.radioButtonGroup.addButton(self.ui.radioButton_cloud, 1)
        self.ui.radioButton_local.setChecked(True)

        # initialize tab widget
        self.ui.tabWidget.setEnabled(False)
        self.ui.tabWidget.setCurrentIndex(0)

    def initOcrMethod(self):
        self.ocrMethod = {}
        self.ocrMethod[0] = localOcr
        # self.ocrMethod[1] = self.cloudOcr

    def connectSigSlot(self):
        # radio button & tab widget
        self.radioButtonGroup.idClicked.connect(self.slotSetEnabledTabWidget)

        # load files
        self.ui.pushButton_loadFile.clicked.connect(self.slotLoadFiles)

        # start process
        self.ui.pushButton_start.clicked.connect(self.slotStart)

        # export ocr result to excel
        self.ui.pushButton_export.clicked.connect(self.slotExport)

    def resetFiles(self):
        self.ui.listWidget_files.clear()
        self.fileInfo.clear()
        self.ui.progressBar.setValue(0)
        self.fileDir = ''
        # self.ui.lineEdit_name.setText('此处输入姓名')

    def updateListView(self, filenames):
        self.resetFiles()
        self.fileDir = os.path.dirname(filenames[0])
        for filename in filenames:
            # list view add item
            listItem = ListItem(os.path.basename(filename))
            self.ui.listWidget_files.addItem(listItem)

            self.fileInfo[filename] = {}

    def localOcr(self):
        return None

    def defaultCloud(self):
        return None

    def eCloud(self):
        # TODO
        pass

    def slotSetEnabledTabWidget(self, id: int):
        if id == 0:
            self.ui.tabWidget.setEnabled(False)
        elif id == 1:
            self.ui.tabWidget.setEnabled(True)

    def slotLoadFiles(self):
        filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(
            self,
            '选择需要处理的票据（一个或多个）',
            '.',
        )
        # text = '当前需要处理的文件数为：{}个'.format(len(self.filenames))
        # self.ui.label_fileCnt.setText(text)
        if len(filenames) == 0:
            return

        self.updateListView(filenames)

    def slotStart(self):
        if len(self.fileInfo) <= 0:
            return

        self.ui.progressBar.setMaximum(len(self.fileInfo))
        ocrMethodId = 0
        if self.radioButtonGroup.checkedId() == 0:
            args = self.localOcr()
            ocrMethodId = 0
        else:
            ind = self.ui.tabWidget.currentIndex()
            if ind == 0:
                args = self.defaultCloud()
            elif ind == 1:
                args = self.eCloud()
            ocrMethodId = ind + 1

        self.processFile(ocrMethodId, args)

    def slotExport(self):
        if len(self.fileInfo) <= 0:
            return

        # read excel template
        df = pd.read_excel('./ui/resource/template.xlsx',
                           sheet_name='增值税普票',
                           header=1)
        for i, info in enumerate(self.fileInfo.values()):
            info['序号'] = i + 1
            df.loc[i + 1] = [info.get(col, '') for col in df.columns]

        df.to_excel(os.path.join(self.resultDir,
                                 ''.join(['增值税普票_', self.userName, '.xlsx'])),
                    index=False)

    def processFile(self, ocrMethodId, args):
        self.resultDir = os.path.join(self.fileDir, 'results')
        os.makedirs(self.resultDir, exist_ok=True)

        self.userName = self.ui.lineEdit_name.text()

        # deal with files
        for i, filename in enumerate(self.fileInfo.keys()):
            ocrResult = self.ocrMethod[ocrMethodId](filename, args)
            self.fileInfo[filename] = ocrResult

            # copy and rename file
            dstPath = os.path.join(
                self.resultDir, ''.join([
                    ocrResult['发票代码'], '_', ocrResult['发票号码'], '_',
                    self.userName, '.pdf'
                ]))
            shutil.copyfile(filename, dstPath)

            self.ui.progressBar.setValue(i + 1)

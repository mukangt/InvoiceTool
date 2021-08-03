'''
Author: mukangt
Date: 2021-08-02 17:01:53
LastEditors: mukangt
LastEditTime: 2021-08-03 18:52:08
Description: 
'''
import os
import shutil

import pandas as pd
from PySide6 import QtCore, QtWidgets, QtGui

from ocr import localOcr
from ui import MainWindow


class OcrProcess(QtCore.QObject):
    # define signals
    sigOperate = QtCore.Signal(dict)

    # sigFinished = QtCore.Signal()

    def __init__(self) -> None:
        super().__init__()

        self.win = MainWindow()
        self.win.setWindowIcon(QtGui.QIcon(":/icon.png"))

        self.initOcrMethod()

        # self.initWokerThread()

        self.bindOcrSigSlot()

        # self.workerThread.start()

        self.cnt = 0

    def initOcrMethod(self):
        self.ocrMethod = {0: localOcr}

    # def initWokerThread(self):
    #     self.workerThread = QtCore.QThread()
    #     self.worker = Worker()
    #     self.worker.moveToThread(self.workerThread)

    def bindOcrSigSlot(self):
        self.win.sigStartClicked.connect(self.startOcr)
        # self.workerThread.fini.connect(self.worker.deleteLater)
        # self.worker.sigResultReady.connect(self.slotReceiveResult)
        # self.sigOperate.connect(self.worker.doWork)

    @QtCore.Slot(dict)
    def startOcr(self, methodArgs):
        ocrArgs = dict()
        ocrArgs['ocrMethod'] = self.ocrMethod[methodArgs['ocrMethodId']]
        ocrArgs['ocrArgs'] = methodArgs['args']

        self.resultDir = os.path.join(self.win.fileInfo['dirname'], 'results')
        os.makedirs(self.resultDir, exist_ok=True)
        ocrArgs['resultDir'] = self.resultDir
        ocrArgs['userName'] = self.win.username
        # deal with files
        for i, filename in enumerate(self.win.fileInfo['files'].keys()):
            ocrArgs['filename'] = filename

            ocrResult = ocrArgs['ocrMethod'](ocrArgs['filename'],
                                             ocrArgs['ocrArgs'])

            # copy and rename file
            dstPath = os.path.join(
                ocrArgs['resultDir'], ''.join([
                    ocrResult['发票代码'], '_', ocrResult['发票号码'], '_',
                    ocrArgs['userName'], '.pdf'
                ]))
            shutil.copyfile(ocrArgs['filename'], dstPath)

            ocrResult['filename'] = ocrArgs['filename']
            self.win.sigProgressBarChanged.emit(i + 1)
            self.win.fileInfo['files'][ocrResult['filename']] = ocrResult
            # self.sigOperate.emit(ocrArgs)

        # self.workerThread.wait()
        self.exportExcel()

        yes = QtWidgets.QMessageBox.information(
            self.win, '处理结果', '处理结束，是否打开结果文件夹',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.Yes)
        if yes == QtWidgets.QMessageBox.StandardButton.Yes:
            QtGui.QDesktopServices.openUrl(
                QtCore.QUrl.fromLocalFile(ocrArgs['resultDir']))

    def exportExcel(self):
        # read excel template
        df = pd.read_excel('./resource/template.xlsx',
                           sheet_name='增值税普票',
                           header=1)
        for i, info in enumerate(self.win.fileInfo['files'].values()):
            info['序号'] = i + 1
            df.loc[i + 1] = [info.get(col, '') for col in df.columns]

        df.to_excel(os.path.join(
            self.resultDir, ''.join(['增值税普票_', self.win.username, '.xlsx'])),
                    index=False)

    # @QtCore.Slot(dict)
    # def slotReceiveResult(self, ocrResult: dict):
    #     self.cnt += 1
    #     self.sigProgressBarChanged.emit(self.cnt)
    #     self.fileInfo['files'][ocrResult['filename']] = ocrResult


class Worker(QtCore.QObject):
    # define signals
    sigResultReady = QtCore.Signal(dict)

    def __init__(self) -> None:
        super().__init__()

    @QtCore.Slot(dict)
    def doWork(self, args: dict):
        ocrResult = args['ocrMethod'](args['filename'], args['ocrArgs'])

        # copy and rename file
        dstPath = os.path.join(
            args['resultDir'], ''.join([
                ocrResult['发票代码'], '_', ocrResult['发票号码'], '_',
                args['userName'], '.pdf'
            ]))
        shutil.copyfile(args['filename'], dstPath)

        ocrResult['filename'] = args['filename']

        self.sigResultReady.emit(ocrResult)

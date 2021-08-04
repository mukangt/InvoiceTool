'''
Author: mukangt
Date: 2021-08-02 17:01:53
LastEditors: mukangt
LastEditTime: 2021-08-04 16:03:02
Description: 
'''
import os
import resource
import shutil

import xlwings as xw
from PySide6 import QtCore, QtGui, QtWidgets

from ocr import localOcr
from ui import MainWindow


class OcrProcess(QtCore.QObject):
    # define signals
    sigOperate = QtCore.Signal(dict)

    # sigFinished = QtCore.Signal()

    def __init__(self) -> None:
        super().__init__()

        self.init()

        self.initOcrMethod()

        # self.initWokerThread()

        self.bindOcrSigSlot()

        # self.workerThread.start()

    def init(self):
        self.win = MainWindow()
        self.win.setWindowIcon(QtGui.QIcon(':/icon.png'))

        self.fileInfo = {}

        self.saveDir = ''

        self.userName = ''

        self.excelTitles = [
            '序号', '发票种类代码', '发票代码', '发票号码', '发票页码', '开票日期', '校验码后六位', '购方税号',
            '红字信息表号'
        ]

        self.excelExample = [
            '示例无需删除', '04', '053001900666', '01167666', '1', '2019/1/8',
            '236377', '91532500X22813280K'
        ]

        self.excelDescription = '''模板说明：
        1.序号列必填，导入的数据行数与序号需对应，不可出现有序号而无数据的情况
        2.红色字段为必输字段，所有设置下拉框的单元格，请严格按照预设填写                                                                                                                                                                                                                 
        3.请按照发票代码种类对照表选择！
        04-增值税普通发票、10-增值税电子发票、11-增值税普通发票（卷式）、18-增值税电子普通发票（通行费）、 13-桥闸通行费、14-一二级公路通行费、16-其他不可抵扣发票、21-代扣代缴税收缴款凭证、22-其他可抵扣发票、23-航空电子客票行程单、24-火车票、25-其他车票船票、26-试报账虚拟发票 、19-分割单                                                                            
        4.发票代码：当发票种类为04、10、11、18、13、14、19则必填！                                                                                                                          
        5.校验码后六位：当发票种类为04、10、11、18则必填！                                                                                                                                                                                                                                     
        6.红字信息表号：红字发票必填！                                                                                                                                                         
        7.开票日期和购方税号：当发票种类为04、10、11、18、19则必填！
        8.发票页码：非必输，影像查看时会根据此字段将报账单上的发票信息与发票扫描的影像做匹配！'''

        self.cnt = 0

    def initOcrMethod(self):
        self.ocrMethod = {0: localOcr}

    # def initWokerThread(self):
    #     self.workerThread = QtCore.QThread()
    #     self.worker = Worker()
    #     self.worker.moveToThread(self.workerThread)

    def bindOcrSigSlot(self):
        self.win.sigStartClicked.connect(self.slotStartOcr)
        self.win.sigFileUpdated.connect(self.slotFileUpdate)
        self.win.sigUserNameChanged.connect(self.slotUserName)
        # self.workerThread.fini.connect(self.worker.deleteLater)
        # self.worker.sigResultReady.connect(self.slotReceiveResult)
        # self.sigOperate.connect(self.worker.doWork)
    @QtCore.Slot(str)
    def slotUserName(self, userName):
        self.userName = userName

    @QtCore.Slot(list)
    def slotFileUpdate(self, filenames):
        self.fileInfo = {filename: {} for filename in filenames}

        if len(filenames) > 0:
            self.win.ui.progressBar.setMaximum(len(filenames))
            self.saveDir = os.path.join(os.path.dirname(filenames[0]),
                                        'output')

    @QtCore.Slot(dict)
    def slotStartOcr(self, methodArgs):
        if len(self.fileInfo) <= 0:
            return

        os.makedirs(self.saveDir, exist_ok=True)

        ocrMethod = self.ocrMethod[methodArgs['ocrMethodId']]
        ocrArgs = methodArgs['args']

        # deal with files
        for i, filename in enumerate(self.fileInfo.keys()):
            ocrResult = ocrMethod(filename, ocrArgs)

            # copy and rename file
            dstPath = os.path.join(
                self.saveDir, ''.join([
                    ocrResult['发票代码'],
                    '_',
                    ocrResult['发票号码'],
                    '_',
                    self.userName,
                    '.pdf',
                ]))
            shutil.copyfile(filename, dstPath)

            self.win.sigProgressBarChanged.emit(i + 1)
            self.fileInfo[filename] = ocrResult

        # self.workerThread.wait()
        self.exportExcel()

        yes = QtWidgets.QMessageBox.information(
            self.win, '处理结果', '处理结束，是否打开结果文件夹',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.Yes)
        if yes == QtWidgets.QMessageBox.StandardButton.Yes:
            QtGui.QDesktopServices.openUrl(
                QtCore.QUrl.fromLocalFile(self.saveDir))

    def exportExcel(self):
        # new excel and save
        app = xw.App(visible=False, add_book=False)
        wb = app.books.add()
        sheet = wb.sheets['sheet1']
        sheet.value = '增值税普票'
        sheet.autofit()
        # sheet.range('A1').value = self.excelDescription

        colNum = len(self.excelTitles)
        rowNum = len(self.fileInfo) + 2
        sheet.range((1, 1), (rowNum, colNum)).api.NumberFormat = '@'
        sheet.range(1, 1).value = self.excelTitles
        sheet.range(2, 1).value = self.excelExample

        # df = pd.read_excel(':/template.xlsx', sheet_name='增值税普票', header=1)
        for i, info in enumerate(self.fileInfo.values()):
            info['序号'] = str(i + 1)
            # row = 'A{}'.format(i + 3)
            # sheet.range((row,1), (row,colNum)).api.NumberFormat = "@"
            sheet.range('A{}'.format(i + 3)).value = [
                info.get(title, '') for title in self.excelTitles
            ]

            # info['序号'] = i + 1
            # df.loc[i + 1] = [info.get(col, '') for col in df.columns]
        wb.save(
            os.path.join(self.saveDir,
                         ''.join(['增值税普票_', self.userName, '.xlsx'])))
        wb.close()
        app.quit()
        # df.to_excel(os.path.join(self.saveDir,
        #                          ''.join(['增值税普票_', self.userName, '.xlsx'])),
        #             index=False)


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

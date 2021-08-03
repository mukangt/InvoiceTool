'''
Author: mukangt
Date: 2021-07-13 17:53:43
LastEditors: mukangt
LastEditTime: 2021-08-03 16:26:17
Description: 
'''
import sys

from PySide6 import QtWidgets

from OcrProcess import OcrProcess

app = QtWidgets.QApplication(sys.argv)
ocr = OcrProcess()
ocr.win.show()
sys.exit(app.exec())

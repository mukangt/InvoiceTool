'''
Author: mukangt
Date: 2021-07-13 17:53:43
LastEditors: mukangt
LastEditTime: 2021-07-30 11:43:52
Description: 
'''
import sys

from PySide6 import QtWidgets

from Dialog import Dialog

app = QtWidgets.QApplication(sys.argv)
dia = Dialog()
dia.show()
sys.exit(app.exec_())

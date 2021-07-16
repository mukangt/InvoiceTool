'''
Author: mukangt
Date: 2021-07-13 17:53:43
LastEditors: mukangt
LastEditTime: 2021-07-13 17:56:26
Description: 
'''
import sys

from PyQt5 import QtWidgets

from ui import Dialog

app = QtWidgets.QApplication(sys.argv)
dia = Dialog()
dia.show()
sys.exit(app.exec_())
